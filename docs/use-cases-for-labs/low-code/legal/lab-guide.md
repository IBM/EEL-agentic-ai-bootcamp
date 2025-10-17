# Lab guide for document processing workflow

## Overview

This lab focuses on a practical use case involving document classification, followed by key data extraction from both unstructured documents (primarily contracts) and structured ones (such as invoices). At the outset, the guide outlines the sequence of activities required to support the user journey of extracting essential information from uploaded documents.

In this lab scenario, a financial services firm processes numerous contracts and invoices weekly, extracting critical information like payment terms, amounts, and due dates. Currently, this is done manually, consuming significant employee time and increasing the risk of errors. With growing document volumes, the firm faces scalability challenges and inefficiencies in their processes.

## Pre-requisites

- Make sure you've already setup the environment:
- [Lab 0 - Environment setup](../../../../labs/env-setup-lab/)
- [ADK Installation](https://developer.watson-orchestrate.ibm.com/getting_started/installing){:target="_blank"}
- [Download files](https://ibm.box.com/s/n0pkqfjzwxi3cvzaq8msaclfnf7mbwro){:target="_blank"}
- Download the **document-extraction-lab.zip** file from Lab1 folder.

## Reference Architecture

![image](../../../images/legal/architecture.png)

## Key Components

**Agents**

- Document Processing Agent (Main Agent): Manages end-to-end document ingestion, classification, extraction, and display.

**Workflow**

- Document Classifier: Distinguishes between document types (Invoice vs. Contract).
- Document Extractor (Contract Extractor): Extracts fields such as Buyer, Supplier, and Effective Date from contract documents.
- Document Extractor (Invoice Extractor): Extracts Invoice Number, Terms, Description, and Bill To address from invoice documents.
- Branch Node: Routes the workflow to the appropriate extractor based on document type.
- Display to User Activity: Displays extracted fields in a readable message format for end users.
- End Node: Returns the final classification result (Contract or Invoice) as output.

## Steps

### Create an Agent

1. Open the watsonx Orchestrate UI. Click on **Create new agent** on the bottom left.
![create-wxO-agent](../../../images/create-wxo_agent.png)

2. Enter `Document processing agent` into the Name field (A), then enter `This agent is able to classify documents and extract core fields to retrieve` into the Description field (B) and click Create (C).
![op-1](../../../images/legal/2.png)

The Agent Builder opens; the screen is divided into three key areas:

- **Navigation Panel (A):** move between different sections of Agent Builder.
- **Configuration (B):** set up and customize the functionality of your agent.
- **Preview (C):** preview and test your agent.
![op-2](../../../images/legal/3.png)

Below is a description of each section:

- **Profile:** Define your agents purpose, usage scenarios, and interaction style. Describe what the agent does, when it should be used (especially in multi-agent configurations), and choose its style Default or ReAct guide how it interprets requests, plans, and uses tools.

- **Knowledge:** Equip your agent with knowledge by uploading files or connecting to conversational search platforms such as Milvus, Elasticsearch, or custom-built sources. This ensures the agent can generate accurate, contextual responses by drawing on relevant content.

- **Toolset:** Provide your agent with tools to perform tasks. Tools can be added from the Catalog, imported from OpenAPI specification files or MCP servers, or built with custom flows. Tools extend the agents capabilities, enabling it to automate actions such as retrieving data or sending emails.

- **Behavior:** Define how the agent interacts with users, formats data, and handles requests. Add rules and instructions to shape its tone, response style, and overall behavior during interactions.

- **Channels:** Connect your agent to communication platforms like Slack or embed it in a website.

### Create an agentic workflow

1. Click Toolset (A). Add click add tool (B).
![op-3](../../../images/legal/4.png)

1. Click on Create an agentic workflow (A).
![op-4](../../../images/legal/5.png)

1. Click the pencil icon (A) to rename the workflow.
![op-6](../../../images/legal/6.png)

1. Type `Document processing` in the Name (A). Type `This flow classifies and extracts values from documents.` In the Description (B). Scroll down to the Output section (C).
![op-7](../../../images/legal/7.png)

### Define the process output

Scrolling down, you’ll find the Input and Output sections, which apply to the entire flow. In this case, no inputs are required since they are already handled within the flow itself through the user activity file upload. For the output, instead of using a text output node, the flow can return the classification result, defined as a string.

1. Click Add output (A). and select String (B).
![op-8](../../../images/legal/8.png)

1. Type “Class_name” in the Name field (A). Click Add (B). Then click Save (C).
![op-9](../../../images/legal/9.png)

### Design the workflow diagram

In this section, you will add the different workflow activities including the document classifier and the 2 extractors.

1. Move the cursor over the link until the + icon appears. Click the + to add an activity (A). The first activity of the process consists in uploading the document to process. It will be implemented as a user activity.
![op-10](../../../images/legal/10.png)

1. Select Create new (A) and then select User activity (B).
![op-11](../../../images/legal/11.png)
    
    !!! note "Note"

        A green box appears, indicating the user activity. This will contain the series of activities that the user must perform whilst interacting with the agent.

1. Move the cursor on the user activity link and click + (A) to add the activities the user will have to perform.
![op-12](../../../images/legal/12.png)

1. Select the Interactions tab (A) then click File upload (B).
![op-13](../../../images/legal/13.png)

The first activity of the process is now defined. The next step is to classify the document the user will have provided. To do this, you will add a watsonx Orchestrate Document Classifier.
![op-14](../../../images/legal/14.png)

### Add a document classifier

In this section, you will add a document classifier to identify Invoice documents from the Contract ones.

1. Move the cursor over the last link of the process and click + (A). Select Create new (B) then click Document classifier (C).
![op-15](../../../images/legal/15.png)

1. Click the Document classifier node (A).
![op-16](../../../images/legal/16.png)

1. Click the edit icon (A).
![op-17](../../../images/legal/17.png)

1. Click Add class (A).
![op-18](../../../images/legal/18.png)

1. Type `Contract` (A).
![op-19](../../../images/legal/19.png)

1. Click Add class again and then type ‘Invoice’ (A).
![op-20](../../../images/legal/20.png)

    You are now ready to test your document classifier.

1. Click Test classifier (A).
![op-21](../../../images/legal/21.png)

1. Drag and drop the two sample files, `Invoice.pdf` and `Contract.pdf` from your local machine location (A).
![op-22](../../../images/legal/22.png)

1. Wait for the documents to be analyzed and classified (A).
![op-23](../../../images/legal/23.png)

    !!! note "Note"

        The two documents have been successfully classified as a Contract class for contract.pdf and an Invoice class for the Invoice.pdf one.

1. Click Done (A).
![op-24](../../../images/legal/24.png)

    The next step is to route the process on the right extractor path depending on the document type. To do this, you will add a branch node responsible for the triage.

### Add a Branch node

1. Move the cursor over the last link of the diagram then click + (A).
![op-25](../../../images/legal/25.png)

1. Click Branch (A).
![op-26](../../../images/legal/26.png)

1. Click the Branch 1 node (A).
![op-27](../../../images/legal/27.png)

    !!! note "Note"

        When creating a branch from scratch, two paths are generated by default, but additional paths can be added as needed.

1. Move the cursor over the Branch 1 name then click the edit icon (A)
![op-28](../../../images/legal/28.png)

1. Type `Document type` in the node name field (A) then hit Enter.
![op-29](../../../images/legal/29.png)

1. Click the Path 1 row (A).
![op-30](../../../images/legal/30.png)

1. Type `Invoice` (A).
![op-31](../../../images/legal/31.png)

1. Click Edit condition (A) to edit the condition and select invoice documents.
![op-32](../../../images/legal/32.png)

1. Click the + icon (A) to add conditions.
![op-33](../../../images/legal/33.png)

    You will use the result of the Document classifier step as the variable to evaluate for the routing.

1. Click Document classifier (A) and then click class_name (B).
![op-34](../../../images/legal/34.png)

1. Select the ‘==’ operator (A).
![op-35](../../../images/legal/35.png)

1. Click + to specify the value to check (A).
![op-36](../../../images/legal/36.png)

1. Type ‘Invoice’ (A) then hit Enter.
![op-37](../../../images/legal/37.png)

    The process will be routed in this branch if the document type is Invoice.

    !!! note "Note"

        Conditions can also be edited with the expression editor (</> icon). The equivalent expression to enter using the expression editor will then be: flow["Document classifier"].output.class_name == "Contract"

1. Click the Back icon (A).
![op-38](../../../images/legal/38.png)

    Let’s just rename the second path Contract. As you will just have 2 types of documents, any document that is not an invoice (i.e. contracts) will be routed to this branch.

1. Click the Path 2 row (A).
![op-39](../../../images/legal/39.png)

1. Type Contract (A) then hit Return.
![op-40](../../../images/legal/40.png)

    You are now ready to add the 2 document extractors, one for each document type.

### Add a document extractor

In this section, you will create two document extractors. Each document extractor will be responsible for extracting specific data from each document class:

Invoice:

- Invoice #
- Terms
- Description

Contract:

- Buyer
- Supplier
- Effective date

&nbsp;

1. Click Add + (A).
![op-41](../../../images/legal/41.png)

1. Select Create new (A) then click Document extractor (B).
![op-42](../../../images/legal/42.png)

1. Click the Document extractor node (A) then click the edit icon (B).
![op-43](../../../images/legal/43.png)

1. Click the Document extractor name (A) to edit it.
![op-44](../../../images/legal/44.png)

1. Type ‘Contract extractor’ (A) as a new name then click the save icon (B).
![op-45](../../../images/legal/45.png)

1. Drag and drop the Contract.pdf file (A) from your computer to the dropping area.
![op-46](../../../images/legal/46.png)

1. Wait for the document to be processed.
![op-47](../../../images/legal/47.png)

1. Once uploaded, the sample document is displayed, and the page is divided into the following key segments:
    1. **Activity Name** – Displays the name of the document extractor activity. Rename it to reflect the sample document you've uploaded.
    1. **LLM Model Selection** – Choose your preferred LLM model from the drop-down menu. You can switch models at any time while prompting them for document extraction.
    1. **Field Definitions** – Define the list of fields you want to extract from the sample document. The selected LLM will retrieve the corresponding values.
    1. **Document Navigation & Upload** – Use the drop-down to navigate between uploaded documents. You can upload up to five additional documents for prompting and testing.
    1. **Document Viewer:** Shows the uploaded document with the specified fields for extraction highlighted.
![op-48](../../../images/legal/48.png)

1. Click the model expand icon (A).
![op-49](../../../images/legal/49.png)

    !!! tip "Tip"

        You can change the LLM model by clicking on the ‘Model’ drop-down. Here you’ll see all the available models that you can select. You can identify the current model that is being used, as you’ll see a tick icon. You can change the model at any time while you test to see which one is most accurate at extracting fields. For now keep the meta-lama model.

    Let’s now define the fields to extract.

1. Click Add field (A).
![op-50](../../../images/legal/50.png)

1. Type `Buyer` (A) and hit Return.
![op-51](../../../images/legal/51.png)

    !!! note "Note"

        The LLM will retrieve a value associated with the key you define here, which will auto-highlight in the document preview.

1. In the same way, add the 2 following fields:

    - Supplier
    - Effective date

    Your screen should look like:
![op-52](../../../images/legal/52.png)

1. Click x (A) to close the extractor.
![op-53](../../../images/legal/53.png)

1. Click in the background to close the Contract extractor property view (A).
![op-54](../../../images/legal/54.png)

    Next, you will create the Invoice extractor in the corresponding branch of the process.

1. Move the mouse over the invoice branch and click + (A)
![op-55](../../../images/legal/55.png)

1. Select Document extractor (A).
![op-56](../../../images/legal/56.png)

1. Click the Document extractor node a move it for a nicer layout (A).
![op-57](../../../images/legal/57.png)

1. Repeat the from step 3 to:

    - Rename the extractor ‘Invoice Extractor’.
    - Add the `Invoice.pdf` document to the extractor.

    You should have the following screen:
![op-58](../../../images/legal/58.png)

    Let’s now add the fields to extract.

1. Click Add field (A).
![op-59](../../../images/legal/59.png)

1. Type Invoice (A) and hit Return.
![op-60](../../../images/legal/60.png)

1. The invoice number should have been recognized (A):
![op-61](../../../images/legal/61.png)

1. Repeat from Step 20 to add the following fields:

    - Terms
    - Description
    ![op-62](../../../images/legal/62.png)

1. You will now add the Bill to field. Click Add + (A)
![op-63](../../../images/legal/63.png)

1. Type ‘Bill to’ (A) end press Enter.
![op-64](../../../images/legal/64.png)

1. Observe the result (A).
![op-65](../../../images/legal/65.png)

    The entire billing address was not correctly highlighted. Let’s train the model to recognize the address field.

1. Hover your mouse over the ‘Bill to’ field and click on the edit icon (A).
![op-66](../../../images/legal/66.png)

1. The left pane appears (A) so you can re-prompt your model to more accurately extract the value for the selected field. Let’s Add example showing where and how to extract the Bill to information.
![op-67](../../../images/legal/67.png)

1. Click Add example (A).
![op-68](../../../images/legal/68.png)

    The ‘Input’ and ‘Output’ sections will appear, allowing you to specify the exact key-value pair you want to extract from the sample document. This helps to re-prompt the model to accurately capture the full value for the selected field.

1. Click inside the ‘Input’ field (A) to enable ‘Select to Copy’ mode, then draw a box around the entire key-value pair (B) on the document to define what should be extracted.
![op-69](../../../images/legal/69.png)

    As soon as you release the mouse button the entire text is captured in the Input Field. The model now knows where to find the information. But the ‘Bill to’ text is not required. You will now teach the model what the output should be for this precise example.

1. Click inside the ‘Output’ field to enable ‘Select to Copy’ mode (A) then draw a box around the address section (B) on the document to define what should be extracted (excluding ‘Bill to’).
![op-70](../../../images/legal/70.png)

1. Once highlighted, release the mouse button and this will auto-populate the Output section (A).
![op-71](../../../images/legal/71.png)

1. Click the Show on Document button (A) to let the LLM retry the extraction.
![op-72](../../../images/legal/72.png)

    !!! note "Note"

        The LLM will use the re-prompt the key-value pair and highlight the updated value in the document preview.

1. The ‘Bill To’ address is re-highlighted (A) after prompting the model, indicating that the LLM has been successfully trained to extract this information. Click on the ‘back’ icon (B) to return to the original page.
![op-73](../../../images/legal/73.png)

    !!! warning "Note"

        The model can only be prompted using unstructured data. Re-prompting on structured formats, like tables, is not currently supported. Please check with your instructors who can guide you with the [ProductRoadmap](https://w3.ibm.com/w3publisher/orchestrate/roadmap) for more details.

1. All the fields that you’ve defined are highlighted on the sample document. Once complete, click X to close the window (A).
![op-74](../../../images/legal/74.png)

1. Click on the diagram background to close the Invoice extractor property view (A).
![op-75](../../../images/legal/75.png)

    You will now add the user display activities for each branch.

### Add a Display to user activity

To complete the flow, we need to add a final activity that presents the extracted values to the user. This step allows us to format and display the results clearly, based on the core fields that we defined when we prompted the model for each document type.

1. Hover the last link in the Contract extractor branch and click + (A).
![op-76](../../../images/legal/76.png)

1. Select Create new (A) then click User activity (B).
![op-77](../../../images/legal/77.png)

1. Click + (A) to add a new action in the user activity node.
![op-78](../../../images/legal/78.png)

1. Click Display to user (A).
![op-79](../../../images/legal/79.png)

1. Select Message (A).
![op-80](../../../images/legal/80.png)

1. Click the Message box to edit its content (A).
![op-81](../../../images/legal/81.png)

1. Hover the Message 1 name (A) then click the edit button (B) to rename it.
![op-82](../../../images/legal/82.png)

1. Type `Extracted contract fields` (A) and hit Return.
![op-83](../../../images/legal/83.png)

1. Type the following to create a table output:

    ```
    Buyer|Supplier|Effective date
    --|--|--
    {flow["Contract extractor"].output.buyer}|{flow["Contract extractor"].output.supplier}|{flow["Contract extractor"].output.effective_date}
    ```

    To display the results for the field, you must assign a variable to it. Click on the Select variable ‘[x]’ button and assign the variables.

1. Your screen should look like (A):
![op-87](../../../images/legal/110.png)

1. Click the background to remove the property view (A).
![op-89](../../../images/legal/89.png)

1. Repeating from Step 1, create a user activity in the Invoice branch (A) to display the following fields:

    - Invoice #
    - Terms
    - Description
    - Bill to
    ![op-90](../../../images/legal/90.png)

    !!! note "Note"

        The invoice variables will be under the Invoice extractor folder.

1. You should get the following result:
![op-91](../../../images/legal/111.png)

### Define the end flow

Now that the output message has been defined for both file types, we can now conclude the flow by updating the end node. The end node will just return the Document type (i.e. Contract/Invoice).

1. Click the End node (A).
![op-92](../../../images/legal/92.png)

1. Click Edit data mapping (A).
![op-93](../../../images/legal/93.png)

    Note that the output, ‘class_name’ is auto-mapped by the LLM (A). This means that the LLM will attempt to automatically link the input/outputs.
    ![op-94](../../../images/legal/94.png)

    !!! tip "Note"

        The auto-map feature works effectively for those flows that are less complex. But for the more complex flows, (for instance if you had two ‘class_name’ outputs) then explicit mapping performs best. 

1. Hover the variable row and click on the Variable icon (A).
![op-95](../../../images/legal/95.png)

1. Click the Document classifier (A).
![op-96](../../../images/legal/96.png)

1. Select class_name (A).
![op-97](../../../images/legal/97.png)

1. The output ‘class_name’ is now assigned to the ‘class_name’ variable (A). Click x (B) to close the window.
![op-98](../../../images/legal/98.png)

1. Click Done (A).
![op-99](../../../images/legal/99.png)

### Add a behavior

To trigger the tool you just created, you must update the agent behavior.

1. Click Behavior (A) and type `Invoke the Document extractor tool and output the result` (B) in the Instructions.
![op-100](../../../images/legal/102.png)

    Your agent is ready to be tested.

### Test your agent

In this section, you will use the Agent preview to test your agent behavior.

1. Type `Invoke document extractor` (A) in the Preview instructions area.
![op-103](../../../images/legal/103.png)

1. Click Add file (A).
![op-104](../../../images/legal/104.png)

1. Upload the `Contract.pdf` file and hit send.
![op-105](../../../images/legal/105.png)

    After uploading your document, the agent will automatically execute the predefined workflow steps in the background. It will extract relevant data, focusing on the fields it has been prompted on, and generate a response with the extracted information. Additionally, it will provide insights into the document classification.

1. After a few seconds the agent will reply with the extracted data and the document type (A).
![op-106](../../../images/legal/106.png)

!!! success "Conclusion"

    👏 Congratulations on completing the lab! 🎉