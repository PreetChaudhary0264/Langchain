from langchain_community.tools import DuckDuckGoSearchResults

search_tool = DuckDuckGoSearchResults()
results = search_tool.invoke("India vs Australia match news today")
print(results)
