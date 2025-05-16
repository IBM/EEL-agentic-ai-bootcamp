# Vehicle Maintenance use case

## Overview

The Vehicle Troubleshooting Assistant is an AI Agent designed to help car owners identify and understand vehicle issues by interpreting natural language inputs like “My car is shaking” or “Check engine light is on.”
It combines real-time telematics data, diagnostic trouble codes (DTCs), and vehicle documentation to offer personalized, accurate diagnostics and actionable guidance such as finding nearby service centers, etc.

## Reference Architecture

![image](https://github.ibm.com/ecosystem-engineering-lab/wxo_agents/assets/244854/ba1b2444-be65-43e1-b7c7-31148495dc22)

## Key Components

- Telematics data analyzer agent (External Agent) – Get the car telematics data and analyze it to provide a natural language summary
- Get Telematics data (Tool) – Get the telematics data of a car. (simulation)
- Get nearest service center (Tool) – Get the nearest service center. (takes lat & lon and gives results)
- Troubleshoot agent (Native wxO Agent) – A supervisor agent that orchestrate between the following:
    1. Knowledge (RAG):
        a. DTC code list.pdf
        b. Car user manual.pdf
    2. Toolset:
        a. Agents:
            i. Telematics data analyzer agent
        b. Tools:
            i. Get nearest service center

## Benefits

- **Customer Experience:** Reduces stress for drivers by providing instant, understandable insights.
- **Service Optimization:** Reduces unnecessary service visits and helps service centers prioritize real issues.
- **Brand Loyalty:** Builds trust by offering proactive, intelligent support post-purchase.
- **Data Utilization:** Leverages telematics data and DTC documentation to deliver accurate, data-driven support.
- **Scalability:** Easily extendable across vehicle models, regions, and support channels (mobile app, web, IVR).

## Deploy the tools

## Build on UI

## Suggested script

1. “What does the engine temperature warning light mean?” -> Troubleshoot agent will use the Knowledge base to RAG and answer this query
2. “Help me diagnose my car. It is shaking and I have the engine temperature warning light on.” -> Troubleshoot agent will transfer the control to Telematics data analyzer agent which will ask follow-up questions if required and give a car health report. The car report is read, and a suggestion is provided by the Troubleshoot agent.
3. “Where is the nearest service center?” -> Troubleshoot agent will invoke the Get nearest service center tool and pass the lat & long received from the Telematics data analyzer agent (assumption is that car will send the current lat & long data as part of telematics data.) and get the nearest service centers from the list of service centers.