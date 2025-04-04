# Building AI Agent in watsonx Orchestrate
## test
In watsonX Orchestrate, you create an AI assistant using the AI Assistant Builder. This tool is a chat interface builder designed to deliver an engaging and seamlessly embedded chatbot experience. By leveraging the power of large language models (LLMs) and the conversational capabilities of watsonX Assistant, the AI Assistant Builder enables dynamic and interactive conversations between users and watsonX Orchestrate.


## Use case  Test Use Access
TBD


## Key features 
TBD


## Accessing the watsonX Orchestrate Platform

To create an AI Assistant in watsonX Orchestrate, you first need to access the platform and navigate to the AI Assistant Builder.

1. Log in to watsonX Orchestrate
    Open your web browser and go to the watsonX Orchestrate portal.
    Enter your IBM credentials and sign in.
2. Navigate to the Home Page
    Upon logging in, you will land on the watsonX Orchestrate home page.
    This page provides options to build AI skills, automate tasks, and explore learning resources.
3. Access the AI Assistant Builder
    In the "Build" section, find the "AI Assistant Builder" card.
    Click on it to begin creating your AI Assistant.

![1](../imagesLab7/1.png)

## Building your AI assistant with actions

In the AI Assistant Builder, an action is a specific outcome your AI assistant completes in response to a user's request. Actions consist of steps, which guide the conversation between the user and the AI assistant. The interaction starts with user input (e.g., "I want to withdraw money"), may involve additional exchanges for gathering information, and concludes when the assistant fulfils the request.
You can design AI assistants that function like personal assistants by creating AI-guided actions, skill-based actions, or custom-built actions.
The examples in this guide demonstrate building a money withdrawal action. You can modify these to suit your own use case.

## To create AI assistant , do the following steps

1.	Enter Assistant Name
    In the "Assistant name" field, enter a meaningful name for your assistant. Example: Fund Management Bot (or any other relevant name based on your use case). The name is used internally and is not visible to end users.
2.	Provide a Description (Optional)
    You can add a short description that summarizes the purpose of this assistant.Example: "A chatbot to assist users with fund management queries and investment options."This step is optional but helps in organizing multiple assistants.
3.	Select Assistant Language
    From the "Assistant language" dropdown, choose the preferred language for the assistant.By default, English (U.S.) is selected.
4.	Proceed to the Next Step
    Click the "Next" button at the top-right corner to continue to the Personalization step.

![2](../imagesLab7/2.png)
     
## Personalizing Your Assistant
    
In this step, you will personalize your AI assistant by specifying where it will be deployed, your industry, role, and the assistant’s purpose. These choices will help tailor the onboarding experience.

## Instructions
    
1.	Deployment Channel
    Under "Tell us where your assistant will live", select where you plan to deploy the assistant. Options may include Web, Mobile App, Messaging Platforms, or Others. Example: Select "Web" if you plan to use the assistant on a website.
2.	Provide Industry Information
    In the "Which industry do you work in?" dropdown, select your industry.Example: Banking and Financial Services (if the assistant is for a finance-related use case).
3.	Define Your Role
    In "What is your role on the team building the assistant?", choose the most relevant role. Example: Designer, Developer, Product Manager, etc.
4.	Select a Need Statement
    Choose a statement that best describes your AI assistant’s purpose.Example: "I want to make it easier for my customers to find what they’re looking for in my app."This helps refine the assistant’s focus and experience.
        
![3](../imagesLab7/3.png)

## Customizing Your Assistant UI
    
In this step, you will customize the chat UI to align with your brand identity. You can set the assistant’s display name, theme, colons, and other appearance settings.

## Instructions
1.	Set the Assistant's Display Name
    Under "Assistant’s name as known by customers", enter the name that users will see when they interact with the assistant.Example: "Fund Management Assistant"
2.	Choose the Intended Purpose
    Select an option based on the assistant’s main use case:
        Standard: For customer support and virtual agent use cases.
        Carbon for AI: If integrating with IBM internal AI-focused applications.
        Recommended: Standard for most business use cases.
