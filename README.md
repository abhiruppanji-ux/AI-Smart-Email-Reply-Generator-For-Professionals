##📧 AI Smart Email Reply Generator

An intelligent email assistant built with Streamlit, Ollama, LangChain, and MongoDB that converts rough notes into professional, well-structured emails with customizable tone and memory-based personalization.

🚀 Features

✨ Convert rough text into polished emails

🎯 Select tone: Professional, Polite, Assertive, Friendly

🧠 Memory system using MongoDB (stores previous inputs)

🔍 Context-aware email generation using vector search (FAISS)

🤖 Powered by LLaMA 3.1 (Ollama)

⚡ Fast and interactive UI with Streamlit

🛠️ Tech Stack

Frontend/UI: Streamlit

LLM: Ollama (LLaMA 3.1)

Embeddings: nomic-embed-text

Vector DB: FAISS

Database: MongoDB

Frameworks: LangChain

📂 Project Structure
├── app.py              # Main Streamlit application
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/ai-email-generator.git
cd ai-email-generator
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Start MongoDB

Make sure MongoDB is running locally:

mongod
4️⃣ Install & Run Ollama

Download Ollama: https://ollama.com/

Pull required models:

ollama pull llama3.1
ollama pull nomic-embed-text

Start Ollama server:

ollama serve
▶️ Run the App
streamlit run app.py
💡 How It Works

User enters rough email notes

Optional: Save input as memory in MongoDB

System retrieves past memory using FAISS similarity search

LLM generates a structured email using:

Context

Selected tone

Prompt engineering

🧪 Example Input
tell boss ur sick, wont come today, will finish report by monday
✅ Output

Professional email

Proper subject line

Formal tone

Structured message

🔮 Future Improvements

🔐 User authentication system

☁️ Cloud deployment (AWS/GCP)

📩 Email sending integration (SMTP/Gmail API)

🧠 Better long-term memory handling

🎨 UI enhancements

🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Your Name

GitHub: https://github.com/your-username
