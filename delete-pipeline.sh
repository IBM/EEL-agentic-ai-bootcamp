#!/usr/bin/env sh

set -e

echo
echo "\033[1;31m---------------------Deleting Tekton CI---------------------\033[0m"
cd Openshift\ Pipeline/
echo
NAMESPACE=$(oc config view --minify -o jsonpath='{..namespace}')
echo "\033[1;37mUsing Openshift Project: $NAMESPACE\033[0m\n"

echo "\033[1;34mDeleting Tekton Tasks...\033[0m"
cd Tasks/
oc delete -f mkdocs-setup.yaml
oc delete -f mkdocs-lint.yaml
oc delete -f mkdocs-build-deploy.yaml
cd ../
echo "\033[1;34mTekton Tasks deleted successfully.\033[0m\n"

echo "\033[1;34mDeleting Tekton Pipeline...\033[0m"
cd Pipeline/
oc delete -f pipeline.yaml
cd ../
echo "\033[1;34mTekton Pipeline deleted successfully.\033[0m\n"

echo "\033[1;34mDeleting Tekton Secrets...\033[0m"
cd Secret/
oc delete -f github-credentials.yaml
cd ../
echo "\033[1;34mTekton Secrets deleted successfully.\033[0m\n"

echo "\033[1;34mDeleting Tekton Trigger...\033[0m"
cd Trigger/
oc delete -f github-trigger.yaml
cd ../
echo "\033[1;34mTekton Trigger deleted successfully.\033[0m\n"


cd ../
echo "\033[1;31m---------------Tekton CI deleted successfully---------------\033[0m\n"