3.	Select a Theme
    Choose between Light or Dark mode based on your brand style.Example: Light mode for a clean, professional look.
4.	Customize Colors
    Primary Color (Chat Header): Define the main color of the assistant's interface.Secondary Color (User Message Bubble): Choose a contrasting color for messages sent by users.Account Color (Special AI Actions): Assign a color to highlight AI-driven responses.
    Example:
        Primary: #FFFFFF (White)
        Secondary: #303D1D (Dark Green)
        Account: #0345AE (Blue)
5.	Set Chat Widget Size (Optional)
    Adjust the width and height of the chatbot window.Default: Width – 380px, Height – 640px(Leave as is if unsure).
6.	IBM Watermark
    Enable or Disable the "Built with IBM WatsonX" watermark based on preference.
7.	Enable Streaming (Optional)
    Streaming allows messages to appear dynamically as they are being typed.Recommended: Keep ON for a more natural user experience.
8.	Upload an Avatar Image (Optional)
    Click "Add an avatar image" to upload a custom icon for your assistant.

![4](../imagesLab7/4.png)

## Previewing Your Assistant

In this step, you will preview how your AI assistant appears and functions on a website before finalizing the setup. This allows you to test interactions and ensure the chatbot is visually and functionally aligned with your requirements.

## Instructions
1.	Review the Chatbot Preview
    The right panel displays a simulated website with the chatbot embedded.Interact with the assistant by typing a message in the input field to see how it responds.Verify that the UI elements, colors, and avatar (if uploaded) appear correctly.
2.	Customize Web Chat (Optional)
    Click "Customize web chat" to modify the chatbot’s appearance further.You can adjust its layout, colors, and positioning based on your website’s design.
3.	Share the Preview (Optional)
    Click "Copy link to share" to generate a preview link that you can send to stakeholders for feedback.

![5](../imagesLab7/5.png)

## Creating an AI-guided action

You can create AI-guided actions to help your assistants to respond to a specific set of inquiries that are based on the preloaded knowledge and instructions.

## To create an AI-guided action, do the following steps:
1.	Click the AI assistant builder tile in watsonX Orchestrate to go to AI assistant builder.
2.	In AI assistant builder, go to Actions > New action > AI-guided action.
3.	In the New action dialog, enter the phrase that the customer must type to start the interaction. Example – GenAI Chat Action
4.	Click Save.
5.	In the AI-guided action page, select the large language model (LLM) from the Select a model dropdown. For more information about models. Example - granite-3b-instruct model (recommended)
6.	Optional: In the Add knowledge* field, you can add a content, which is the knowledge reference for the AI-guided action. This knowledge is sent to the LLM along with the prompt**.
7.	In the Add prompt instructions section, click the Add instructions button if you want to add instructions for the default prompt in your assistant.
8.	Enter the prompt instructions in the Prompt instruction field that help the LLM in your assistant to give refined responses and guide the conversations with clarity and specificity.

!!! info "Add Knowledge"
	
You are digital assistant at Wealth Bank. Your primary responsibility is to assist customers with their financial needs, specifically with investment suggestions.Wealth Bank offers a variety of investment products tailored to different time horizons: short-term (1-2 years), mid-term (3-5 years), and long-term (5+ years).

!!! info "Add prompt instructions"
	
Greetings


## Repeat above steps to create AI guided Action - Investment Query Classification Prompt

!!! info "Select Model"
    
    granite-3-8b-instruct (recommended)

