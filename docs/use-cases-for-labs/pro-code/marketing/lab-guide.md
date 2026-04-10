# Lab Guide: Intelligent Marketing Agent with watsonx.data MCP Server

In this lab, you will use watsonx Orchestrate Agent Builder to create an AI-powered marketing agent that leverages IBM watsonx.data through the Model Context Protocol (MCP). The agent analyzes customer data, generates personalized product recommendations, and creates targeted email campaigns automatically.

We will focus on a retail data model with three main entities: Customers, Products, and Transactions stored in watsonx.data Iceberg tables.

## Pre-requisites

Before starting this lab, make sure the following items are available:


- Make sure you've already setup the environment:
- [Lab 0 - Environment setup](../../../../labs/env-setup-lab/)
- [ADK Installation](https://developer.watson-orchestrate.ibm.com/getting_started/installing){:target="_blank"}
- [Download files](https://ibm.box.com/s/n0pkqfjzwxi3cvzaq8msaclfnf7mbwro){:target="_blank"}
- Download the **marketing_agent_with_watsonxdata_mcp.zip** file from Lab2 folder.


## setup the project

Make sure you have downloaded the required files for the lab and extracted it. Go to the root of the downloaded directory.
```
cd marketing_agent_with_watsonxdata_mcp/
```

You should see the following directories & files listed:
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

**Step 1: Create a Test data files in watsonx.data Iceberg tables**

1. Login https://cloud.ibm.com/
2. go to resources --> databases and open watsonx.data and open in web console
   Make sure you select the presto engine and catelog name as 'iceberg_data_1'
3. click on ingest data
4. select  Add data from local storage
5. from upload open add the csv files downloaded from lab material in 'test_data_files' and click on next
6. select catelog as iceberg_data_1 and add schema name as 'sales_data'
   In create new tabel section put file name as tabel name
7. click on preview
8. Ingest data
9. similarly you should  upload csv files for transactions and products tabel also.

**Step 2: Deploy the MCP server on Code Engine to generate a public URL for remote MCP.**

Use deployment-guide.md for the instructor guide to generate a public URL for remote MCP.

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


 1. Intelligent Marketing Agent (Supervisor Agent)
An AI-powered agent running in watsonx Orchestrate capable of analyzing customer data, generating personalized product recommendations, and creating targeted email campaigns. This agent orchestrates the entire workflow from data retrieval to recommendation generation.

 2. watsonx.data MCP Server (External Tool Provider)
A Model Context Protocol server (`watsonxdata_mcp_http_server.py`) running on IBM Cloud Code Engine that exposes watsonx.data capabilities as tools. It enables the agent to query lakehouse data, explore catalogs, and manage data operations using natural language.

 3. Data Query Tools (MCP Tools)
A suite of tools provided by the MCP server for data access:
- **execute_select** – Execute SQL SELECT queries against watsonx.data tables
- **list_engines** – List available Presto/Spark engines
- **list_schemas** – List database schemas in catalogs
- **list_tables** – List tables within schemas
- **describe_table** – Get detailed table schema and metadata
- **get_instance_details** – Retrieve watsonx.data instance information

4. Retail Data Lakehouse (Knowledge Base)
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



## Steps for Project Agent Configuration

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

## Step 6: Verify Imported MCP Tools

After connecting the server, verify that the agent can access relevant tools such as:

- `list_engines`
- `list_schemas`
- `list_tables`
- `describe_table`
- `execute_select`
- `get_instance_details`

Depending on your server configuration, additional tools may also be available for schema management and ingestion jobs.

## Step 8: Test Simple Queries

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

## Step 9: Test Analytical Retail Queries

Now test more project-specific analytical questions.

### Example prompts

- `What are men purchasing more?`
- `Who are our top 10 customers by purchase count?`
- `Show me customers in a table`

Expected behavior:

- The agent joins `customers`, `products`, and `transactions` where needed
- It casts string fields when numerical sorting or calculations are required
- It switches to table format only when explicitly asked

## Step 10: Test Personalized Recommendation Workflows

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


## Step 12: Deploy the Agent

Once the agent behaves correctly in preview, deploy it through watsonx Orchestrate.

## Summary

You have now created and validated a project-specific retail recommendation solution that combines:

- watsonx Orchestrate for agent execution
- watsonx.data for retail lakehouse analytics
- MCP for tool-based access to enterprise data
- Code Engine for scalable server hosting

