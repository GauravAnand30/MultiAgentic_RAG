from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from sentence_transformers import SentenceTransformer
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

class PDFLoader:
    def __init__(self, pdf_path="C:\\Users\\Acer\\OneDrive\\Desktop\\NewRAG\\Data\\standard-treatment-guidelines.pdf"):
        self.loader = PyPDFLoader(pdf_path)
        self.documents = self.loader.load()
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_db = FAISS.from_documents(self.documents, self.embeddings)
        self.retriever = self.vector_db.as_retriever()

    def retrieve_info(self, query):
        return self.retriever.get_relevant_documents(query)
