# Multiagentic Medical RAG Q&A

## Overview
**Multiagentic Medical RAG Q&A** is an advanced medical information retrieval system that leverages **Retrieval-Augmented Generation (RAG)** with multiple intelligent agents. It integrates structured document parsing, real-time web search, knowledge retrieval, and AI-powered response generation to assist users with medical-related queries.

## Project Structure

### 1️⃣ Data Ingestion (PyPDF & Web Data)
- Extracts structured text from medical PDFs using **PyPDF**.
- Fetches real-time medical information from **DuckDuckGo**, **Wikipedia**, and other trusted medical sources.

### 2️⃣ Query Categorization Agent (LLM - Agent 1)
- Classifies user queries into **10 medical categories**, including:
  - Symptoms, Medications, Diagnosis, General Health, Emergency
  - Treatment Plans, Alternative Medicine, Pediatrics, Nutrition & Diet, Mental Health
- Uses an **LLM-powered classifier** for accurate query classification.

### 3️⃣ Medical Knowledge Retrieval (FAISS DB)
- Splits parsed PDFs into smaller text chunks for **better retrieval accuracy**.
- Converts text chunks into **embeddings** using **Hugging Face sentence-transformers**.
- Stores generated embeddings in **FAISS DB** for efficient similarity searches.
- Retrieves **most relevant document chunks** based on query similarity.

### 4️⃣ Web Search Agent (DuckDuckGo API - Agent 2)
- Searches the web for **additional relevant medical information**.
- Fetches top search results from **DuckDuckGo API** to enhance query resolution.

### 5️⃣ Response Generation Agent (LLM + Context Retrieval - Agent 3)
- Combines retrieved knowledge from **FAISS DB** and **web search results**.
- Uses **OpenAI API** to generate a detailed response **based on the retrieved context**.

### 6️⃣ Emergency Escalation Agent (Agent 4)
- Identifies **critical or emergency medical cases**.
- Flags severe cases like **chest pain or breathing issues** for **immediate medical consultation**.

### 7️⃣ Query Processing & Routing (LangGraph)
- Executes a structured **workflow** for query handling:
  1. User Query → **Categorization Agent**
  2. Category Assigned → **FAISS DB Retrieval**
  3. Retrieved Context → **Web Search Agent (if needed)**
  4. Web & PDF Data → **Response Generation Agent**
  5. Response → **Final Output or Emergency Escalation**

### 8️⃣ User Interaction Agent (FastAPI + UI)
- Provides **API endpoints** using **FastAPI** for seamless user interaction.
- Builds an **interactive UI** using **HTML, CSS, and Bootstrap**.

### 9️⃣ Deployment & Scalability
- Runs **locally** with **FAISS DB** and **DuckDuckGo API**.
- Can be deployed to **AWS for cloud-based storage** and scalability.

## Installation & Setup
```bash
# Clone the repository
git clone https://github.com/your-username/multiagentic-medical-rag.git
cd multiagentic-medical-rag

# Create a virtual environment
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app:app --reload
```

## Technologies Used
- **Python, FastAPI, PyPDF, FAISS, DuckDuckGo API**
- **LangChain, OpenAI API, Hugging Face Transformers**
- **HTML, CSS, Bootstrap**
- **AWS for Deployment**

## Future Enhancements
- **Integration with electronic health records (EHR)**.
- **Improved multi-modal search using images and voice queries**.
- **Advanced AI-driven personalized recommendations**.

## Contributing
Feel free to submit issues and pull requests for improvements. 🚀

## License
This project is licensed under the **MIT License**.

---
**Author:** Gaurav Anand  

