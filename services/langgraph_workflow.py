from typing import Dict, TypedDict
from langgraph.graph import StateGraph, END
from agents.classifier import classify_query
from agents.pdf_retriever import retrieve_from_pdfs
from agents.web_search import retrieve_from_web
from agents.response_generator import generate_response
from agents.escalation import escalate_to_doctor

class MedicalState(TypedDict):
    query: str
    category: str
    retrieved_info: str
    web_search_result: str
    final_response: str

def route_query(state: MedicalState) -> str:
    if state["category"] == "Emergency":
        return "escalate_to_doctor"
    else:
        return "generate_response"

workflow = StateGraph(MedicalState)

workflow.add_node("classify_query", lambda state: {"category": classify_query(state["query"])})
workflow.add_node("retrieve_from_pdfs", lambda state: {"retrieved_info": retrieve_from_pdfs(state["query"])})
workflow.add_node("retrieve_from_web", lambda state: {"web_search_result": retrieve_from_web(state["query"])})
workflow.add_node("generate_response", lambda state: {
    "final_response": generate_response(state["query"], state["retrieved_info"], state["web_search_result"])
})
workflow.add_node("escalate_to_doctor", lambda state: {"final_response": escalate_to_doctor()})

workflow.add_edge("classify_query", "retrieve_from_pdfs")
workflow.add_edge("retrieve_from_pdfs", "retrieve_from_web")
workflow.add_edge("retrieve_from_web", "generate_response")

workflow.add_conditional_edges("classify_query", route_query, {
    "generate_response": "generate_response",
    "escalate_to_doctor": "escalate_to_doctor"
})

workflow.add_edge("generate_response", END)
workflow.add_edge("escalate_to_doctor", END)

workflow.set_entry_point("classify_query")
medical_ai = workflow.compile()
