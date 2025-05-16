# 🧠 Talk to One Text File

A local AI-powered app that lets you upload a `.txt` file and ask questions about its contents. It’s built with:

- 🧠 [Mistral 7B](https://ollama.com/library/mistral) (running locally via Ollama)
- 💬 [Gradio](https://www.gradio.app/) for a sleek chat UI
- 🧩 LangChain + Sentence Transformers for chunking and retrieval

---

### 🚀 How It Works

1. Upload a `.txt` file (up to 200MB)
2. The app chunks and embeds it locally
3. Ask questions — the RAG engine fetches relevant context and sends it to Mistral for answering

Everything runs 100% locally — no OpenAI key, no cloud dependencies.

---

### 🔧 Use Case

- Chat with research papers
- Interact with documentation
- Summarize books or articles
- Offline privacy-focused workflows

---

### 📦 Tech Stack

| Component         | Purpose                    |
|------------------|----------------------------|
| **Gradio**        | Frontend Chat Interface    |
| **LangChain**     | RAG + Embedding Pipeline   |
| **SentenceTransformers** | Text Embeddings       |
| **Mistral via Ollama** | Local LLM Inference    |

---

### 🛠️ Run Locally

```bash
# 1. Clone
git clone https://github.com/TokenFlowMasterDio/Talk-to-One-Text-File.git
cd Talk-to-One-Text-File

# 2. Set up environment
python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate on Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start Ollama (if not running)
ollama run mistral

# 5. Launch the app
python main.py
