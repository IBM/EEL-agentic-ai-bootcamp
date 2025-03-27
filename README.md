# Documentation Template

Documentation is an integral part of any project. This template is a good starting point for your documentation. The template uses [Mkdocs](https://www.mkdocs.org), a static site generator to convert your markdown files into HTML and host it on github pages.

![conversion](https://user-images.githubusercontent.com/52746337/161740278-ba4dc688-669b-4bdf-9deb-8ce3a8b78879.png)


Here is how you can use it after creating your repository from the template repository:

- All content in the [/docs](/docs/) folder will be converted to HTML by [MkDocs](https://www.mkdocs.org)

- Follow the [Automate Mkdocs deployment on GitHub Pages using OpenShift Pipelines](https://developer.ibm.com/tutorials/use-openshift-pipelines-on-any-cloud-to-automate-mkdocs-deployment/) tutorial to setup a tekton pipeline to deploy your documentation site.

- You can add/edit your documentation in the [/docs](/docs/) folder and commit the changes to the GitHub repository.

- The documentation will be automatically deployed as a static site on GitHub Pages.

- Link to access the documentation will automatically get updated in the About section of the Repository.
