#!/bin/bash

# Script to automate GitHub repository setup
# Usage: ./setup_git_repo.sh <repo_name> <public/private>

# Check if GitHub CLI (gh) is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed. Install it with: brew install gh"
    exit 1
fi

# Check if Git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Install it with: brew install git"
    exit 1
fi

# Check if arguments are provided
if [ "$#" -ne 2 ]; then
    echo "❌ Usage: ./setup_git_repo.sh <repo_name> <public/private>"
    exit 1
fi

# Assign command-line arguments
REPO_NAME=$1
PRIVACY=$2
DIR_NAME=${PWD##*/}  # Get current directory name

# Step 1: Initialize Git repository
echo "🚀 Initializing Git repository in '$DIR_NAME'..."
git init

# Step 2: Create .gitignore file
echo "📄 Creating .gitignore file..."
cat <<EOL > .gitignore
# Ignore Python virtual environments
venv/
.env/
*.venv
*.env

# Ignore Conda environments
conda_env/
env/

# Ignore common Python cache & logs
__pycache__/
*.pyc
*.pyo
*.log

# Ignore IDE and system files
.vscode/
.idea/
.DS_Store
EOL

# Step 3: Add & commit files
echo "✅ Staging and committing files..."
git add .
git commit -m "Initial commit"

# Step 4: Authenticate GitHub CLI
echo "🔑 Authenticating GitHub CLI..."
gh auth login

# Step 5: Create GitHub repository
echo "🌍 Creating GitHub repository '$REPO_NAME'..."
gh repo create "$REPO_NAME" --$PRIVACY --source=. --remote=origin

# Step 6: Push repository to GitHub
echo "⬆️ Pushing code to GitHub..."
git branch -M main
git push -u origin main

# Step 7: Confirm success
echo "🎉 Repository '$REPO_NAME' successfully created and pushed!"
echo "🔗 View it at: https://github.com/$(gh auth status --show-token | grep "Logged in to github.com as" | awk '{print $6}')/$REPO_NAME"