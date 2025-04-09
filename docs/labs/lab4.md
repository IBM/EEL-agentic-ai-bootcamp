# Lab 4: Register your deployed agents into watsonx Orchestrate 
---
## Step 1: Create the Code Engine Endpoints

### 1A: Create the Endpoint

1. **Using IBM Cloud Web UI:**
   - Navigate to [IBM Cloud Code Engine Projects](https://cloud.ibm.com/containers/serverless/projects) and select the project that has been created for you.
   - Click 'Applications'
   - Click 'Create'

2. **Creating your Application:**
   - Change the name to `${your agent name}-agent`
   - Use an existing container image
   - Click 'Configure image'
   - Click 'Registry server'
   - Type in `quay.io` (you must select it from the dropdown list after typing it)
   - Leave 'Registry secret' as None
   - Change 'Namespace' to `mattmule`
   - Change 'Repository name' to `agent-builder-v2`
   - Click Done
   - Change 'Autoscaling - instance scaling range'/'Min number of instances to 1' (This avoids timeout errors if your Application scales down to 0 instances)
   - Go to 'Optional settings'/'Environment variables', click 'Add'
      - Add the following environment variables:
         - `WATSONX_DEPLOYMENT_ID`
         - `WATSONX_API_KEY`
         - `WATSONX_SPACE_ID`
         - `WATSONX_URL` (optional)
   - Click 'Create'

3. **Test the Application:**
   - Choose **Test application** and click **Application URL**.
   - Append `/docs` to the end of the URL path to view a formatted API page.
     - Example: `https://wxo-agent-test1-app1.1pj4w3r1pi47.us-south.codeengine.appdomain.cloud/docs`
   - Click 'Post /chat/completions'
   - Click 'Try it out'
   - Use this json as a test: ```{
  "model": "string",
  "context": {},
  "messages": [
    {
      "role": "user",
      "content": "your prompt input for agent"
    }
  ],
  "stream": true,
  "extra_body": {
    "thread_id": "string"
  }
} ```
   - click Execute
   - Verify you get a stream of outputs under Response body
   - Copy the full curl request enpoint
      - Example: `https://mdm-agent-builder.1sfrdnqsrnj5.us-south.codeengine.appdomain.cloud/chat/completions`


## Step 2: Register the New Endpoint as an External Agent

### 2A: Create an agent in watsonx Orchestrate


1. **In IBM watsonx orchestrate Web UI:**
   - Go to https://cloud.ibm.com/resources and click "AI / Machine Learning"
   - Click AI / Machine Learning, the click the blue box: "Launch watsonx Orchestrate"
   - From the top left hamburger menu, select **Agent Configuration**.
   - Select **Agents** from the left-hand navigation.
   - Click the **Add agent** button on the top right.

3. **Enter Details (Agent Details):**
   - **Display Name:** e.g., `Risk Assessment Agent`
   - **Description:** Enter a description of capabilities,
      ```
         About the agent features and capabilities
      ```
   - **API Key:** Enter `WATSONX_API_KEY or IBM IAM KEY`
   - **Service Instance URL:** Use the Test URL with `/chat/completions` appended.
     - Example: `https://wxo-agent-test1-app1.1pj4w3r1pi47.us-south.codeengine.appdomain.cloud/chat/completions`

### Step 3: Call the new External Agent from Orchestrate

1. **In IBM watsonx orchestrate Web UI:**
   - From the top left hamburger menu, select **Agent Configuration**.
   - Select **Chat** from the left-hand navigation.
   - Type a question that should route to the new agent, like `What is the weather like in Maui?`
   - The results from the external agent should be streamed to the IBM watsonx Orchestrate chat window
   - Type a question that should route to the new agent, like `What cards could I use on a trip there?`
   - The results from the external agent should be streamed to the IBM watsonx Orchestrate chat window
     
- Replace image information with the newly created information
- Check out https://github.ibm.com/Matthew-Mueller/wxo-external-agent-template/tree/main for an example (crewai)
