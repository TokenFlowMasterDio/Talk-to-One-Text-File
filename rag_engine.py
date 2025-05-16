from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama


def load_text(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    embeddings = OllamaEmbeddings(model="mistral")
    db = FAISS.from_documents(texts, embeddings)
    return db


def answer_question_with_refinement(db, question):
    retriever = db.as_retriever()
    llm = Ollama(model="mistral")
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False
    )
    result = qa_chain.invoke({"query": question})
    return result["result"]
