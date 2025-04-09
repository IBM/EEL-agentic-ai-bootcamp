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

## John Doe's Portfolio Risk Assessment
| Security Name | Market Value (USD) | Sector | Risk Level | Rationale |
| --- | --- | --- | --- | --- |
| S&P 500 | 5,074.08 | Index | Medium | The S&P 500 is a diversified index with a broad range of sectors, which reduces its risk level. However, it is still subject to market volatility. |
| Tesla Inc | 1.204T | Technology | High | Tesla Inc is a volatile stock with a high beta, which increases its risk level. |
| Microsoft Corporation | 3.046T | Technology | Medium | Microsoft Corporation is a stable company with a diverse range of products, which reduces its risk level. However, it is still subject to market volatility. |
| Apple Inc | 3.419T | Technology | Medium | Apple Inc is a stable company with a diverse range of products, which reduces its risk level. However, it is still subject to market volatility. |
| Walmart Inc | 837.88B | Retail | Low | Walmart Inc is a stable company with a diverse range of products, which reduces its risk level. |
| Caterpillar Inc | 151.33B | Industrials | Medium | Caterpillar Inc is a cyclical company with a high correlation to economic growth, which increases its risk level. |
| FedEx Corporation | 58.06B | Transportation | Medium | FedEx Corporation is a cyclical company with a high correlation to economic growth, which increases its risk level. |
| General Motors | 46.46B | Automotive | Medium | General Motors is a cyclical company with a high correlation to economic growth, which increases its risk level. |
| Ford Motor Company | 37.81B | Automotive | Medium | Ford Motor Company is a cyclical company with a high correlation to economic growth, which increases its risk level. |
| Deere & Company | 129.06B | Industrials | Medium | Deere & Company is a cyclical company with a high correlation to economic growth, which increases its risk level. |
| Vanguard Total Bond ETF | 121,366M | Fixed Income | Low | Vanguard Total Bond ETF is a diversified bond fund with a low risk level. |
| SPDR Gold Shares ETF | 73.22B | Commodities | High | SPDR Gold Shares ETF is a volatile commodity with a high risk level. |
"""
        return tool_output