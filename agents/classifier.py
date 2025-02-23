from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

categories = [
    "Symptoms", "Medications", "Diagnosis", "General Health", "Emergency",
    "Nutrition", "Preventive Care", "Chronic Diseases", "Mental Health", "Alternative Medicine"
]

def classify_query(query: str):
    prompt = ChatPromptTemplate.from_template(
        f"Categorize the following medical query into one of these categories: {', '.join(categories)}. Query: {{query}}"
    )
    chain = prompt | ChatOpenAI(temperature=0)
    return chain.invoke({"query": query}).content
