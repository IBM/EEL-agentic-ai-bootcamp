# Build and Deploy a risk assessment agent with watsonx.ai SDKs

!!! warning "Draft version"
    
    Work in progress!

!!! info "Agentic AI Framework Details"

    - **Framework**: CrewAI
    - **Foundation Model**: meta-llama/llama-3-3-70b-instruct

## Use case

### Wealth management agent - Risk assessment agent

The Portfolio Risk Assessment Agent supports financial advisors by evaluating investment portfolios for potential risk exposures. It reviews each asset in the portfolio based on factors like market value concentration, sector distribution, volatility, and overall diversification, delivering a detailed and actionable risk profile.

Key Features:

- Risk Evaluation per Asset: Assesses each security in the portfolio and assigns a Risk Level (High, Medium, Low) based on exposure and volatility.
- Diversification & Sector Analysis: Identifies sector overconcentration and diversification gaps that may impact portfolio stability.
- Markdown Risk Report: Generates a clean, structured Markdown table summarizing each asset’s name, value, sector, risk level, and rationale for easy review and reporting.

## Steps

### Clone the GitHub repo

1. We have curated the CrewAI multi-agent as part of this lab, get started by cloning the repo:

    ```
    git clone --no-tags --depth 1 --single-branch --filter=tree:0 --sparse https://github.com/IBM/EEL-agentic-ai-bootcamp.git
    cd EEL-agentic-ai-bootcamp/
    git sparse-checkout add labs/lab2/risk-assessment-agent
    ```

1. This CrewAI code is developed using the quick start [template for LLM apps building using CrewAI framework](https://www.ibm.com/watsonx/developer/agents/quickstart).

!!! info "Reference Material"
    You can learn more about the different starter kits made available by watsonx developer hub here: <https://www.ibm.com/watsonx/developer/agents/quickstart>

1. Once you have cloned the repo goto the `risk-assessment-agent` directory:

    ```
    cd labs/lab2/risk-assessment-agent
    ```

### Install the dependencies

1. Create a virtual environment. `uv` package manager is recommended.

    ```
    uv venv
    source .venv/bin/activate
    ```

1. Install the python dependencies.

    ```
    uv sync
    ```

### Configure environment variables

1. In `config.toml` enter the following details:

    ```
    watsonx_apikey = " " # watsonx api key
    space_id = " " # space id
    project_id = " " # project id
    tavily_api_key = " " # tavily api key
    ```

    !!! success "Credentials"
        
        `watsonx_apikey`, `space_id` and `project_id` has been generated in Lab 1. Please use the same credentials. 
        `tavily_api_key` you can create a free Tavily API key on https://tavily.com/ or ask the instructor to provide the API key.

### Run the agent locally

1. Run the following command to test the agent locally.

    ```
    python examples/execute_ai_service_locally.py
    ```

1. Enter the input as follows:

    ```
    Here is John Doe's portfolio: S&P 500, Tesla Inc, Microsoft Corporation, Apple Inc, Walmart Inc, Caterpillar Inc, FedEx Corporation, General Motors, Ford Motor Company, Deere & Company, Vanguard Total Bond ETF, SPDR Gold Shares ETF
    ```
    
1. You wil see the Agent's reply.

### Deploy the agent to watsonx.ai

1. Now the agent is tested locally, you can deplop the agent on watsonx.ai runtime.

    ```
    python scripts/deploy.py
    ```