## Use case : Personalized Customer Experience and Wealth Planning with AI Agents 

As organizations expand, one of the key operational activities is in managing the onboarding process efficiently and consistently. The complexity of coordinating multiple stakeholders, systems, and tasks often leads to delays, onboarding,miscommunication, and a fragmented new-onboard experience. With the introduction of Onboarding system and advanced reasoning models, enterprises now have the opportunity to implement a centralized onboarding solution.

## Problem

Wealth Bank's digital onboarding process faced challenges in efficiently engaging users seeking financial guidance through their online portal. Visitors often arrived with wealth-related queries but left without receiving personalized support or registering for services. Issues include:

- Lack of instant onboarding led to missed opportunities for client conversion.
- Disconnected experiences between query resolution and registration reduced user engagement.
- Manual data entry and disjointed processes failed to capture conversation context, limiting personalization. 

The AI-powered agent now transforms this experience by handling all interactions in natural language, responding to user queries, maintaining context, and seamlessly registering users for personalized financial advice—directly within the chatbot interface.


## Objective

Wealth Bank plans to implement an AI-powered Onboarding Agent to transform how users engage with its digital wealth advisory services. This intelligent assistant will guide users from their initial wealth-related queries to instant registration for personalized financial advice—all through a seamless, conversational interface. The goal is to create an AI-enabled system that enhances user experience and onboarding by:

- Engaging users in natural language to address wealth and investment-related queries.
- Maintaining context throughout the conversation to deliver relevant and personalized responses.
- Encouraging users to register for tailored financial advice based on their needs and interests.
- Seamlessly capturing user inputs and instantly registering them with Wealth Bank within the chatbot.
- Storing conversation context to ensure continuity and improved personalization across future interactions.

By automating and personalizing the onboarding journey, Wealth Bank aims to increase client conversion, enhance user satisfaction, and streamline the path to financial advisory services.

## Business Value 

- Reduction in manual onboarding and data entry efforts.
- Seamless, AI-driven registration through natural language conversations.
- Increased user engagement and higher conversion to personalized financial services.
- Real-time context retention for improved personalization and client satisfaction.
- Faster onboarding process, leading to quicker access to advisory services.

## Architecture

![2](../imagesLab7/archImage.png)

## Step-by-step hands-on guide

It demonstrates how to implement the use case using watsonx.ai and watsonx Orchestrate, with step-by-step guidance available here.


### Accessing the IBM watsonx Orchestrate Platform

To create an AI Assistant in watsonx Orchestrate, you first need to access the platform and navigate to the AI Assistant Builder.