!!! info "Add Knowledge"
    
    You are an AI assistant specializing in investment guidance at Wealth Bank. Your task is to recommend suitable Wealth Bank products based on the customer's investment duration and amount.

    **Products Offered:**

    ##Short-term Investment (1-2 years):

    **WB Ultra Short Fund**

    Monthly SIP: Start with just 500 INR.
    Lump Sum: Minimum investment of 5000 INR.
    Duration: Ideal for 1-2 years.
    Benefits: Low-risk option with reasonable returns, perfect for short-term goals.

    **WB Short Duration Fund**

    Monthly SIP: Start with 1000 INR.
    Lump Sum: Minimum investment of 10,000 INR.
    Duration: Suitable for 1-2 years.
    Benefits: Focuses on short-term debt securities, providing liquidity and safety.

    **WB Quick Access Savings Plan**

    Monthly SIP: Start with 1500 INR.
    Lump Sum: Minimum investment of 15,000 INR.
    Duration: Best for up to 2 years.
    Benefits: Offers easy access to funds with competitive interest rates, ensuring your money is available when needed.

    ##Mid-term Investment (3-5 years):

    **WB Mid Term Fund**

    Monthly SIP: Start with just 500 INR.
    Lump Sum: Minimum investment of 5000 INR.
    Duration: Ideal for 3-5 years.
    Benefits: Balanced fund with moderate risk and potential for steady growth.

    **WB Balanced Advantage Fund**

    Monthly SIP: Start with 1000 INR.
    Lump Sum: Minimum investment of 10,000 INR.
    Duration: Suitable for 3-5 years.
    Benefits: Dynamically managed equity and debt portfolio, aiming for stable returns with reduced volatility.

    **WB Dynamic Bond Fund**

    Monthly SIP: Start with 1500 INR.
    Lump Sum: Minimum investment of 15,000 INR.
    Duration: Best for 3-5 years.
    Benefits: Actively managed bond fund that adjusts duration based on interest rate outlook, providing potential for higher returns.

    **WB Growth and Income Plan**

    Monthly SIP: Start with 2000 INR.
    Lump Sum: Minimum investment of 20,000 INR.
    Duration: Suitable for 3-5 years.
    Benefits: Combines growth from equity investments with the stability of fixed-income securities, offering a balanced approach.

    **WB Multi-Asset Allocation Fund**

    Monthly SIP: Start with 2500 INR.
    Lump Sum: Minimum investment of 25,000 INR.
    Duration: Ideal for 3-5 years.
    Benefits: Diversified across asset classes including equity, debt, and gold, aiming for consistent returns and risk mitigation.

    **WB Hybrid Equity Fund**

    Monthly SIP: Start with 3000 INR.
    Lump Sum: Minimum investment of 30,000 INR.
    Duration: Best for 3-5 years.
    Benefits: Invests in both equity and debt instruments, aiming for growth with a safety cushion.

    ##Long-term Investment (5+ years):

    **WB Long Term Funds**

    Monthly SIP: Flexible amounts starting from 500 INR.
    Lump Sum: Minimum investment of 5000 INR.
    Duration: Ideal for 5+ years.
    Benefits: Diversified portfolio aimed at long-term capital appreciation with a 3-year lock-in period.

    **WB Guaranteed Income Plan**

    Lump Sum: Minimum investment of 3 lakh INR.
    Duration: 12-year investment period, with payouts starting after 15 years of maturity.
    Benefits: After 15 years, receive a monthly income of 40K for the next 15 years plus the invested corpus, ensuring financial stability and steady income.

    **WB Equity Linked Savings Scheme (ELSS)**

    Monthly SIP: Start with 1000 INR.
    Lump Sum: Minimum investment of 10,000 INR.
    Duration: 5+ years, with a 3-year lock-in period.
    Benefits: Tax-saving benefits under Section 80C with potential for high returns through equity investments.

    **WB Child Education Fund**

    Monthly SIP: Start with 1500 INR.
    Lump Sum: Minimum investment of 15,000 INR.
    Duration: Best for 10-15 years.
    Benefits: Structured to accumulate wealth for a child's higher education, with potential growth from equity and debt instruments.

    **WB Retirement Savings Plan**

    Monthly SIP: Start with 2000 INR.
    Lump Sum: Minimum investment of 20,000 INR.
    Duration: Suitable for 15-20 years.
    Benefits: Focuses on building a substantial retirement corpus through a mix of equity and fixed-income securities.

    **Wealth Builder Plan**

    Monthly SIP: Start with 2500 INR.
    Lump Sum: Minimum investment of 25,000 INR.
    Duration: Ideal for 10+ years.
    Benefits: Aggressive growth plan aimed at long-term wealth creation through diversified equity investments.

    **WB Real Estate Investment Fund**

    Monthly SIP: Start with 3000 INR.
    Lump Sum: Minimum investment of 50,000 INR.
    Duration: Best for 7-10 years.
    Benefits: Invests in real estate projects and properties, providing potential for high returns and diversification.

    **WB Prime Real Estate Growth Fund**
    Monthly SIP: Start with ₹5,000.
    Lump Sum: Minimum investment of ₹50,000.
    Duration: Ideal for 8-12 years.
    Benefits: Focuses on high-growth commercial and residential real estate projects, offering potential for significant capital appreciation.

    **Urban Real Estate Opportunities Fund**
    Monthly SIP: Start with ₹4,000.
    Lump Sum: Minimum investment of ₹40,000.
    Duration: Best suited for 7-10 years.
    Benefits: Invests in urban real estate developments, including residential complexes and office spaces, providing a balanced growth opportunity.

    **Global Real Estate Advantage Fund**
    Monthly SIP: Start with ₹6,000.
    Lump Sum: Minimum investment of ₹60,000.
    Duration: Ideal for 10-15 years.
    Benefits: Offers exposure to international real estate markets, providing diversification and access to global growth opportunities.

    **WB Infrastructure Growth Fund**   
    Monthly SIP: Start with 3500 INR.
    Lump Sum: Minimum investment of 35,000 INR.
    Duration: Ideal for 8-12 years.
    Benefits: Focuses on infrastructure projects, offering potential for substantial growth and capital appreciation.

    **Global Infra Growth Fund**
    Monthly SIP: Start with ₹4,000.
    Lump Sum: Minimum investment of ₹40,000.
    Duration: Best suited for 10-15 years.
    Benefits: Invests in global infrastructure projects, offering diversification and long-term growth potential.

    **Tech-Driven Infra Fund**
    Monthly SIP: Start with ₹4,500.
    Lump Sum: Minimum investment of ₹45,000.
    Duration: Ideal for 10-14 years.
    Benefits: Focuses on technology-driven infrastructure projects, offering high growth potential in the rapidly evolving tech landscape.



