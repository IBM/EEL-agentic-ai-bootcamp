from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class InputSchema(BaseModel):
    """Input schema for PortfolioFetcherInputSchema."""

    username: str = Field(..., description="The name of the user")


class PortfolioFetcherTool(BaseTool):
    name: str = "PortfolioFetcher"
    description: str = (
        "Fetches user's portfolio from the database. "
    )
    args_schema: Type[BaseModel] = InputSchema

    def _run(self, username: str) -> list[str]:
        
        tool_output = """#John Doe's Portfolio

# Portfolio Table
|   ID | Security Name           |   Market Value (USD) |   Y2Y % | Industry Sector         |
|-----:|:------------------------|---------------------:|--------:|:------------------------|
|    1 | S&P 500                 |              5000000 |      15 | Index Fund              |
|    2 | Tesla, Inc.             |              1500000 |      20 | Consumer Discretionary  |
|    3 | Microsoft Corporation   |              2000000 |      18 | Information Technology  |
|    4 | Apple Inc. (AAPL)       |              1800000 |      17 | Consumer Electronics    |
|    5 | Walmart Inc. (WMT)      |              1200000 |      10 | Consumer Staples        |
|    6 | Caterpillar Inc. (CAT)  |              1200000 |      12 | Industrials             |
|    7 | FedEx Corporation (FDX) |              1100000 |      11 | Logistics               |
|    8 | General Motors (GM)     |              1000000 |      14 | Automotive              |
|    9 | Ford Motor Company (F)  |               900000 |      12 | Automotive              |
|   10 | Deere & Company (DE)    |              1000000 |       9 | Agriculture & Equipment |
|   11 | Vanguard Total Bond ETF |              2000000 |       4 | Fixed Income            |
|   12 | SPDR Gold Shares ETF    |              1500000 |       6 | Commodities             |

"""
        return tool_output