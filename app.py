import streamlit as st
import os
import yaml
from src.ai_model import get_nutrition_info, query_nutrition_knowledge

# Page configuration
st.set_page_config(
    page_title="Agentic AI - Food Nutrition Analyzer",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Premium Styling
st.markdown("""
<style>
    /* Main Background and Styling */
    .stApp {
        background: linear-gradient(135deg, #0e1117 0%, #161b22 100%);
        color: #c9d1d9;
    }
    
    /* Header Customization */
    .main-header {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .sub-header {
        color: #8b949e;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }
    
    /* Status indicators */
    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    
    .status-active {
        background-color: rgba(56, 189, 248, 0.15);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.3);
    }
    
    .status-warning {
        background-color: rgba(245, 158, 11, 0.15);
        color: #f59e0b;
        border: 1px solid rgba(245, 158, 11, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# App Title & Subtitle
st.markdown('<h1 class="main-header">AGENTIC AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Based Food Nutrition Analyzer & Knowledge Engine</p>', unsafe_allow_html=True)

# Read config if available
config = {}
if os.path.exists("config/config.yaml"):
    try:
        with open("config/config.yaml", "r") as f:
            config = yaml.safe_load(f) or {}
    except Exception:
        pass

model_name = config.get("api", {}).get("model", "models/gemini-1.5-flash")
temperature = config.get("api", {}).get("temperature", 0.7)

# Sidebar
st.sidebar.markdown("### ⚙️ Engine Settings")
st.sidebar.markdown(f"**Model**: `{model_name}`")
st.sidebar.markdown(f"**Temperature**: `{temperature}`")

st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ Connection Status")

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if api_key and "your_gemini_api_key" not in api_key and "your_google_api_key" not in api_key:
    st.sidebar.markdown('<span class="status-badge status-active">● API Key Configured</span>', unsafe_allow_html=True)
else:
    st.sidebar.markdown('<span class="status-badge status-warning">▲ Key Missing/Placeholder</span>', unsafe_allow_html=True)
    st.sidebar.info("Add your `GEMINI_API_KEY` to the `.env` file for Gemini queries to work.")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📂 Data Source")
st.sidebar.write("Local index directory: `data/`")


# Tabs for separate features
tab1, tab2 = st.tabs(["🍎 Food Nutrition Info", "📖 Query Knowledge Base"])

with tab1:
    st.markdown("### Fetch Detailed Nutrition Info")
    st.write("Get a comprehensive breakdown of ingredients, macronutrients, and health details for any food item.")
    
    food_item = st.text_input("Enter a food item (e.g. Avocado Toast, Grilled Salmon, Apple)", key="food_input")
    
    if st.button("Analyze Nutrition", type="primary"):
        if food_item.strip():
            with st.spinner(f"Analyzing '{food_item}'..."):
                response = get_nutrition_info(food_item)
                st.markdown("#### Analysis Result")
                st.markdown(response)
        else:
            st.warning("Please enter a valid food item.")

with tab2:
    st.markdown("### Ask Food & Nutrition Questions")
    st.write("Query the documents loaded in the local `data/` folder using LlamaIndex.")
    
    question = st.text_input("Ask a question about the loaded documentation (e.g. What is the recommended calorie intake?)", key="kb_input")
    
    if st.button("Query Knowledge Base", type="primary"):
        if question.strip():
            with st.spinner("Searching knowledge base..."):
                response = query_nutrition_knowledge(question)
                st.markdown("#### Answer")
                st.markdown(response)
        else:
            st.warning("Please enter a valid question.")
