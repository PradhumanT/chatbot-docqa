# 🧠 LangChain Document Chatbot (Phase 1)

This project is an end-to-end implementation of a document-aware chatbot powered by LangChain, Pinecone, and Google Gemini (via `langchain-google-genai`). The assistant answers user queries based strictly on the content of a given document.

---

## 🚀 Features

- 📄 Load and process `.pdf` documents
- ✂️ Chunk documents and generate semantic embeddings
- 📦 Store & retrieve embeddings using **Pinecone vector DB**
- 🧠 Run a Retrieval-Augmented Generation (RAG) chain with **Gemini LLM**
- 🚫 Restricts answers to only what's in the document (hallucination guard)
- 🖥️ Fully modularized into a Python app (backend only)
- ✅ Ready for productionization or integration into UI frameworks (Streamlit, FastAPI)

---

## 🧱 Project Structure

```
chatbot-docqa/
├── app/
│   ├── config.py              # Load env variables
│   ├── loader.py              # Load and parse PDF files
│   ├── splitter.py            # Text chunking logic
│   ├── embeddings.py          # Embedding model (HuggingFace)
│   ├── vector_store.py        # Pinecone logic (init, save, load)
│   └── chatbot.py             # RetrievalQA chain with custom prompt
│
├── main.py                    # CLI entry point to chat
├── data/                      # Folder for input documents
├── .env                       # API keys (not committed)
├── requirements.txt           # Dependencies
├── README.md                  # You're here!
└── .gitignore
```

---

## 🛠️ Technologies Used

- [LangChain](https://www.langchain.com/)
- [Pinecone](https://www.pinecone.io/) for vector search
- [Gemini Pro](https://ai.google.dev/) via `langchain-google-genai`
- [Hugging Face Embeddings](https://www.sbert.net/) — MiniLM-L6-v2
- PDF parsing with `pypdf`
- Environment management via `python-dotenv`

---

## 📥 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/chatbot-docqa.git
   cd chatbot-docqa
   ```

2. Create and activate a virtual environment (or use conda):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:
   ```env
   PINECONE_API_KEY=your-pinecone-key
   GOOGLE_API_KEY=your-gemini-api-key
   ```

5. Add your document inside the `data/` folder (e.g., `attention-is-all-you-need.pdf`)

6. Run the chatbot:
   ```bash
   python main.py
   ```

---

## 📌 Example Query

```
Ask a question (or type 'exit'): What is the transformer architecture described in this paper?
Answer:
The paper introduces a novel transformer model that relies solely on attention mechanisms to model dependencies between input and output...
```

---

## ✅ Next Phase (Planned)

We're now expanding this project into a **LangChain Agent App** with:

- 🧠 Python execution
- 🌐 Web search + Wikipedia lookup
- 📄 Real-time RAG from user-uploaded documents
- 💬 Context-aware, multi-turn conversations
- 🖥️ Full Streamlit frontend
- ☁️ AWS EC2 deployment

➡️ Follow the next repo: [coming soon...]

---

## 📄 License

MIT License — feel free to fork, extend, and remix!
