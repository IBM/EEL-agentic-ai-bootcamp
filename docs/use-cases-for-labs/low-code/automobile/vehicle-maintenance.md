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

## Step by step hands-on instructions

- Please find the step by step hands-on instructions to execute this lab here: [Lab-guide](lab-guide.md)