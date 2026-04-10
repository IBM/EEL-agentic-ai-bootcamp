# Lab Guide: Intelligent Marketing Agent with watsonx.data MCP Server

In this lab, you will use watsonx Orchestrate Agent Builder to create an AI-powered marketing agent that leverages IBM watsonx.data through the Model Context Protocol (MCP). The agent analyzes customer data, generates personalized product recommendations, and creates targeted email campaigns automatically.

We will focus on a retail data model with three main entities: Customers, Products, and Transactions stored in watsonx.data Iceberg tables.

## Prerequisites

Before starting this lab, make sure the following items are available:

- Make sure you've already set up the environment:
- [Lab 0 - Environment setup](../../../../labs/env-setup-lab/)
- [ADK Installation](https://developer.watson-orchestrate.ibm.com/getting_started/installing){:target="_blank"}
- [Download files](https://ibm.box.com/s/n0pkqfjzwxi3cvzaq8msaclfnf7mbwro){:target="_blank"}
- Download the **marketing_agent_with_watsonxdata_mcp.zip** file from Lab2 folder.


## Setup the Project

Make sure you have downloaded the required files for the lab and extracted them. Go to the root of the downloaded directory:
```
cd marketing_agent_with_watsonxdata_mcp/
```

You should see the following directories and files listed:
```
│
├── agents/
│   └── marketing_agent.yaml
│
├── app/
│   └── watsonxdata_mcp_http_server.py
│
├── test_data_files/
│   ├── customers.csv
│   ├── products.csv
│   └── transactions.csv
│
├── .env
├── deploy.sh
├── Dockerfile
├── example.env
└── requirements.txt
```

## Instructor Guide

**Step 1: Create Test Data Files in watsonx.data Iceberg Tables**

??? tip "INSTRUCTORS: SETUP THE RETAIL DATA IN WATSONX.DATA"

    Instructors need to set up the retail data in watsonx.data before demonstrating this feature.

    1. Login to https://cloud.ibm.com/
    2. Go to **Resources** → **Databases** and open watsonx.data, then open in web console
       - Make sure you select the Presto engine and catalog name as `iceberg_data_1`
    3. Click on **Ingest data**
    4. Select **Add data from local storage**
    5. From upload, add the CSV files downloaded from lab material in `test_data_files` and click **Next**
    6. Select catalog as `iceberg_data_1` and add schema name as `sales_data`
       - In the "Create new table" section, put the file name as the table name
    7. Click on **Preview**
    8. Click **Ingest data**
    9. Similarly, upload CSV files for transactions and products tables


**Step 2: Deploy the MCP server on Code Engine to generate a public URL for remote MCP.**

??? tip "INSTRUCTORS: DEPLOY MCP SERVER ON CODE ENGINE"

    # Podman Deployment Steps for watsonx.data MCP Server

    ## Prerequisites

    ### Install Required Tools

    **Install IBM Cloud CLI:**
    ```bash
    brew install --cask ibm-cloud-cli
    ```

    **Install Container Registry plugin:**
    ```bash
    ibmcloud plugin install container-registry
    ```

    **Install Code Engine plugin:**
    ```bash
    ibmcloud plugin install code-engine
    ```

    **Install Podman:**
    ```bash
    brew install podman
    ```


    ## Install Dependencies

    Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    ---

    ## Setup Environment Variables

    Create a `.env` file with your credentials. You can copy `example.env` from the zip folder to `.env` and update it with your credentials.

    ```bash
    # IBM Cloud API Key
    IBM_CLOUD_API_KEY=your_api_key_here
    WATSONX_DATA_API_KEY=your_api_key_here

    # watsonx.data Instance Details
    # You can get these details from watsonx.data instance
    WATSONX_DATA_INSTANCE_ID=crn:..
    WATSONX_DATA_REGION=<YOUR-REGION>
    WATSONX_DATA_URL=https://<YOUR-REGION>.lakehouse.cloud.ibm.com/lakehouse/api


    ```

    **Get resource group:**
    ```bash
    ibmcloud resource groups
    ```

    **Set the resource group in .env:**
    ```
    RESOURCE_GROUP=your-resource-group
    ```

    **Get project name:**
    ```bash
    ibmcloud ce project list
    ```

    **Set the PROJECT_NAME in .env:**
    ```
    PROJECT_NAME=your-code-engine-project
    ```

    **Get namespace:**
    ```bash
    ibmcloud cr namespace-list
    ```

    **Set the NAMESPACE in .env:**
    ```
    NAMESPACE=your-container-registry-namespace
    ```

    **Set the app name in .env:**
    ```
    APP_NAME=watsonxdata-mcp
    ```

    ---

    ## Quick Deployment Script

    All the above steps are automated in the `deploy.sh` script:

    ```bash
    ./deploy.sh
    ```

    ---

    ## Get Application URL

    Get the public URL of your deployed application:

    ```bash
    ibmcloud ce application get --name watsonxdata-mcp --output url
    ```

    **Example output:**
    ```
    https://watsonxdata-mcp.abc123.us-south.codeengine.appdomain.cloud
    ```

    ---

    ## Integration with watsonx Orchestrate

    After deployment, add the MCP server to watsonx Orchestrate. Append `/mcp` at the end:

    1. **Get MCP Server URL:**
      ```
      https://watsonxdata-mcp.abc123.us-south.codeengine.appdomain.cloud/mcp
      ```

    2. **Add to watsonx Orchestrate:**
      - Go to: watsonx Orchestrate → Tools → Add MCP Server 
      - Select: "Remote MCP server" 
      - Name: `marketing-recommendation-mcp-tool`
      - Description: `IBM watsonx.data MCP Server for querying lakehouse data, exploring catalogs, and managing data operations using natural language.`
      - Enter Server URL: `<MCP Server URL>`
      - Add the listed tools
      - Save

    3. **Verify:**
      - Test MCP tools in Orchestrate
      - Try "List Engines" or "List Schemas"

    ---

    ## Manual Approach

    Load the environment variables:

    ```bash
    export $(cat .env | grep -v '^#' | grep -v '^$' | xargs)
    ```

    ---

    ## Initialize and Start Podman

    Ensure Podman is initialized and started:

    ```bash
    podman machine init
    podman machine start
    ```

    **Note:** Execute these commands in the directory where the Dockerfile is located.

    ---

    ## Build the Container Image

    Build the image using Podman:

    ```bash
    podman build --platform linux/amd64 -t mcp-server-app .
    ```

    ## Login to IBM Cloud

    Login to IBM Cloud using SSO:

    ```bash
    ibmcloud login --sso
    ```

    A link will open in the browser - copy the one-time code and paste it in the terminal.

    **Set target region and resource group:**
    ```bash
    ibmcloud resource groups
    ibmcloud target -g ${RESOURCE_GROUP} -r ${WATSONX_DATA_REGION}
    ```

    ---

    ## Verify IBM Container Registry

    Check active service resources to verify ICR:

    ```bash
    ibmcloud resource service-instances
    ```

    Check the current region and API endpoint of ICR:

    ```bash
    ibmcloud cr info
    ```

    **Expected output:**
    ```
    Container Registry                us.icr.io
    Container Registry API endpoint   https://us.icr.io/api
    ```

    ---

    ## Create Container Registry Namespace (if needed)

    List existing namespaces:

    ```bash
    ibmcloud cr namespace-list
    ```

    If you don't have a namespace, create one:

    ```bash
    ibmcloud cr namespace-add your-namespace-name
    ```

    ---

    ## Tag the Image for IBM Container Registry

    Tag the image with the full registry path:

    ```bash
    # Tag the image
    podman tag mcp-server-app:latest $REGISTRY/$NAMESPACE/$IMAGE_NAME:latest
    ```

    **Example:**
    ```bash
    podman tag mcp-server-app:latest jp.icr.io/your-namespace/mcp-server-app:latest
    ```

    ---

    ## Login to IBM Container Registry

    Login to IBM Container Registry using Podman:

    ```bash
    ibmcloud cr login --client podman
    ```

    **Expected output:**
    ```
    Logging in to 'us.icr.io'...
    Logged in to 'us.icr.io'.
    OK
    ```

    ---

    ## Push Image to IBM Container Registry

    Push the image to ICR:

    ```bash
    podman push $REGISTRY/$NAMESPACE/$IMAGE_NAME:latest
    ```

    **Example:**
    ```bash
    podman push us.icr.io/my-namespace/mcp-server-app:latest
    ```

    **Note:** This may take several minutes depending on image size and network speed.

    ---

    ## Create or Select Code Engine Project

    List existing Code Engine projects:

    ```bash
    ibmcloud ce project list
    ```

    Select an existing project:

    ```bash
    ibmcloud ce project select --name your-project-name
    ```

    Or create a new project:

    ```bash
    ibmcloud ce project create --name your-project-name
    ```

    ---

    ## Create Registry Access Secret

    Create a secret for Code Engine to access the Container Registry:

    ```bash
    ibmcloud ce registry create \
      --name icr-secret \
      --server $REGISTRY \
      --username iamapikey \
      --password $IBM_CLOUD_API_KEY
    ```

    **Example:**
    ```bash
    ibmcloud ce registry create --name icr-secret \
      --server jp.icr.io \
      --username iamapikey \
      --password yGDcu79Qh1Xufgum1PFrNUeASJDq1RRWFYb2BATSAiBy

    ```

    **Note:** This secret allows Code Engine to pull images from your private registry.
    ---

    ## Deploy Application to Code Engine

    Deploy the application:

    ```bash
    ibmcloud ce application create \
      --name watsonxdata-mcp \
      --image $REGISTRY/$NAMESPACE/$IMAGE_NAME:latest \
      --registry-secret icr-secret \
      --port 8000 \
      --min-scale 1 \
      --max-scale 3 \
      --cpu 0.5 \
      --memory 1G \
      --env WATSONX_DATA_API_KEY="$WATSONX_DATA_API_KEY" \
      --env WATSONX_DATA_INSTANCE_ID="$WATSONX_DATA_INSTANCE_ID" \
      --env WATSONX_DATA_REGION="$WATSONX_DATA_REGION" \
      --env WATSONX_DATA_BASE_URL="$WATSONX_DATA_BASE_URL" \
      --wait
    ```

    ---

    ## Get Application URL

    Get the public URL of your deployed application:

    ```bash
    ibmcloud ce application get --name watsonxdata-mcp --output url
    ```

    **Example output:**
    ```
    https://watsonxdata-mcp.abc123.us-south.codeengine.appdomain.cloud
    ```

    ---

    ## Integration with watsonx Orchestrate

    After deployment, add the MCP server to watsonx Orchestrate. Append `/mcp` at the end:

    1. **Get MCP Server URL:**
      ```
      https://watsonxdata-mcp.abc123.us-south.codeengine.appdomain.cloud/mcp
      ```

    2. **Add to watsonx Orchestrate:**
      - Go to: watsonx Orchestrate → Tools → Add MCP Server 
      - Select: "Remote MCP server" 
      - Name: `retail-recommendation-mcp-tool`
      - Description: `IBM watsonx.data MCP Server for querying lakehouse data, exploring catalogs, and managing data operations using natural language.`
      - Enter Server URL: `<MCP Server URL>`
      - Add the listed tools
      - Save

    3. **Verify:**
      - Test MCP tools in Orchestrate
      - Try "List Engines" or "List Schemas"

  
## Reference Architecture

```text
┌─────────────────────────────────────────────────────────────────┐
│                     watsonx Orchestrate                         │
│                    (Agent Builder / Chat UI)                    │
└────────────────────────┬────────────────────────────────────────┘
                         │ MCP over SSE
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              watsonx.data MCP HTTP/SSE Server                   │
│            (watsonxdata_mcp_http_server.py on Code Engine)      │
└────────────────────────┬────────────────────────────────────────┘
                         │ watsonx.data MCP tools
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                        IBM watsonx.data                         │
│                 Catalog: iceberg_data_1                         │
│                 Schema: mynta_sales_data                        │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  customers   │  │   products   │  │ transactions │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

## Key Components

This project has been designed around the following components:


### 1. Intelligent Marketing Agent (Supervisor Agent)

An AI-powered agent running in watsonx Orchestrate capable of analyzing customer data, generating personalized product recommendations, and creating targeted email campaigns. This agent orchestrates the entire workflow from data retrieval to recommendation generation.

### 2. watsonx.data MCP Server (External Tool Provider)

A Model Context Protocol server (`watsonxdata_mcp_http_server.py`) running on IBM Cloud Code Engine that exposes watsonx.data capabilities as tools. It enables the agent to query lakehouse data, explore catalogs, and manage data operations using natural language.

### 3. Data Query Tools (MCP Tools)

A suite of tools provided by the MCP server for data access:
- **execute_select** – Execute SQL SELECT queries against watsonx.data tables
- **list_engines** – List available Presto/Spark engines
- **list_schemas** – List database schemas in catalogs
- **list_tables** – List tables within schemas
- **describe_table** – Get detailed table schema and metadata
- **get_instance_details** – Retrieve watsonx.data instance information

### 4. Retail Data Lakehouse (Knowledge Base)

IBM watsonx.data lakehouse storing retail data in Iceberg format:
- **Catalog:** `iceberg_data_1`
- **Schema:** `sales_data`
- **Tables:** 
  - `customers` – Customer profiles and demographics
  - `products` – Product catalog with ratings and pricing
  - `transactions` – Purchase history and transaction details


## Important Behavior Configured in the Agent

The agent in `marketing_agent.yaml` works in two modes:

### Mode A - Simple Query
Used for:
- Listing engines
- Showing tables
- Counting records
- Running simple analytical queries

Behavior:
- Uses MCP tools directly
- Returns results in natural language by default
- Avoids table formatting unless the user explicitly requests a table

### Mode B - Complex Recommendation Query
Used for:
- Recommendation requests
- Campaign generation
- Discount suggestions
- Personalized email generation

Behavior:
- Retrieves customer details
- Looks up purchase history
- Identifies preferred categories
- Selects recommended products
- Generates structured recommendation email output



## Import the Agent Configuration

The agent in `marketing_agent.yaml` is configured to connect to the remote MCP server in watsonx Orchestrate.

This project already includes a ready-to-import agent definition in `marketing_agent.yaml`.

Use the Orchestrate CLI to import it:

```bash
orchestrate agents import -f agents/marketing_agent.yaml
```

Expected result:

```
Importing agent from marketing_agent.yaml...
✓ Agent 'Agentic_Lakehouse_Growth_Engine' imported successfully
```

This imports:

- Agent name: `Agentic_Lakehouse_Growth_Engine`
- Style: `react`
- LLM: `groq/openai/gpt-oss-120b`
- Detailed instructions for simple analytics and recommendation generation

## Verify Imported MCP Tools

After connecting the server, verify that the agent can access relevant tools such as:

- `list_engines`
- `list_schemas`
- `list_tables`
- `describe_table`
- `execute_select`
- `get_instance_details`

Depending on your server configuration, additional tools may also be available for schema management and ingestion jobs.

## Test Simple Queries

Use the preview panel in watsonx Orchestrate and test direct data access prompts.

### Example prompts

- `List all engines in watsonx.data`
- `Show me all tables in the sales_data schema`
- `How many customers do we have?`
- `What are the top 5 products by rating?`

Expected behavior:

- The agent uses metadata or query tools
- The response is concise and conversational
- Tables are not shown unless explicitly requested

## Test Analytical Retail Queries

Now test more project-specific analytical questions.

### Example prompts

- `What are men purchasing more?`
- `Who are our top 10 customers by purchase count?`
- `Show me customers in a table`

Expected behavior:

- The agent joins `customers`, `products`, and `transactions` where needed
- It casts string fields when numerical sorting or calculations are required
- It switches to table format only when explicitly asked

## Test Personalized Recommendation Workflows

This is the primary advanced scenario for this project.

### Example prompts

- `What should we recommend to customer C001?`
- `What can I recommend to Sai Kumar?`
- `Generate email campaign for top two high value customers `

Expected behavior:

1. The agent determines this is a complex recommendation workflow.
2. If a name is provided, it looks up the customer ID automatically.
3. It retrieves:
   - customer profile
   - purchase history
   - preferred categories
   - top-rated products
4. It analyzes customer activity.
5. It proposes discount strategy.
6. It generates a structured recommendation email.


## Deploy the Agent

Once the agent behaves correctly in preview, deploy it through watsonx Orchestrate.

## Summary

You have now created and validated a project-specific retail recommendation solution that combines:

- watsonx Orchestrate for agent execution
- watsonx.data for retail lakehouse analytics
- MCP for tool-based access to enterprise data
- Code Engine for scalable server hosting

