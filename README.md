📝 LangGraph Essay Evaluator
An intelligent, multi-agent automated essay grading system. This project uses LangGraph to orchestrate a sequential workflow where different "nodes" (agents) analyze, score, and provide feedback on essays—all running locally via Ollama.

🚀 Key Features
Agentic Workflow: Uses a state-based graph to ensure a structured analysis pipeline.

Deep Analysis: Evaluates essays based on Grammar, Clarity, Structure, Vocabulary, and Coherence.

Dual Input Support:

Text: Paste your essay directly into the UI.

PDF: Upload documents for automatic text extraction.

Local & Private: Powered by Llama 3.1 via Ollama; no data ever leaves your machine.

Modern UI: Interactive dashboard built with Streamlit.

🏗️ Architecture
The application follows a directed workflow:

Analyze: Summarizes strengths and weaknesses.

Score: Generates a numerical value (0-100).

Suggest: Provides actionable tips based on the analysis and score.

🛠️ Tech Stack
Frameworks: LangGraph, LangChain

LLM: Ollama (Llama 3.1)

Frontend: Streamlit

Parsing: PyPDF2

📋 Prerequisites
Install Ollama: Download here.

Pull the Model:

Bash
ollama pull llama3.1
⚙️ Installation & Setup
Clone the Repo:

Bash
git clone https://github.com/your-username/langgraph-essay-evaluator.git
cd langgraph-essay-evaluator
Install Dependencies:

Bash
pip install -r requirements.txt
Run the App:

Bash
streamlit run app.py
📂 Project Structure
app.py: The Streamlit interface and PDF processing logic.

essay_scoring.py: The LangGraph definition and node logic.

requirements.txt: List of necessary Python packages.
