## Deploy the tools

## Build on UI

## Suggested script

1. “What does the engine temperature warning light mean?” -> Troubleshoot agent will use the Knowledge base to RAG and answer this query
2. “Help me diagnose my car. It is shaking and I have the engine temperature warning light on.” -> Troubleshoot agent will transfer the control to Telematics data analyzer agent which will ask follow-up questions if required and give a car health report. The car report is read, and a suggestion is provided by the Troubleshoot agent.
3. “Where is the nearest service center?” -> Troubleshoot agent will invoke the Get nearest service center tool and pass the lat & long received from the Telematics data analyzer agent (assumption is that car will send the current lat & long data as part of telematics data.) and get the nearest service centers from the list of service centers.