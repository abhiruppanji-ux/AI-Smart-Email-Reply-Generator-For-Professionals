## 📧 AI Smart Email Reply Generator

An AI-powered web app that converts rough notes into **professional, structured emails** with customizable tone and memory-based personalization.

Built using **Streamlit, Ollama (LLaMA 3.1), LangChain, FAISS, and MongoDB**.

---

## 🚀 Features

* ✨ Generate professional emails from rough input
* 🎯 Multiple tones: Professional, Polite, Assertive, Friendly
* 🧠 Memory storage using MongoDB
* 🔍 Context-aware generation using FAISS similarity search
* 🤖 Runs locally with Ollama (no paid API required)
* ⚡ Simple and interactive Streamlit UI

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **LLM:** LLaMA 3.1 via Ollama
* **Embeddings:** nomic-embed-text
* **Vector Store:** FAISS
* **Database:** MongoDB
* **Framework:** LangChain

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/your-username/ai-email-generator.git
cd ai-email-generator
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run MongoDB

```
mongod
```

### 4. Setup Ollama

```
ollama pull llama3.1
ollama pull nomic-embed-text
ollama serve
```

### 5. Run Application

```
streamlit run app.py
```

---

## 💡 Usage

1. Enter rough email notes
2. Select desired tone
3. (Optional) Save input as memory
4. Click **Generate Smart Reply**
5. Get a polished, professional email

---

## 📌 Example

**Input:**
`tell boss ur sick, wont come today, will finish report by monday`

**Output:**
A complete email with subject, greeting, body, and closing in selected tone.

---

## 🔮 Future Enhancements

* User authentication
* Email sending integration (Gmail/SMTP)
* Cloud deployment
* Improved long-term memory

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Your Name
GitHub: [https://github.com/your-username](https://github.com/your-username)
