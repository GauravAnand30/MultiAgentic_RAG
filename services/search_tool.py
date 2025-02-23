from langchain.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

def search_web(query: str):
    return search_tool.run(query)
