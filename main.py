import streamlit as st
from openai import OpenAI
from pymongo import MongoClient
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
#ollama
client=OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
#streamlit
st.set_page_config(page_title="AI Smart Email Reply Generator for Professionals")
st.title("AI Smart Email Generator")
st.markdown("-------------")


coil1,coil2=st.columns([2,1])

with coil1:
    rough_message=st.text_area(
        "Write Here!",
        placeholder="e.g.,tell boss ur sick,wont come today,will finish report by monday",
        height=150
    )

with coil2:
    tone=st.selectbox(
        "Select Tone:",
        ["Proffesional","Polite","Assertive","Friendly"]
    )

#MongoDB setup
mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
db = mongo_client["email_ai"]
collection = db["documents"]

#MongoDB
if st.button(" Save as Memory"):
    if rough_message.strip():
        collection.insert_one({
            "user_id": "1",
            "content": rough_message
        })
        st.success("Saved to memory!")
    else:
        st.warning("Nothing to save!")
def load_user_memory(user_id):
    docs = collection.find({"user_id": user_id})
    return [Document(page_content=d["content"]) for d in docs]

#PromptEngineering
if st.button(" Generate Smart Reply", use_container_width=True):

    if not rough_message.strip():
        st.error("Enter a rough message first!")

    else:
        with st.spinner("AI is crafting your email..."):

            try:
                documents = load_user_memory("1")

                if documents:
                    splitter = RecursiveCharacterTextSplitter(
                        chunk_size=300,
                        chunk_overlap=50
                    )

                    chunks = splitter.split_documents(documents)

                    embeddings = OllamaEmbeddings(model="nomic-embed-text")

                    vectorstore = FAISS.from_documents(chunks, embeddings)
                    retriever = vectorstore.as_retriever()

                    relevant_docs = retriever.invoke(rough_message)

                    context = "\n".join([doc.page_content for doc in relevant_docs])
                else:
                    context = "No user memory available."
                system_instruction = f"""
You are a professional email assistant.

Use the user's background to personalize the email.

User Background:
{context}

Rules:
- Maintain {tone} tone
- Include subject line
- Keep it clear and professional
- Add appropriate greeting and closing
"""

                full_prompt = f"""
{system_instruction}

### Rough Notes:
{rough_message}

### Final Email:
"""

                #olama call to api
                response = client.chat.completions.create(
                    model="llama3.1",
                    messages=[
                        {"role": "user", "content": full_prompt}
                    ],
                    temperature=0.5
                )

                #output
                result = response.choices[0].message.content

                st.markdown("### Generated Email")
                st.success("Done!")
                st.code(result, language="markdown")
            except Exception as e:
                st.error(f"Error: {e}")