1. Log in to [ IBM Cloud account](https://cloud.ibm.com/notifications?type=account).

    ![2](../imagesLab7/login1.png)

2. Navigate to the [Resources](https://cloud.ibm.com/resources) Page.

    ![2](../imagesLab7/login2.png)

3. Click on **Launch watsonx orchestrate** , it will take you to the orchestrate interface .

    ![2](../imagesLab7/login3.png)

### Create the Fund Management AI Assistant 

1. Click on **Assistant Builder**

    ![2](../imagesLab7/bot1.png)

2. Click on **New** to create a new AI Assistant

    ![2](../imagesLab7/bot2.png)

3. Enter following details in the screen and click on **Create**
- Assistant name : **Fund Management Bot**
- Description : A chatbot to assist users with fund management queries and investment options.
- Assistant language - Default (English(US))
A new Fund Management Bot assistant is created .
    ![2](../imagesLab7/bot3.png)

4. On the left panel click on **Actions** . Click **Create Action** to create the first action.

    ![1](../imagesLab7/bot4.png)

5. Click on **AI-Guided** action . 

    ![1](../imagesLab7/botAction1.png)

6. Enter following details and click on Save to save the action :
    Phrase : **GenAI Chat Action**

    ![1](../imagesLab7/botAction2.png)

    Large Language Model : granite-3b-instruct model (recommended)

!!! info "Add Knowledge"
    
You are digital assistant at Wealth Bank. Your primary responsibility is to assist customers with their financial needs, specifically with investment suggestions.Wealth Bank offers a variety of investment products tailored to different time horizons: short-term (1-2 years), mid-term (3-5 years), and long-term (5+ years).

!!! info "Add prompt instructions"
    
Greetings

![1](../imagesLab7/botAction3.png)

6. Repeat step 5 to create another **AI Guided** Action **Investment Query Classification Prompt**

Action Name : Investment Query Classification Prompt
Large Language Model : granite-3b-instruct model (recommended)


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
3. Ask for registration if more personalized offer needed or existing customer show the offers. 

    ![7](../imagesLab7/7.png)


## Import the skills in Skill Catalog 

### Pre-requisite

Download the files [CustomerInfo](../files/customerInfo.json) and [Customer Onboard](../files/customerOnboard.json) to proceed with the steps below.

1. Click on **Skill Studio** . Click on **Create** --> **Import API**

    ![1](../imagesLab7/skill1.png)

2. Browse and import customerInfo.json ( provided as part of labs)

    ![1](../imagesLab7/skill2.png)

3. Enhance and Publish the skill .
 
4. Go to Skill Catalog search for customerInfo skill and click on **Add Skill** and then **Connect App**. 
Username : test
Password : test 

    ![1](../imagesLab7/skill4.png)

5. In Skill Catalog , search for **Microsoft Outlook** , search for **Send an email** skill click on it . Click on **Connect App** . Provide your outlook credentials .

6. Before importing skill flow , it is essential thats the skills comprising the skill flow are part of skill catalog . Now follow steps 1 and 2 to  import the skill flow **customer Onboard.json**

7. Enhance the skill flow and publish it . 
 
### Connecting to apps 

1. Click on **Skill Sets** . Select the **Fund Management Bot draft** in the dropdown . 
- Search for skills imported in the previous steps and click on **Connect App** , edit **Team Credentials** and save for both skills .

!!! info "Credentials"
    cp4admin / EpZP3ZeTlhgiw0DhCQxQ


    ![1](../imagesLab7/skill6.png)
    ![1](../imagesLab7/skill7.png)

- Search for **Outlook** and click on **Connect App** . Give your outlook credentials

The skills are ready to be used by the **Fund Management Bot**

### Create a skill-based action

1. Navigation to **Assistant Builder** . Ensure in the top panel **Fund Management Bot** is selected . Click **Create Action** to create the **Skill-based action**

    ![1](../imagesLab7/skill8.png)

2. Click on **customerInfo** and click on **Next** to create a customerInfo skill based action
Phrase : Register customer

    ![1](../imagesLab7/skill9.png)

Click on Save to save the action .

    ![1](../imagesLab7/skill10.png)

### Create a custom-built action

1. Click **Create Action** to create the **Custom-built action**
Phrase : I want help on investment

    ![11](../imagesLab7/11.png)

2. Click on **New Step +** to add a new step .
Set **is Taken** field : default value **without conditions**

    ![12](../imagesLab7/12.png)

- Enter value in **Assistant says** field .

!!! info "Assistant says"

Hello! I'm your digital assistant at Wealth Bank, ready to assist with your financial needs. How can I help you today? Are you interested in investment recommendations, or do you have questions about our investment products?

    ![13](../imagesLab7/13.png)


3. Click on **New step +** button  and name it as **Initial Confirmation**. In the Is taken field, retain default value .

- Enter value in **Assistant says** field .

!!! info "Assistant says"

Please enter your query here...

- Click on Define customer response as free text .

    ![13](../imagesLab7/lab13.1.png)

- Select Sub action .

    ![13](../imagesLab7/lab13.2.png)

- Select – **Investment Query Classification prompt** and save the step.

    ![13](../imagesLab7/lab13.3.png)


    ![14](../imagesLab7/14.png)

4. Click on **New Step +** . Click on **Set variable values** . Click on **Set value +**

    ![15](../imagesLab7/lab15.1.png)

- Create a session variable  as **Inventory Query**

    ![15](../imagesLab7/15.png)

 - Set **Inventory Query** to 2.Initial Confirmation

    ![16](../imagesLab7/16.png)

5. Click on **New Step +** and call it **Ask for Register**

    ![17](../imagesLab7/lab17.1.png)

- Enter value in **Assistant says** field .

!!! info "Assistant says"

We have expert team of financial advisors, who will work with you to structure your financial portfolio. We would encourage you to register with us.

- Click Define customer response as **confirmation**

    ![17](../imagesLab7/17.png)

6. Click on **New Step +** 

- Is Taken Field : with conditions

- if **ask for register** is **Yes**

!!! info "Assistant says"
    
    Please enter your details..."

- Click Define customer response as sub-action and select **customer onboard**

    ![17](../imagesLab7/18.png)

- Save and exit

    ![19](../imagesLab7/19.png)

7. Click on **New Step** . Call it **Upload documents**
 Is Taken Field : default value 

 !!! info Assistant says :

 Thank you for registering. Please upload your investment portfolio doc here - Upload file 
 
 - Create a link **Upload File** and enter the value 
 
 https://cloud-object-storage-cos-wxo.s3.jp-tok.cloud-object-storage.appdomain.cloud/WB_NEW.html


    ![20](../imagesLab7/19.1.png)


## Publish the AI Assistant 

1. Click on **Publish** to publish the chatbot in Live environment. 

    ![20](../imagesLab7/20.png)
 
- Review all draft content

    ![21](../imagesLab7/21.png)

- Click on publish 

    ![22](../imagesLab7/22.png)
    
When you publish your content, AI assistant builder creates a snapshot of the draft content, resulting in a version. This version contains all of the content from actions, including settings and variables.

    ![23](../imagesLab7/23.png)

### Embedding AI Assistant in a web page

1. Click on **Integrations**

    ![24](../imagesLab7/24.png)
    
2. Select **Web Chat** and click on Open

    ![25](../imagesLab7/25.png)

3. Select Live environment

    ![27](../imagesLab7/27.png)

4. Select on **Embed** tab. Copy the **script** tag .

    ![28](../imagesLab7/28.png)

## Embed this code in web html file to run the AI assistant.

Download the files [FundManager](../files/FundManager.html) and [John Doe Portfolio.pdf](../files/JohnDoePortfolio.pdf) to proceed with the steps below.

Add the script tag copied in step 4 to render the AI Assistant in the wed page .

### Running the AI Assistant in a web page 

1. Enter query 
    ```
    I want help on investment
    ```

    ![28](../imagesLab7/labchat1.png)

2. Enter query 
    ```
    I would like to invest 100000 for 4 years** . 
    ```
    ![28](../imagesLab7/labchat2.png)

3. The AI assistant will ask if you want to register , click **Yes** . A form will pop up , fill the details and Click on **Apply** 

    ![28](../imagesLab7/labchat5.png)

    ![28](../imagesLab7/labchat6.png)

Upon onboarding , registered user would receive an email notification .  

    ![28](../imagesLab7/labchat7.png)

Upload the pdf provided in the step above in the **Document Upload** section in the same webpage

    ![28](../imagesLab7/labchat8.png)

4. You can ask follow up questions as well like  
    ```
    How is the real estate sector performing now ?**
    ```

    ![28](../imagesLab7/labchat3.png)

5. Enter query 
    ```
    Do you think infrastructure is good sector to invest at current market conditions**
    ```
    ![28](../imagesLab7/labchat4.png)
