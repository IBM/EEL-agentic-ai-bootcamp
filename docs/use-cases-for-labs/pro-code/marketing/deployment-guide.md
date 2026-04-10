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

**Install podman**
```bash
brew install podman
```


## Step 1: Install Dependencies

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 2: Setup Environment Variables

Create a `.env` file with your credentials , you can copy paste 'example.env' from zip folder in .env and update with your credentials.

```bash
# IBM Cloud API Key
IBM_CLOUD_API_KEY=your_api_key_here
WATSONX_DATA_API_KEY=your_api_key_here

# watsonx.data Instance Details
#You can these details from watsonx.data instance
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

## Step: Get Application URL

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

After deployment, add the MCP server to watsonx Orchestrate , append /mcp in the end:

1. **Get MCP Server URL:**
   ```
   https://watsonxdata-mcp.abc123.us-south.codeengine.appdomain.cloud/mcp
   ```

2. **Add to watsonx Orchestrate:**
   - Go to: watsonx Orchestrate → Tools → Add MCP Server 
   - Select: "Remote MCP server" 
   - Name : 'marketing-recommendation-mcp-tool'
   - Description: `IBM watsonx.data MCP Server for querying lakehouse data, exploring catalogs, and managing data operations using natural language.`
   - Enter Server URL: <MCP Server URL> 
   - Add the listed tools
   - save

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

## Step 3: Initialize and Start Podman

Ensure Podman is initialized and started:

```bash
podman machine init
podman machine start
```

**Note:** Execute these commands in the directory where the Dockerfile is located.

---

## Step 4: Build the Container Image

Build the image using Podman:

```bash
podman build --platform linux/amd64 -t mcp-server-app .
```

## Step 6: Login to IBM Cloud

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

## Step 7: Verify IBM Container Registry

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

## Step 8: Create Container Registry Namespace (if needed)

List existing namespaces:

```bash
ibmcloud cr namespace-list
```

If you don't have a namespace, create one:

```bash
ibmcloud cr namespace-add your-namespace-name
```

---

## Step 9: Tag the Image for IBM Container Registry

Tag the image with the full registry path:

```bash
# Tag the image
podman tag mcp-server-app:latest $REGISTRY/$NAMESPACE/$IMAGE_NAME:latest
```

**Example:**
```bash
podman tag mcp-server-app:latest jp.icr.io//mcp-server-app:latest
```

---

## Step 10: Login to IBM Container Registry

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

## Step 11: Push Image to IBM Container Registry

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

## Step 12: Create or Select Code Engine Project

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

## Step 13: Create Registry Access Secret

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

**Note:** This secret allows Code Engine to pull images from your private registry.
```
---

## Step 14: Deploy Application to Code Engine

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

## Step 15: Get Application URL

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

After deployment, add the MCP server to watsonx Orchestrate , append /mcp in the end:

1. **Get MCP Server URL:**
   ```
   https://watsonxdata-mcp.abc123.us-south.codeengine.appdomain.cloud/mcp
   ```

2. **Add to watsonx Orchestrate:**
   - Go to: watsonx Orchestrate → Tools → Add MCP Server 
   - Select: "Remote MCP server" 
   - Name : 'retail-recommendation-mcp-tool'
   - Description: `IBM watsonx.data MCP Server for querying lakehouse data, exploring catalogs, and managing data operations using natural language.`
   - Enter Server URL: <MCP Server URL>
   - Add the listed tools
   - save

3. **Verify:**
   - Test MCP tools in Orchestrate
   - Try "List Engines" or "List Schemas"
