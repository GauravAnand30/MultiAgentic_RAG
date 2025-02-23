from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def generate_response(query: str, pdf_data: str, web_data: str):
    prompt = ChatPromptTemplate.from_template(
        "Using the provided medical knowledge and web search data, generate a detailed response. \n\n"
        "Medical PDF Data: {pdf_data} \n"
        "Web Search Data: {web_data} \n"
        "Query: {query}"
    )
    chain = prompt | ChatOpenAI(temperature=0)
    return chain.invoke({
        "query": query,
        "pdf_data": pdf_data,
        "web_data": web_data
    }).content
