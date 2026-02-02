# 📄 Essay Scoring and Feedback App

This repository contains a **Streamlit-based web app** that allows users to submit essays and receive:  

- **Score out of 100**  
- **Detailed feedback**  
- **Improvement suggestions**  

The backend uses **LangGraph** with a **LangChain Ollama LLaMA 3.1 model** to analyze essays intelligently.

---

## 🧩 Features

1. **Multiple Submission Options**  
   - Write or paste essay text directly  
   - Upload essay as a PDF (text automatically extracted)

2. **AI-Based Essay Analysis**  
   - Grammar, clarity, structure, vocabulary, and coherence are analyzed  
   - Provides feedback, score, and improvement suggestions

3. **Interactive UI**  
   - Built with **Streamlit** for an easy-to-use interface  
   - Real-time results with a loading spinner while processing

---

## 🚀 Installation

1. **Clone the repository**  
```bash
git clone https://github.com/yourusername/essay-scoring-app.git
cd essay-scoring-app
Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
Install dependencies

pip install -r requirements.txt
Setup LLM (Ollama LLaMA 3.1)

Make sure your Ollama environment is configured properly

Replace the model name in essay_scoring.py if needed

📝 Usage
Run the Streamlit app

streamlit run app.py
Open in your browser

The app will run at http://localhost:8501

Submit an essay

Choose between writing text or uploading PDF

Click Submit Essay to get:

Essay Score

Detailed Feedback

Suggestions for improvement

🛠️ Code Structure
essay-scoring-app/
│
├─ app.py                 # Streamlit front-end interface
├─ essay_scoring.py       # LangGraph workflow for essay analysis
├─ requirements.txt       # Python dependencies
└─ README.md
essay_scoring.py contains the graph-based workflow:

Analyze node: analyzes essay and generates feedback

Score node: gives numerical score

Suggest node: provides improvement suggestions

app.py handles user interaction via Streamlit and invokes the workflow.

⚡ Technologies Used
Python

Streamlit

PyPDF2

LangChain Ollama

LangGraph

📈 Future Improvements
Support for more document formats (DOCX, TXT)

Advanced rubric-based scoring

Multi-language essay support

Deploy as a cloud app
