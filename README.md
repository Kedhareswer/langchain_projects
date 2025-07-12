# 🔗 LangChain Projects

This repository is a collection of modular and production-grade LangChain projects built with advanced tools such as Groq, FAISS, Pinecone, and Streamlit. Each project explores a different aspect of large language models (LLMs) and agent-based systems for practical AI-powered applications.

---

## 🚀 Projects Included

### 1. 📄 Document Q&A Chatbot
Upload PDFs and ask questions directly from the content using RAG (Retrieval-Augmented Generation).

- **Tech Stack:** LangChain, Groq LLM, Pinecone/FAISS, PyMuPDF
- **Highlights:** Document chunking, semantic search, vector store, Streamlit UI (optional)

---

### 2. 🧠 Code Assistant
Paste any Python code and get intelligent responses including debugging help, explanations, or refactoring suggestions.

- **Tech Stack:** LangChain, PythonREPLTool, Groq LLM
- **Highlights:** Code execution with LangChain tools, memory-based chat (optional)

---

### 3. 🧮 Math Assistant
Symbolically compute derivatives and integrals using SymPy and LangChain agents.

- **Tech Stack:** SymPy, LangChain Tools, Groq
- **Highlights:** Custom tools (`sympy_derivative`, `sympy_integral`), expression rendering in LaTeX

---

### 4. 🧑‍🔬 Autonomous Research Agent (In Progress)
Ask a research question → the agent fetches papers → parses + summarizes findings → generates citations.

- **Tech Stack:** LangChain Agents, ArXiv API, PyMuPDF, metadata-based citation generation
- **Highlights:** Multi-step planning, paper loader, citation formatting, optional UI

---

## 📂 Structure

```

langchain\_projects/
│
├── document\_qa/
│   └── app.py, rag\_pipeline.py, utils.py
│
├── code\_assistant/
│   └── notebook\_demo.ipynb
│
├── math\_assistant/
│   └── sympy\_tools.py, math\_agent.ipynb
│
├── autonomous\_research\_agent/
│   └── planner.py, paper\_parser.py, summarize.py
│
└── README.md

````

---

## 🧪 Setup

1. Clone the repo  
```bash
git clone https://github.com/Kedhareswer/langchain_projects.git
cd langchain_projects
````

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your API keys:

```
GROQ_API_KEY=your-groq-key
PINECONE_API_KEY=your-pinecone-key
```

---

## 🛠️ Tools & Technologies

* [LangChain](https://github.com/langchain-ai/langchain)
* [Groq LLM](https://console.groq.com/)
* [Pinecone / FAISS](https://www.pinecone.io/)
* [SymPy](https://www.sympy.org/)
* [Streamlit](https://streamlit.io/)
* [PyMuPDF / pdfplumber](https://pymupdf.readthedocs.io/)

---

## 📌 Roadmap

* [x] Document Q\&A system with Groq + Pinecone
* [x] Code execution agent with PythonREPL
* [x] Math assistant with symbolic tools
* [ ] Research planner with citation generation
* [ ] Streamlit UI for all apps

---

## 🤝 Contributing

Pull requests and ideas are welcome! Open an issue for suggestions or bugs.

---

---

Let me know if you'd like the `requirements.txt`, `.env.example`, or project-specific README files added as well.
```
