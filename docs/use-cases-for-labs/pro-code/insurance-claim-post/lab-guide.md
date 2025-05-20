# Health Insurance - Post Hospitalization Claim LAB Guide

This LAB is written to simulate a customer care agent for hospitals. Healthcare insurance claims post hospitalization scenario that involve multiple steps, data sources, and decision points, making it ideal for a multi-agent system. 

## Pre-requisites:

- Make sure you've already setup the environment:
- [Lab 0 - Environment setup: Pre-requisites](../../labs/environment-setup-lab/)
- [ADK Installation](https://developer.watson-orchestrate.ibm.com/getting_started/installing)
- [Download files](https://ibm.ent.box.com/folder/321723563348?s=ip9fq5u0b8pty8dvrlza8ikrs8cel4xg)
- Download the zip file from Lab2 folder

## Steps to import
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
6. Run the import all script `./scripts/import-all.sh`
7. Go to Manage Agents on your Watsonx Orchestrate Instance and make sure you deploy each imported Agent.

## Test your Agents

[Demo Video](https://ibm.box.com/s/00xsb9gn53pq02ycqvn2ju9o3p8ei88d)

**Try with generic query - This should use backend knowledge base for generic health insurance queries**

- Below query responses should come from "nsa-health-insurance-basics.pdf" document

```
1: Does a Health Plan Typically Pay for Services from Any Doctor?
2: What are some typically costs that consumers pay when they have insurance ?
3: Can you please share examples of Health Insurance Cost Sharing ?
4: Can you share more details on self-insured employer plans vs. fully-insured plans ?
5: What's Explanation of Benefit (EOB) document ?
6: Give me an example where the consumer has not paid anything toward the out-of-network deductible.

```

**Health Insurance Claim process flow**

- Start a new Chat for the following flow

```
I need to submit a new claim for a doctor's visit.
```

- Agent should ask about memberId and date of birth to verify/authenticate the member details

```
My MemberId is MEMBER456 and date of birth is: 1985-07-22
```

- Authentication would be done by calling **authentication tool**
- After authentication, Agent should ask for other details for initiating the claim process
- User should response one of the below bases on what Agent asks for:

- Next, if Agent asks for the name of the patient and date of service

```
Name of the patient is Sarah Johnson. Dr. Emily Carter on October 26th, 2023. And I also had some lab tests done at Quest Diagnostics the same day.
```

- If Agent asks for description of the services or charges

```
I had a chest pain and Dr. Emily did some initial checks but she asked for a few lab tests that I get done by Quest Diagnostics.  Doctor's charges were $50 and Lab test charges were $150.
```

- Based on the details asked by the Agent you can provide details one by one OR just provide all the below details that the user can provide from services taken.  These details in real scenario can be found in Superbill or receipts by the Doctor/Hospital or the Labs after the diagnosis:

```
Here are all the details:
Superbill - Health Clinic Inc.
Patient: Sarah Johnson (ID: MEMBER456)
Date of Service: 2023-10-26
Provider: Dr. Emily Carter, NPI: 1234567890
Service Code (CPT): 99214, Diagnosis (ICD-10): M54.5, Charge: $250.00
Provider: Quest Diagnostics, NPI: 0987654321, Charge: $120.00
Service Code (CPT): 80053 (Lab Panel), 

```

- You can see the reasoning done by LLM used by respective Agent and check each step processed by different collaborator agents calling different tools. Output of each tool call is shown under each step.

- Go to your [ServiceNow instance](https://developer.servicenow.com/dev.do) developer portal and from "workspaces" menu, click on "Service Operations Workspace" to see all the incidents:

![img.png](../../../images/SNOW_DeveloperPortal.jpg)

- Here you should see the created Incident:

![img.png](../../../images/SNOW_incidents.jpg)

- Here Clinical Review & Fraud Detection along with Payment processing can be done by Human-in-the-loop.

## Important things to consider

- Make sure you go through the Agents and Tools files from the downloaded artifacts
- This use case is built using all native Agents and tools in Watsonx Orchestrate
- Agents and respective tools are deployed within wxO instance and AgentOps is taken careof.
- For adding Observability, you can integrate it with Langfuse and that would show all the traces, sessions, observations and more from all Agents, LLMs, Thinking process and much more on the dashboard.
- For further Agentic AI Governance, this can be integrated with IBM Watsonx Governance.