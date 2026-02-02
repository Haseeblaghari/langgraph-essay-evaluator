# =========================
# IMPORTS
# =========================
import streamlit as st                  # Streamlit for building the web app
from PyPDF2 import PdfReader            # PyPDF2 for reading PDF files
from backend import chat          # Import the compiled LangGraph chatbot workflow


# =========================
# STREAMLIT PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Essay Input App",       # Title of the browser tab
    layout="centered"                   # Center-align the page layout
)


# =========================
# PAGE TITLE AND INSTRUCTIONS
# =========================
st.title("📄 Essay Submission")
st.write("Choose how you want to submit your essay:")


# =========================
# USER INPUT OPTION
# =========================
# Allow users to choose between writing an essay or uploading a PDF
option = st.radio(
    "Select an option:",
    ("Write Essay Text", "Upload Essay PDF")
)

# Initialize essay text variable
essay_text = ""


# =========================
# OPTION 1: WRITE ESSAY TEXT
# =========================
if option == "Write Essay Text":
    essay_text = st.text_area(
        "✍️ Write or paste your essay here:",  # Placeholder text in the text area
        height=250                             # Height of the text box
    )


# =========================
# OPTION 2: UPLOAD ESSAY PDF
# =========================
elif option == "Upload Essay PDF":
    uploaded_file = st.file_uploader(
        "📤 Upload your essay PDF",  # File uploader widget
        type=["pdf"]                 # Only allow PDF files
    )

    if uploaded_file is not None:
        # Read PDF using PyPDF2
        reader = PdfReader(uploaded_file)
        essay_text = ""
        for page in reader.pages:
            essay_text += page.extract_text()  # Extract text from each page

        st.success("✅ PDF uploaded and text extracted successfully!")


# =========================
# SUBMIT BUTTON
# =========================
if st.button("Submit Essay"):
    # Check if essay text is empty
    if not essay_text or essay_text.strip() == "":
        st.warning("⚠️ Please provide an essay before submitting.")
    else:
        # Show loading spinner while the LLM processes the essay
        with st.spinner("🤖 Analyzing essay..."):
            # Invoke the LangGraph chatbot workflow with the essay as input
            results = chat.invoke({"essay": essay_text})

        # =========================
        # DISPLAY RESULTS
        # =========================
        st.subheader("📝 Submitted Essay")
        st.write(essay_text)

        st.subheader("📊 Score")
        st.write(results["score"])

        st.subheader("🧠 Feedback")
        st.write(results["feedback"])

        st.subheader("✏️ Suggestions")
        st.write(results["suggestion"])
