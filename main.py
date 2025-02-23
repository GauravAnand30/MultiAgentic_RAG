from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import logging
from services.langgraph_workflow import medical_ai

app = FastAPI()

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Serve static frontend files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query_medical_ai(request: QueryRequest):
    logging.debug(f"Received query: {request.query}")
    
    try:
        result = medical_ai.invoke({"query": request.query})
        logging.debug(f"Medical AI Response: {result}")
        
        return {
            "category": result.get("category", "Unknown"),
            "response": result.get("final_response", "No response available"),
        }
    except Exception as e:
        logging.error(f"Error processing query: {e}")
        return {"error": "Failed to process the query"}

@app.get("/")
def read_root():
    return FileResponse("frontend/index.html")
