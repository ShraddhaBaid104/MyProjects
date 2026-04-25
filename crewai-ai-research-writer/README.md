# 🤖 CrewAI AI Research & Writing System

A multi-agent AI system built using CrewAI and OpenAI that automates research and content creation through collaborative agents.

---

## 📌 Overview

This project demonstrates how multiple AI agents can work together to solve complex tasks using a structured workflow.

* A **Research Agent** gathers and analyzes information
* A **Writer Agent** transforms research into structured content
* Tasks are orchestrated sequentially using CrewAI

This project highlights the power of **agentic AI systems** built on top of modern LLMs.

---

## 🚀 Features

* Multi-agent collaboration using CrewAI
* Task-based execution pipeline
* Modular and extensible architecture
* Powered by OpenAI language models
* Clean and scalable project structure

---

## 🧠 Architecture

```
User Input
   ↓
Research Agent → gathers insights
   ↓
Writer Agent → generates content
   ↓
Final Output
```

---

## 🛠️ Tech Stack

* CrewAI
* LangChain
* OpenAI API
* Python 3.12
* python-dotenv

---

## 📁 Project Structure

```
crewai-ai-research-writer/
│
├── agents.py        # Defines AI agents
├── tasks.py         # Defines tasks
├── main.py          # Entry point
├── tools.py         # (Optional extensions)
├── .env.example     # API key template
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/ShraddhaBaid104/crewai-ai-research-writer.git
cd crewai-ai-research-writer
```

### 2. Create virtual environment

```bash
uv venv
.venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
uv pip install crewai langchain openai python-dotenv
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🧪 Example Workflow

1. Research agent collects information about a topic
2. Writer agent converts it into a structured article
3. Final output is generated automatically

---

## 📈 Future Improvements

* Add Retrieval-Augmented Generation (RAG)
* Integrate external APIs and tools
* Build a frontend interface (Streamlit / FastAPI)
* Add evaluation metrics for output quality

---

## 🎯 Learning Outcomes

* Multi-agent system design
* Task orchestration with CrewAI
* LLM integration using OpenAI
* Building modular AI pipelines

---

## 📄 License

This project is for educational and demonstration purposes.
