# 🍎 Food Nutrition Analyzer & RAG Knowledge Engine

An AI-powered nutrition intelligence system combining **Google Gemini** with **LlamaIndex Retrieval-Augmented Generation (RAG)**. The project features both an interactive **Streamlit** dashboard and a **FastAPI** REST backend.

---

## 🚀 Features

- **Direct Nutrition Analysis**: Get instant macronutrient, micronutrient, and dietary breakdown for any food item powered by Gemini.
- **RAG Knowledge Base Querying**: Ask natural-language questions across internal nutrition guides and datasets using LlamaIndex and Gemini vector embeddings.
- **Interactive Streamlit Web App**: Clean, responsive dark-themed dashboard with real-time status indicators and tabbed navigation.
- **FastAPI REST API**: High-performance asynchronous endpoints ready for integration with mobile apps, microservices, or frontend clients.
- **Fault-Tolerant Mock Fallback**: Automatic failover to simulated responses when API keys are absent or rate limits are reached.
- **Structured Logging**: Continuous operation tracking with Loguru.

---

## 📁 Project Structure

```text
basic_rag/
├── config/
│   └── config.yaml          # Model settings (model name, temperature)
├── data/                    # Local text corpora indexed for RAG
│   ├── nutrition_basics.txt
│   └── nutrition_facts.txt
├── logs/                    # Application log files
├── src/
│   ├── __init__.py
│   ├── ai_model.py          # Gemini & LlamaIndex RAG logic with fallback handling
│   └── main.py              # FastAPI REST endpoints
├── .env.example             # Template for API credentials
├── .gitignore               # Git rules protecting secrets, logs, and venvs
├── app.py                   # Streamlit web application
├── requirements.txt         # Python project dependencies
└── README.md                # Project documentation
```

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **LLM & Embeddings**: Google Gemini (`models/gemini-3.5-flash`, `models/gemini-embedding-2`) via `google-generativeai` & `llama-index-llms-gemini`
- **RAG Framework**: LlamaIndex (`VectorStoreIndex`, `SimpleDirectoryReader`)
- **Web UI**: Streamlit
- **REST API**: FastAPI + Uvicorn
- **Logging**: Loguru
- **Configuration**: python-dotenv & PyYAML

---

## ⚙️ Quick Start

### 1. Clone Repository & Set Up Virtual Environment

```bash
git clone <your-repo-url>
cd basic_rag

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On macOS / Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy the example environment file and add your Gemini API Key:

```bash
cp .env.example .env
```

Open `.env` and set:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```
> *Tip: Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/).*

---

## 🖥️ Running the Applications

### 1. Streamlit Web Dashboard

Launch the web interface:

```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

### 2. FastAPI REST Server

Start the FastAPI application:

```bash
uvicorn src.main:app --reload --port 8000
```

- **Root Status**: `http://localhost:8000/`
- **Interactive Swagger Docs**: `http://localhost:8000/docs`
- **Interactive ReDoc**: `http://localhost:8000/redoc`

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check and server status |
| `GET` | `/analyze/{food_item}` | Detailed nutrition breakdown for a food item |
| `GET` | `/ask/{question}` | RAG query over internal nutrition knowledge base |

#### Example cURL

```bash
# Query food nutrition
curl -X GET "http://localhost:8000/analyze/Avocado%20Toast"

# Ask knowledge base
curl -X GET "http://localhost:8000/ask/What%20is%20the%20recommended%20calorie%20intake?"
```

---

## 🔒 Security Note

Never commit `.env` or sensitive credentials to version control. The included `.gitignore` protects your secret keys, local logs, and virtual environments.

