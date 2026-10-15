from langchain_community.tools.tavily_search import TavilySearchResults

def get_web_search_tool():
    """Returns a Tavily search tool for general knowledge queries."""
    return TavilySearchResults(max_results=5)