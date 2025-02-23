from services.pdf_loader import PDFLoader

pdf_loader = PDFLoader()

def retrieve_from_pdfs(query: str):
    docs = pdf_loader.retrieve_info(query)
    return " ".join([doc.page_content for doc in docs])
