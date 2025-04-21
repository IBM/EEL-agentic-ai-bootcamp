from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from tavily import TavilyClient


class WebSearchInputSchema(BaseModel):
    """Input schema for WebSearchInputSchema."""

    query: str = Field(..., description="The search query string")


class WebSearchTool(BaseTool):
    name: str = "TavilySearchTool"
    description: str = (
        "Search the web for relevant information using Tavily Search."
    )
    args_schema: Type[BaseModel] = WebSearchInputSchema

    def _run(self, query: str) -> list[str]:
        tavily_client = TavilyClient()
        response = tavily_client.search(query=query, max_results=1, include_answer=False)
        return response
