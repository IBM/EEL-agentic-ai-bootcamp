# Lab guide for AI powered customer service

In this lab, you will use watsonx Orchestrate Agent Builder to create an AI agent that supports customer service teams in an e-commerce company. The agent provides an interactive chat interface embedded in the support platform, helping users track orders, raise claims, and manage returns.

We will focus on a simple data model with two main entities Customer and Order linked by the customer ID, with optional extensions for Returns and Claims.

![schema](../../../images/cs/sql-schema.png)

## Pre-requisites

- Make sure you've already setup the environment:
- [Lab 0 - Environment setup](../../../../labs/env-setup-lab/)
- [Download files](https://ibm.box.com/s/n0pkqfjzwxi3cvzaq8msaclfnf7mbwro){:target="_blank"}
- Download the zip file from Lab1 folder

## Reference Architecture

![architecture](../../../images/cs/architecture.png)

## Key Components

This lab has been tested with **watsonx Orchestrate (SaaS)** running on **IBM Cloud**.  
Ensure the following components are available in your environment:

| Component | Description | Example |
|------------|--------------|----------|
| **watsonx Orchestrate** | Used for building and deploying the AI Agent | SaaS - IBM Cloud |
| **Agent Builder** | Interface to configure, test, and deploy the agent | Orchestrate ? Build ? Agent Builder |
| **Customer Service API** | Backend service that provides customer and order data | FastAPI / mock REST API |
| **JSON Tool Files** | OpenAPI specification files used to define tools | `customer-service.json` |
| **Web Integration (Optional)** | HTML page where the chat widget is embedded | `index.html` |
| **LLM (Foundation Model)** | For reasoning and planning during conversations | IBM Granite / Mistral / Meta Llama |
| **Storage (Optional)** | For tracking agent metrics or chat logs | Cloud Object Storage / internal DB |

---

!!! tip "Tip"

    For more advanced scenarios, you can extend your stack with:

    - **Milvus / Elasticsearch** for retrieval-based conversational search.
    - **Watsonx.ai** for fine-tuning or evaluating LLMs.

## Steps

### Agent creation

1. Open the watsonx Orchestrate UI. Click on **Create new agent** on the bottom left.
![create-wxO-agent](../../../images/create-wxo_agent.png)

2. Enter `Order and Logistics Management Agent` into the Name field (A), then enter `This agent helps staffs manage orders, deliveries, returns, and claims. It integrates with the backend Customer Service API to fetch order details, track shipments, create and monitor returns, and handle product claims.` into the Description field (B) and click Create (C).
![op-1](../../../images/cs/1.png)

The Agent Builder opens; the screen is divided into three key areas:

- **Navigation Panel (A):** move between different sections of Agent Builder.
- **Configuration (B):** set up and customize the functionality of your agent.
- **Preview (C):** preview and test your agent.
![op-2](../../../images/cs/2.png)

Below is a description of each section:

- **Profile:** Define your agents purpose, usage scenarios, and interaction style. Describe what the agent does, when it should be used (especially in multi-agent configurations), and choose its style Default or ReAct guide how it interprets requests, plans, and uses tools.

- **Knowledge:** Equip your agent with knowledge by uploading files or connecting to conversational search platforms such as Milvus, Elasticsearch, or custom-built sources. This ensures the agent can generate accurate, contextual responses by drawing on relevant content.

- **Toolset:** Provide your agent with tools to perform tasks. Tools can be added from the Catalog, imported from OpenAPI specification files or MCP servers, or built with custom flows. Tools extend the agents capabilities, enabling it to automate actions such as retrieving data or sending emails.

- **Behavior:** Define how the agent interacts with users, formats data, and handles requests. Add rules and instructions to shape its tone, response style, and overall behavior during interactions.

- **Channels:** Connect your agent to communication platforms like Slack or embed it in a website.

### Tool import

1. Click Toolset (A). Add click add tool (B)
![op-3](../../../images/cs/3.png)
2. Click Add from file or MCP server (A).
![op-4](../../../images/cs/4.png)

3. Click Import from file (A).
![op-5](../../../images/cs/5.png)

4. Upload or drag and drop the `customer-service.json` file (A), then click Next.
![op-6](../../../images/cs/6.png)

5. Select all operations for (A), then scroll down.
![op-7](../../../images/cs/7.png)

6. Go to next page (A).
![op-8](../../../images/cs/8.png)

7. Select all the remaining operations (A) and click on done (B).
![op-9](../../../images/cs/9.png)

8. The operations will be imported as tools, observe how the agent Tools have been updated.
![op-10](../../../images/cs/10.png)

9. Click the three dots in the Create Return tool, then click Edit details (A).
![op-11](../../../images/cs/11.png)

    The description from the OpenAPI specification you see has been extracted. And used as the description for the tool in Orchestrate.
    ![op-12](../../../images/cs/12.png)

    !!! note "Note"

        API descriptions may not be provided or lack a suitable explanation for how the API should be
        used. Orchestrate requires a good description as this is how the agent determines if and how a
        tool should be used. Avoid tools with similar descriptions and overlapping responsibilities to improve the performance of your agent.

10. Click Cancel (A) to close this panel.
![op-13](../../../images/cs/13.png)

### Define Instructions/Behavior to the agent

1. Click Behavior (A) and enter the following text into the Instructions field (B).
![op-14](../../../images/cs/14.png)
    ```
    Persona:
    - You are a customer service assistant tasked to help customers manage orders, deliveries, returns, and claims.

    Context:
    - You operate in a customer support environment for e-commerce or delivery systems.
    - Your primary users are support representatives.
    - You interact directly with the Customer Service API to fetch and update data.
    - Maintain conversational continuity and remember the customer?s recent orders and reference them in follow-up queries.
    - Try to reply in a markdown table.

    Reasoning:
    - Use List Customers and Customer Summary to identify top customers by total spend or repeat purchases.
    - Use List Orders to count orders by status or compute total revenue.
    - Use Get Order Details and Get Product to group revenue by product category.
    - Use List Returns and Get Return Status to find the number and completion status of returns.
    - Use Get Order Claims to count claims by claim type.
    - When needed, combine results from multiple tools using shared fields such as customerId, orderId, or productId.
    - Always provide concise answers with clear metrics and avoid assumptions not supported by data.
    ```

### Test the agent

1. In the Preview panel enter `How many orders are there in transit status? List them in a table` into the chat field (A) and press Enter(B).
![op-15](../../../images/cs/15.png)

1. Observe the list of orders in transit status retrieved by the agent. Next ask `How many orders were delivered successfully?` into the chat field (A) and press Enter(B).
![op-16](../../../images/cs/16.png)

1. Orchestrate has used the right tool to extract the full list of order delivered. Next ask `What are some of the recently returned orders that are pending for approval?`
![op-17](../../../images/cs/17.png)

1. Observe the results. Next ask `Are there any claims of lost or damaged products?`.
![op-18](../../../images/cs/18.png)

1. Click on show reasoning (A) step 1 (B) and show more (C) to see the list orders tool output. You can see the reasoning of the llm where it has selected only the orders that are in transit. (D)
![op-19](../../../images/cs/19.png)

1. Click on step 2 (A) and show more (B) to see the get order tool output. You can see the agent has invoked the tool with the order that was in transit. (C)
![op-20](../../../images/cs/20.png)

1. In the Preview panel, (A) enter `Give me the details of this order` as a follow-up question for claims.
![op-21](../../../images/cs/21.png)

1. Observe the agent kept the conversation context in memory and replied with the same product details. Next ask `Are there any other orders being delayed?` (A) and press Enter(B).
![op-22](../../../images/cs/22.png)

1. Try more question like `Can you track the status?`
![op-23](../../../images/cs/23.png)
![op-24](../../../images/cs/24.png)

!!! tip "Tip"

        You can also raise a return request by typing:

        - Customer wants to return a product
        - Please initiate a return request for order ORD1004

### Deploy the agent

1. Once the agent is functioning as expected, deploy the Agent. Click (A) to deploy agent.
![op-25](../../../images/cs/25.png)

1. It will take you to Pre-deployment summary page, verify the tools and click Deploy(A).
![op-26](../../../images/cs/26.png)

1. You should see a success message once the Agent is deployed as shown below.
![op-27](../../../images/cs/27.png)

### Web integration

1. Click on channels (A) select the **embedded agent** (B), click on **Live environment** (C) and copy the code (D).
![op-28](../../../images/cs/28.png)

1. Right-click and open the `index.html` file (A). Open it in a text editor. Scroll to lines `10-12` containing a space (A) where we can paste the embed code of the Orchestrate agent.
![op-29](../../../images/cs/29.png)

    !!! tip "Note"

        Sublime text and VSCode are both text editors and are freely available.

1. Double-click and open the `index.html` file and you should see an example webpage as shown. You will find the watsonx Orchestrate chat agent on the bottom right (A). Click on it to bring up the chat window.
![op-30](../../../images/cs/30.png)

1. The agent is now embedded into your website and can be invoked seamlessly.
![op-31](../../../images/cs/31.png)

### Interact with the deployed agent in watsonx Orchestrate

1. Back to watsonx Orchestrate, click on the hamburger menu on top left and select **Chat** (A).
![op-32](../../../images/cs/32.png)

1. From the drop down, select the Order and Logistics Management Agent that you just developed. (A)
![op-33](../../../images/cs/33.png)

1. You can chat with the agent from the watsonx Orchestrate chat UI.
![op-34](../../../images/cs/34.png)

!!! success "Conclusion"

    👏 Congratulations on completing the lab! 🎉