!!! info "Add prompt instructions"

1. Restatement and Clarification of the Inquiry:
    Repeating the customer’s questions to illustrate comprehension. This indicates attentiveness and ensures clarity.
2. Divide the Investment Options into Segments: Split investment options according to term; which are
    short-term, medium-term and long-term.
    Give detailed product information with key attributes and benefits highlighted.
3. Ask for registration if more personalised offer needed or existing customer show the offers. 

![7](../imagesLab7/7.png)
 
## Creating a skill-based action

Create an action from a skill when you want to implement orchestration for specific conversations in your AI assistant through the skills available on watsonX Orchestrate. 
Before you begin
You must connect to the app of the skill for it to appear as an option in this step

## Connecting to apps
By default, the credential type is not specified for an app. Complete the following steps to assign credential preferences for an app and connect to it:
1.	From the menu , click Skill sets.
2.	On the Fund Manager page, select the Connections tab.
3.	From the drop-down menu with skill sets, select Team skills or an AI assistant or Orchestrate Agent Skillset.
4.	Search and select the app (Ex. – Customer profile) from the search menu.
5.	Click the overflow menu next to the app, and click Connect app.
    set Team credentials:
        Select the option Team credentials.
        Click Connect app.
        Provide the connection details * for the app, and click Connect app.
        All your team members can now use the skills that the app offers without providing the connection details.
        The Credential type of the app is set as Team.
        The Connected by column displays the user details of the person who set the team credentials.

