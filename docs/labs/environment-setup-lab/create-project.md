# Lab 0 - Environment setup: Setup your first project in watsonx.ai

Before starting the first technical lab, we will be walking through how to create your own project to get familiar with watsonx.ai and ensure you have access to your environment for the bootcamp.

It is important we create a project in the right environment, or else it will cause issues down the line!

### 1. Log into watsonx<a name="log-in-to-watsonx"></a>

Follow this link to log into watsonx: <https://dataplatform.cloud.ibm.com/wx/home?context=wx>

!!! info
    Please accept the Terms & Conditions!

### 2. Check that you are in the right instance<a name="check-instance"></a>

You should now be taken to the watsonx home screen. Check at the top right that you are in the right instance. If it does not show the right name of the instance, you can select it in the drop-down. For the entirety of the bootcamp, you will be working in that same instance!

If you do not know your instance, go to your techzone reservations list https://techzone.ibm.com/my/reservations. Look for your recently created reservation and click on "Open this environment". Scroll down and look for a reservation name that looks similar to this:  **ITZ-WATSONX-21.**

**Note:** The instance at the top right tends to change to your default personal account every time you switch/go back to a new page. Thus, it's always good to check the top right corner every time you switch to a new page.

![check-right-instance](../../images/check-right-instance.png)

### 3. Create a new project<a name="new-project"></a>

Now, we can go ahead and create a new project. 

In the **Projects** section, click the "+" symbol to create a new project.
 
Or, use the link here to trigger a [New Project](https://dataplatform.cloud.ibm.com/projects/new-project?context=wx) creation.

![create-new-project](../../images/create-new-project.png)

Enter a **unique name** for your project, include both your first and last name and any other information you would like.

![unique-name](../../images/unique-name.png)

### Cloud Object Storage (COS)
It is likely there is also already a Cloud Object Storage instance selected for you, with a name that starts with "itzcos-..." If so, you don't have to do anything! 

Otherwise, you may be prompted to select from multiple instances. Please consult with your bootcamp lead which COS instance to select.

![select-instance](../../images/select-instance.png)

### Click Create
Now, click Create. It may take a few seconds to officially be created.

### 4. Associate the correct runtime instance<a name="runtime-instance"></a>

With the project created, you should be directed to the project home page. Select the "Manage" tab.

Click on "Services and Integrations" in the left sidebar. Then, click on "Associate service."

![manage-tab](../../images/manage-tab.png)

Select the service listed with "Type" = "watsonx.ai Runtime" and click **Associate**. 

![select-runtime-service](../../images/select-runtime-service.png)

**Note:** If you can't find the service, remove all filters from the "Locations" dropdown. If you see 2+ Watson Machine Learning services, select the one where "Group" = the same *environment* name of the instance. The *environment* name can be found on https://techzone.ibm.com/my/reservations. 

![techzone](../../images/techzone.png)


Time to get started with your first use case!