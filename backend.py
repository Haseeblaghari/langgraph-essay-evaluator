# Import core components from LangGraph
# StateGraph is used to define a graph-based workflow
# START and END represent the entry and exit points of the graph
from langgraph.graph import StateGraph, START, END

# Import Ollama-based LLM wrapper from LangChain
from langchain_ollama import ChatOllama

# TypedDict is used to strictly define the structure of the shared state
from typing import TypedDict


# =========================
# STATE DEFINITION
# =========================
# This defines the shared state that flows through the graph.
# Each node can read from and write to this state.
class EssayState(TypedDict):
    essay: str        # Input essay text
    score: int        # Numerical score for the essay
    feedback: str     # Analytical feedback from the LLM
    suggestion: str  # Improvement suggestions


# Initialize the LLM (Ollama with LLaMA 3.1 model)
llm = ChatOllama(model="llama3.1")


# =========================
# NODE 1: Essay Analysis
# =========================
# This node analyzes the essay and provides summarized feedback
# based on grammar, clarity, structure, vocabulary, and coherence.
def analyze_essay_node(state: EssayState):

    prompt = f"""
Analyze and give summarize feedback the following essay based on:
    - Grammar
    - Clarity
    - Structure
    - Vocabulary
    - Coherence

    Essay:
    {state["essay"]}
"""
    
    # Invoke the LLM with the analysis prompt
    response = llm.invoke(prompt)

    # Return feedback to be stored in the shared state
    return {"feedback": response.content}


# =========================
# NODE 2: Scoring
# =========================
# This node assigns a numerical score (out of 100) to the essay.
def score_node(state: EssayState):
    prompt = f"""
Give a score out of 100 for this essay.
    Only return a number.

    Essay:
    {state["essay"]}
"""
    
    # Invoke the LLM to generate a score
    response = llm.invoke(prompt)

    # Convert the LLM output into an integer score
    return {"score": int(response.content.strip())}


# =========================
# NODE 3: Improvement Suggestions
# =========================
# This node suggests clear improvements based on the essay
# and the feedback generated in earlier steps.
def suggest_improvements_node(state: EssayState):

    prompt = f"""
    Based on this essay and feedback, suggest clear improvements.

    Essay:
    {state["essay"]}

    Feedback:
    {state["feedback"]}
    """

    # Invoke the LLM to generate suggestions
    response = llm.invoke(prompt)

    # Return improvement suggestions to the shared state
    return {"suggestion": response.content}


# =========================
# GRAPH CONSTRUCTION
# =========================
# Initialize a StateGraph with the defined EssayState
graph = StateGraph(EssayState)

# Register nodes in the graph
graph.add_node("analyze", analyze_essay_node)
graph.add_node("score", score_node)
graph.add_node("suggest", suggest_improvements_node)

# Define execution flow (edges) between nodes
graph.add_edge(START, "analyze")   # Start → Analyze essay
graph.add_edge("analyze", "score") # Analyze → Score
graph.add_edge("score", "suggest") # Score → Suggest improvements
graph.add_edge("suggest", END)     # Suggest → End

# Compile the graph into an executable workflow
chat = graph.compile()