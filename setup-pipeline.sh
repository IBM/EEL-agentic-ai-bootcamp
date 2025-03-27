#!/usr/bin/env sh

set -e

echo
echo "\033[1;32m-------------Setting up Tekton CI----------------\033[0m"
cd Openshift\ Pipeline/
echo
NAMESPACE=$(oc config view --minify -o jsonpath='{..namespace}')
echo "\033[1;37mUsing Openshift Project: $NAMESPACE\033[0m\n"

echo "\033[1;34mSetting up Tekton Tasks...\033[0m"
cd Tasks/
oc apply -f mkdocs-setup.yaml
oc apply -f mkdocs-lint.yaml
oc apply -f mkdocs-build-deploy.yaml
cd ../
echo "\033[1;34mTekton Tasks setup complete.\033[0m\n"

echo "\033[1;34mSetting up Tekton Pipeline...\033[0m"
cd Pipeline/
oc apply -f pipeline.yaml
cd ../
echo "\033[1;34mTekton Pipeline setup complete.\033[0m\n"

echo "\033[1;34mSetting up Tekton Secrets...\033[0m"
cd Secret/
echo "\033[1;36mEnter your Git username:\033[0m"
read GITUSERNAME
echo "\033[1;36mEnter your Git personal access token:\033[0m"
read -s GITPERSONALACCESSTOKEN
oc apply -f github-credentials.yaml
oc patch secret git-credentials -p '{"stringData": {"username": "'$GITUSERNAME'", "password": "'$GITPERSONALACCESSTOKEN'"}}'
echo "\033[1;34mGit credentials configured. You can view them by running:\033[0m"
echo "\033[1;35moc get secret git-credentials -o yaml\033[0m\n"
cd ../
echo "\033[1;34mPatching Pipeline ServiceAccount...\033[0m"
oc patch sa pipeline -p '{"secrets": [{"name": "git-credentials"}]}'
echo "\033[1;34mPipeline ServiceAccount setup complete.\033[0m\n"

echo "\033[1;34mSetting up Tekton Trigger...\033[0m"
cd Trigger/
oc apply -f github-trigger.yaml
cd ../
echo "\033[1;34mTekton Trigger setup complete.\033[0m\n"

echo "\033[1;34mWaiting for the EventListener Route to be Ready...\033[0m\n"
sleep 10
cd ../

GIT_URL="$(git config --get remote.origin.url)"
GIT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"

GIT_USER=$(echo $GIT_URL | cut -d '/' -f4)
GIT_REPO=$(echo $GIT_URL | cut -d '/' -f5 | cut -d '.' -f1)

ROUTE="http://$(oc get route mkdocs-build-listener-el -o jsonpath='{.spec.host}')"

echo "\033[1;34mUpdating GitHub Repository Details...\033[0m"
curl "https://api.github.com/repos/$GIT_USER/$GIT_REPO" \
-H "Authorization: token $GITPERSONALACCESSTOKEN" \
-d @- << EOF
{
    "description": "The documentation is hosted on the link below.",
    "homepage": "https://$GIT_USER.github.io/$GIT_REPO"
}
EOF
echo "\033[1;34mGitHub Repository Details updated successfully.\033[0m\n"

echo "\033[1;34mAdding Webhook to the GitHub Repo...\033[0m"
curl "https://api.github.com/repos/$GIT_USER/$GIT_REPO/hooks" \
-H "Authorization: token $GITPERSONALACCESSTOKEN" \
-d @- << EOF
{
    "name": "web",
    "active": true,
    "events": [
    "push"
    ],
    "config": {
    "url": "$ROUTE",
    "content_type": "json"
    }
}
EOF
echo "\033[1;34mWebhook added successfully.\033[0m\n"


echo "\033[1;32mTekton CI pipeline setup complete.\033[0m\n\
You can add/update/delete anything in the GitHub Repo:\033[1;36m$GIT_URL\033[0m and the Openshift pipeline will run automatically to build the docs and deploy it on \033[1;36m'https://$GIT_USER.github.io/$GIT_REPO'.\033[0m\n\
Do you want to trigger the pipeline to build mkdocs now? (y/n)\033[0m"
read -r answer
if [ "$answer" != "${answer#[Yy]}" ] ;then
    
    tkn pipeline start mkdocs-oc-pipeline \
    -p git-url=$GIT_URL \
    -p git-rev=$GIT_BRANCH \
    --use-param-defaults
else
    echo "\033[1;34mYou can run the pipeline later with the following command:\033[0m"
    echo "\033[1;36mtkn pipeline start mkdocs-oc-pipeline -p git-url=$GIT_URL -p git-rev=$GIT_BRANCH --use-param-defaults\033[0m\n"
fi

echo "\033[1;32m-----------Tekton CI setup complete-------------\033[0m\n"
