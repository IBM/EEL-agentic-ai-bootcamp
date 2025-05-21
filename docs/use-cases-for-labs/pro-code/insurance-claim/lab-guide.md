# Cashless claim process: customer support & Pre-authorization

## 🛠️ **Lab guide -  Use Case Implementation Guide** 



This guide provides step-by-step instructions for building and testing the use case.

### 📌 Use Case Summary

The use case outlines two key stages in the **cashless hospitalization claim process**:

1. **📞 Customer Support**
   - Assist policyholders with claim-related inquiries.
   - Clarify policy benefits and processing steps.

2. **⚙️ Pre-Authorization Calculation**
   - Automated back-end process for insurers.
   - Determines approved coverage based on hospital treatment estimates.

### 🎯 Scenario

A policyholder seeks treatment with an active insurance policy but faces uncertainties:

- ❓ **Unclear on coverage & cashless claims**
- 💸 **Concerned about out-of-pocket expenses**

**Key Requirements:**  
✔️ Transparent policy benefits explanation.  
✔️ Clear breakdown of insurer-approved amount vs. hospital treatment cost.

This use case ensures a **seamless customer experience** while optimizing insurer workflows.

## ⏳ **Build and run**

### Pre-requisites:

- Make sure you've already setup the environment:
- [Lab 0 - Environment setup: Pre-requisites](../../labs/environment-setup-lab/)
- [ADK Installation](https://developer.watson-orchestrate.ibm.com/getting_started/installing)

 **Steps to connect with service-now**
1. Sign-up for a Service Now account at https://developer.servicenow.com/dev.do
2. Validate your email address (check email)
3. On the landing page click start building. This will allocate a new instance of SNOW for you.
4. Back on the landing page, click your profile icon on the top right and under "My instance" click manage instance password.
5. Create an application connection using these credentials
```bash
orchestrate connections add -a service-now
orchestrate connections configure -a service-now --env live --type team --kind basic --url <the instance url>
orchestrate connections set-credentials -a service-now --env live -u admin -p <password from modal>
```
**Download lab files**

Download the required lab files from [here](https://ibm.box.com/s/em1p0uhoi56ixjym3ig8ql3j7vgnyg2d). Unzip it to some folder.

### **Create project structure**

Create following folder structure -
    
    wxo-agents ---
                  |---agents
                  |---tools
                  |---knowledge_base
                      |---documents

### **Creating tools**
There are many tools used in this use-case, however, for lab purpose we will be creating one python tool and will import rest of the required tool.

Create a tool to call a decision service to calculate the pre-authorized amount.

Steps - 

1. create a file in **tools** directory called `calculate_preauth_amount.py`

2. add following imports to your file

    ```python
    from pydantic import Field, BaseModel
    from typing import Optional
    from ibm_watsonx_orchestrate.agent_builder.tools import tool
    import requests
    ```

3. add following method 

    ```python
    def calculate_preauth_amount(
            estimated_treatment_cost: float,
            policy_coverage_limit: float,
            disease_category:str,
            hospital_tier: int,
            co_payment_percentage: float,
    ) -> dict:
        """
        Calculate pre-authorization amount for insurance claims.
        Accepts parameters as keyword arguments which will be converted to ClaimPreauthAmountRequest.
        """
        try:

            req = {
                "estimated_treatment_cost": estimated_treatment_cost,
                "policy_coverage_limit": policy_coverage_limit,
                "disease_category": disease_category,
                "co_payment_percentage": co_payment_percentage,
                "hospital_tier": hospital_tier
            }
            base_url = "https://preauthorisation-ordermanagement.cp4bautomation-685c4d909dba5536870f4da931535b5a-0000.eu-de.containers.appdomain.cloud/preauth/calculate"
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }

            response = requests.post(
                base_url,
                headers=headers,
                json=req
            )
            response.raise_for_status()

            response_data = response.json()
            return response_data

        except Exception as e:
            return dict(
                approved_amount=0,
                currency="INR",
                message=f"Error: {str(e)}"
            )
    ```

4. add below decorator to *calculate_preauth_amount* method 
```python
@tool(name="calculate_preauth_amount", description="Calculates the pre-authorized amount")

```
5. copy all the file in tools folder to your 'wxo-agents/tools' folder

6. add followings to your *'requirements.txt'*
```commandline
requests
```
7. You can use below command to import your tools
```commandline
$ orchestrate tools import -k python \
    -f "<path-to-your-tool>/<tool-file-name>.py" \
    -r "requirements.txt"
```

8. However, we have provided shell/bat scripts to automate this step. Run the script:
```
./import-tools.sh
```


### **Creating knowledge**
In watsonx Orchestrate, agents can use knowledge bases to search for user requests and return relevant, grounded content or answers.

You can create two types of knowledge bases: built-in and external. Built-in knowledge bases are created using a built-in Milvus instance and are populated with documents you import. External knowledge bases refer to your own Milvus or Elasticsearch instances, which you can connect to watsonx Orchestrate for use by agents.

In this lab we are going to build in-built knowledge base.

Steps - 

1. copy pdf files from lab documents to wxo-agents/knowledge_base/documents
2. create *medibuddy_claim_process.yaml* file and add following 
```yaml
spec_version: v1
kind: knowledge_base 
name: medibuddy_claim_process
description: This knowledge addresses the claim process for Medibuddy insurance.
documents:
  - documents/medibuddy_guidelines.pdf
```
3. create *users_insurance_policy.yaml* file and add following 
```yaml
spec_version: v1
kind: knowledge_base 
name: insurance_policy_details
description: This knowledge addresses the user's insurance policy details.
documents:
  - documents/Comprehensive_health_policy.pdf
```
4. Import both the knowledge-base using below command
```commandline
orchestrate knowledge-bases import -f <knowledge-base-file-path>
```
### **Creating agents**

With the ADK, you can create native agents, external agents, and external watsonx Assistants agents. Each of these agent types requires its own set of configurations.

In this lab, we will build and import native agents of each type listed below, and then import the remaining agents..

We are having two types of native agents in our use case.
1. Agents using knowledge_base
2. Agents using tools 

Steps -

1. **Create native agents with knowledge_base** - create *policy_support_agent.yaml* file and add below content
```yaml
spec_version: v1
kind: native
name: policy_support_agent
description: This agent provides answers to the frequently asked questions related policy claim process, network hospitals and any other information related to the users insurance policy.
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
style: react
instructions: >
  You are a QnA agent. Your task is to answer the questions related to the users insurance policy. 
  You can use the knowledge base to answer the questions. 
  If you are not sure about the answer, please ask for clarification do not provide a generic response.
  You can also ask for more information if needed.
  You can also provide links to the relevant documents in the knowledge base.
  Don't make up answers.
  
  Transfer to supervisor is must

knowledge_base:
  - insurance_policy_details
```
2. **Create native agents with tools** - create *claim_adjudication_agent.yaml* and below content
```yaml
spec_version: v1
style: default
name: claim_adjudication_agent
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
description: >
  your primary goal is to calculate pre-authorized amount based on the information collected and received.
  
  you are an agent responsible for claims adjudication, you use your decision-making capability to evaluate, validate, and settle claims.
  The goal is to balance fair payouts to policyholders while protecting the insurer from unjustified losses. 
  Efficient adjudication improves customer satisfaction and operational accuracy.
  
  your primary goal is to calculate pre-authorized amount based on the information collected and received.

instructions: >
  
  Condition: Transfer from claim_analyst_agent
    Action:
      1. Use read_email tool to read the email and get the required information
      2. Use get_network_hospitals to get the hospital_tier hospital mentioned in email sent from hospital
      3. Use get_policy_info tool to get the information about policy using customer id passed by user. remove '%' from co payment before passing to calculate_preauth_amount tool.
      4. Must call calculate_preauth_amount tool  to calculate the pre-authorized amount
      5. Prepare a summary based on all above information
      6. Transfer to supervisor:
         "observation: send report to customer's email."
  

tools:
  - calculate_preauth_amount
  - read_email
  - get_network_hospitals
  - get_policy_info
```
3. copy all the .yaml file from *lab_file/agents* to *wxo-agents/agents*

4. **Importing the agents** - use below commands to import the agents

```commandline
orchestrate agents import -f <path to .yaml/.json/.py file>
```

## **Test the use case**

### **Front desk agent**

Select 'claim_support_desk_agent' from agents menu on left hand-side.

Use below script to test the front desk agent 
```commandline
- What is covered under in-patient treatment in this policy?
- What are the exclusions for domiciliary treatment?
- I want initiate a claim process
```
if prompted for customer id and aadhar. Enter below 
```commandline
my customer id is CUST001 and aadhar is 1234-5678-9012
```
### **Claim analyst agent**

Select 'claim_analyst_agent' from agents menu on left hand-side.

Use below message to trigger the agent 
```commandline
- Calculate pre-authorization amount for customer CUST001
```