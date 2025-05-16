import streamlit as st
from rag_engine import load_text, answer_question_with_refinement

st.set_page_config(page_title="Talk to One Text File", layout="centered")
st.title("🧠 Talk to One Text File")

uploaded_file = st.file_uploader("Upload your `.txt` file", type=["txt"])

if uploaded_file:
    with st.spinner("Reading & Indexing..."):
        file_path = f"temp_uploaded_file.txt"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        db = load_text(file_path)
        st.success("File indexed! Ask your questions below.")

        question = st.text_input("Ask a question about the text:")
        if question:
            with st.spinner("Thinking..."):
                answer = answer_question_with_refinement(db, question)
                st.write("🧠 **Answer:**", answer)




