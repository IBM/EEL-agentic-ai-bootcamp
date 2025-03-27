# Build and Deploy a wealth management multi-agent with watsonx.ai SDKs

!!! warning "Draft version"
    
    Work in progress!

!!! info "Agentic AI Framework Details"

    - **Framework**: CrewAI
    - **Foundation Model**: meta-llama/llama-3-3-70b-instruct

## Use case

### Wealth management agent

The Wealth Manager Agent assists financial advisors in preparing for client meetings by generating detailed investment reports. It retrieves the client’s stock portfolio, analyzes performance, fetches market insights, and compiles a professional report.

Key Features:

- Portfolio Data Retrieval: Extracts stock holdings, market value, and performance metrics from the database.
- Market & News Analysis: Conducts a web search to summarize recent news and trends for each stock.
- Report Generation: Compiles all findings into a structured, downloadable PDF report.

## Steps

### Clone the GitHub repo

1. We have curated the CrewAI multi-agent as part of this lab, get started by cloning the repo:

    ```
    git clone --no-tags --depth 1 --single-branch --filter=tree:0 --sparse https://github.com/IBM/EEL-agentic-ai-bootcamp.git
    cd EEL-agentic-ai-bootcamp/
    git sparse-checkout add labs/lab2
    ```

1. This CrewAI code is developed using the quick start [template for LLM apps building using CrewAI framework](https://www.ibm.com/watsonx/developer/agents/quickstart).

!!! info "Reference Material"
    You can learn more about the different starter kits made available by watsonx developer hub here: <https://www.ibm.com/watsonx/developer/agents/quickstart>