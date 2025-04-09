# Lab 4: Register your deployed agents into watsonx Orchestrate 
---
## Step 1: Create the Code Engine Endpoints

### 1A: Create the Endpoint

1. **Using IBM Cloud Web UI:**
   - Navigate to [IBM Cloud Code Engine Projects](https://cloud.ibm.com/containers/serverless/projects) and select the project that has been created for you.
   - Click 'Applications'
   - Click 'Create'

2. **Creating your Travel Concierge Application:**
   - Change the name to `${your initials}-travel-concierge`
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
      "content": "what is the weather like in Maui?"
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

### 1B: Create the Loyalty Specialist Endpoint

1. **Using IBM Cloud Web UI:**
   - Navigate to [IBM Cloud Code Engine Projects](https://cloud.ibm.com/containers/serverless/projects) and select the project that has been created for you.
   - Click 'Applications'
   - Click 'Create'

2. **Creating your Loyalty Specialist Application:**
   - Change the name to `${your initials}-loyalty-specialist`
   - Use an existing container image
   - Click 'Configure image'
   - Click 'Registry server'
   - Type in `quay.io` (you must select it from the dropdown list after typing it)
   - Leave 'Registry secret' as None
   - Change 'Namespace' to `mattmule`
   - Change 'Repository name' to `crewai`
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
   - Change 'role' to `user`
   - Change 'content' to `How can I optimize my card points?`
   - Change 'stream' to `true` (to duplicate how WxO calls the endpoint)
   - Verify you get a stream of outputs
   - Copy the full curl request enpoint
      - Example: `https://mdm-agent-builder.1sfrdnqsrnj5.us-south.codeengine.appdomain.cloud/chat/completions`

## Step 2: Register the New Endpoint as an External Agent

### 2A: Create the Travel Concierge Endpoint


1. **In IBM watsonx orchestrate Web UI:**
   - Go to https://cloud.ibm.com/resources and click "AI / Machine Learning"
   - Click AI / Machine Learning, the click the blue box: "Launch watsonx Orchestrate"
   - From the top left hamburger menu, select **Agent Configuration**.
   - Select **Agents** from the left-hand navigation.
   - Click the **Add agent** button on the top right.

3. **Enter Details (Travel Concierge):**
   - **Display Name:** e.g., `Travel Concierge`
   - **Description:** Enter a description of capabilities,
      ```
         Travel Concierge is a vacation planning assistant that helps users plan their vacations.
         When the user asks for a detailed vacation plan, this assistant provides up-to-date information about activities, dining options, and travel logistics to suggest a detailed day-by-day vacation plan.
         When the user asks about the weather of a travel destination, this assistant provides up-to-date weather forecasts for the travel destination to help users plan accordingly.
         Example Questions: "Give me a detailed 5-day vacation plan to Los Angeles, CA with a budget limit of $6000.", "How is the weather in Washington DC from March 15 to March 20?"
      ```
   - **API Key:** Enter `123`
   - **Service Instance URL:** Use the Test URL with `/chat/completions` appended.
     - Example: `https://wxo-agent-test1-app1.1pj4w3r1pi47.us-south.codeengine.appdomain.cloud/chat/completions`

### 2B: Create the Loyalty Specialist Endpoint


1. **In IBM watsonx orchestrate Web UI:**
   - From the top left hamburger menu, select **Agent Configuration**.
   - Select **Agents** from the left-hand navigation.
   - Click the **Add agent** button on the top right.

2. **Enter Details (Loyalty Specialist):**
   - **Display Name:** e.g., `Loyalty Specialist`
   - **Description:** Enter a description of capabilities,
      ```
         Loyalty Specialist is an assistant designed to know and offer the best deals on Credit Cards and Memberships. Any questions related to those topics should be directed towards this assistant. Additionally any time the customer is overly positive this assistant should be used to retain them.

         Example Questions:
         "Wow that seems like a great vacation, I wish there was a more affordable way to afford it"
         "I need a new credit card to afford that"
         "Thanks for all your help"
         "Do you offer a credit card"
         "What are membership perks?"
      ```
   - **API Key:** Enter `123`
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



## Bonus Steps
- Install podman
- Create a quay.io account
- Create a new quay.io organization and public repository <quay-repo>
- Clone https://github.com/watson-developer-cloud/watsonx-orchestrate-developer-toolkit/tree/main/
- Go to one of the examples
- Adjust the code as desired
- Execute this code in terminal
   ```
   DATE_TAG=$(date +%Y-%m-%d);
   podman build --platform linux/amd64 -t external-agent .;
   podman tag external-agent:latest quay.io/mattmule/<quay-repo>:latest;
   podman tag external-agent:latest quay.io/mattmule/<quay-repo>:$DATE_TAG;
   podman push quay.io/mattmule/<quay-repo>:latest;
   podman push quay.io/mattmule/<quay-repo>:$DATE_TAG;
   ```
- Replace image information with the newly created information
- Check out https://github.ibm.com/Matthew-Mueller/wxo-external-agent-template/tree/main for an example (crewai)
