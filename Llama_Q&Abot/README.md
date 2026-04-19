# 📚 Local RAG System using LlamaIndex + Ollama

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline using **LlamaIndex**, **Ollama**, and **HuggingFace embeddings**. It allows you to query a local PDF document interactively using a lightweight local LLM.

---

## 🚀 Features

* 📄 Load and process PDF documents
* ✂️ Chunk documents into manageable nodes
* 🧠 Generate embeddings using a lightweight model
* 🔍 Retrieve relevant context using vector search
* 🤖 Query using a local LLM via Ollama
* 💾 Persistent storage of index (no need to rebuild every time)

---

## 🛠️ Tech Stack

* **LlamaIndex** – Data framework for LLM applications
* **Ollama** – Local LLM inference (TinyLlama)
* **HuggingFace Embeddings** – `all-MiniLM-L6-v2`
* **Python 3.12+**

---

## 📂 Project Structure

```
.
├── data/
│   └── Spain.pdf          # Input document
├── storage/               # Persisted index (auto-created)
├── main.py                # Main script
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install and run Ollama

Download and install Ollama from: https://ollama.com

Then pull the model:

```bash
ollama pull tinyllama
```

---

## ▶️ Running the Project

```bash
python main.py
```

You’ll see:

```
🔄 Creating new index...
```

or

```
⚡ Loading existing index...
```

Then start asking questions:

```
Ask a question (type 'exit' to quit):
```

---

## 💡 Example Queries

* What is Spain known for?
* What are the major cities in Spain?
* Describe the culture of Spain

---

## 🔁 How It Works

1. Load PDF using `SimpleDirectoryReader`
2. Split text into chunks using `SimpleNodeParser`
3. Convert chunks into embeddings
4. Store in vector index
5. Retrieve top-k relevant chunks
6. Pass context to LLM for answer generation

---

## 🧠 Configuration Details

### LLM (Ollama)

```python
Settings.llm = Ollama(
    model="tinyllama",
    request_timeout=120.0
)
```

### Embeddings

```python
Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

---

## ⚠️ Troubleshooting

### ❌ Model memory error

If you see:

```
model requires more system memory
```

👉 Try:

* Closing background apps
* Using a smaller model
* Increasing system RAM

---

## 📌 Future Improvements

* Add Streamlit UI
* Support multiple documents
* Add chat history memory
* Deploy as API

---

## 🙌 Acknowledgements

* LlamaIndex team
* Ollama for local LLMs
* HuggingFace for embeddings

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Contribute

Feel free to fork this repo, open issues, and submit pull requests!
