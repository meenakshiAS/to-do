#!/bin/bash
echo "Plugins have been updated, creating a pull request or modifying an existing one if it exists"
PR_TITLE="chore(jenkins): Updates Jenkins plugins"
EXISTING_PR=$(gh pr list --search "$PR_TITLE" --json number,headRefName)
EXISTING_PR_BRANCH=$(echo "$EXISTING_PR" | jq -r 'if (type=="array" and length > 0) then .[0].data.repository.pullRequests.nodes[0].headRefName else "" end')
if [ -z "$EXISTING_PR_BRANCH" ]; then
  git checkout -b "$BRANCH_NAME"
else
  
  git checkout "$EXISTING_PR_BRANCH"
fi
git add dockerfiles/plugins.txt
git commit --amend --no-edit
git push -u origin HEAD
if [ -z "$EXISTING_PR_BRANCH" ]; then
  gh pr create --title "$PR_TITLE" --body "This pull request updates the Jenkins plugins listed in \`plugins.txt\`." --base "$BASE_BRANCH" --head "$BRANCH_NAME"
fi