!!! info "Credentials"
    cp4admin/EpZP3ZeTlhgiw0DhCQxQ

![8](../imagesLab7/8.png)

## To create a skill-based action, do the following steps:
Click the AI assistant builder tile in watsonX Orchestrate to go to AI assistant builder. 
In AI assistant builder, go to Actions > New action > Skill-based action.
In the Build an action from a skill page, click the skill(Customer profile) to which you want to link the action to, making the skill the foundation to your action.

![9](../imagesLab7/9.png)

In the Name your action field, enter a name for your action . Example - Register customer
In the Enter a phrase field, enter the phrase that customers must type or ask to trigger an action for the watsonX Orchestrate skill. Example - Register customer   
Click the Save button to save the action

![10](../imagesLab7/10.png)

## Creating a custom-built action

You create a new action from scratch when you want to define each step of your action in your conversation. You can define the steps with or without conditions, which help you to control the customer responses.

You can also use the AI-guided and skill-based actions that you created as subactions for your steps. Its enables to the possibility to pass generated values between these actions to use as you want. For more information about how to use AI-guided and skill-based actions as subactions.

## To create an action from scratch, do the following steps:	

Click the AI assistants tile in watsonX Orchestrate to go to AI assistant builder.
In AI assistant builder, go to Actions > Create action > Custom-built action. 
In the New action dialog, enter the phrase that the customer must type to start the interaction.  Refer below screenshots
After entering the phrase to start the interaction, you must add steps in an action to create the conversation flow. To add a step, use the following instructions:

 ![11](../imagesLab7/11.png)

![12](../imagesLab7/12.png)

Click the New step button in the Conversation steps pane to add a step.   
In the Is taken field, use the default value of without conditions. This step is always required for any withdrawal.
In the Assistant says field, type "Hello! I'm your digital assistant at Wealth Bank, ready to assist with your financial needs. How can I help you today? Are you interested in investment recommendations, or do you have questions about our investment products?"

![13](../imagesLab7/13.png)
 
## Create New Step 
Click the New step button in the initial Conversation pane to add a step.
In the Is taken field, use the value of without conditions. This step is always required for any withdrawal.
In the Assistant says field, type "Please enter your query here..."   
Click Define customer response.
Select Sub action and select – Investment Query Classification prompt

![14](../imagesLab7/14.png)

Set variables –
Set Inventory Query to 2.Initial conversation

 ![15](../imagesLab7/15.png)

![16](../imagesLab7/16.png)

## Create New step 

Click the New step button in the ask for register pane to add a step.
In the Assistant says field, type "We have expert team of financial advisors, who will work with you to structure your financial portfolio. We would encourage you to register with us."
Click Define customer response as confirmation

![17](../imagesLab7/17.png)


## Create new step 

In the Is taken field, use the value of with conditions. 
    if ask for register is Yes
    In the Assistant says field, type "Please enter your details..."
Click Define customer response as subaction and select customer form

![17](../imagesLab7/18.png)

Save and exit

![19](../imagesLab7/19.png)

## Previewing and publishing
After you build an assistant, you can test to make sure it works as you intended before you make it available to customers. AI assistant builder makes it straightforward to preview your assistant in a closed environment and manage exactly what you make available to customers. Go to Publish .

![20](../imagesLab7/20.png)
 
Review all draft content

![21](../imagesLab7/21.png)

Click on publish 

![22](../imagesLab7/22.png)
    
When you publish your content, AI assistant builder creates a snapshot of the draft content, resulting in a version. This version contains all of the content from actions, including settings and variables.

![23](../imagesLab7/23.png)

## Sharing AI assistant with web chat

Click on integration 

![24](../imagesLab7/24.png)
    
Select Web Chat to Open

![25](../imagesLab7/25.png)

Select Live environment

![26](../imagesLab7/26.png)

![27](../imagesLab7/27.png)

Select embed tab

![28](../imagesLab7/28.png)

## Embed this code to web html file to run the AI assistant.
