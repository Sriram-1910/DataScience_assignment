import os
import git
from datasets import load_dataset

# Load dataset
dataset = load_dataset("universal_dependencies", "en_gum")
sample = dataset['train'][0]

# Display a sample sentence
print("Sentence:", " ".join([token['form'] for token in sample['tokens']]))
print("POS Tags:", sample['upos'])
print("Dependencies:", sample['deprel'])

# Setup Git Repository
repo_name = "DataScience_assignment"
repo_url = "https://github.com/Sriram-1910/DataScience_assignment.git"
local_path = f"/content/{repo_name}"
if not os.path.exists(local_path):
    repo = git.Repo.init(local_path)
    repo.create_remote('origin', repo_url)
else:
    repo = git.Repo(local_path)

os.chdir(local_path)

# Save output to file
with open("dependency_parsing_output.txt", "w") as f:
    f.write("Sentence: " + " ".join([token['form'] for token in sample['tokens']]) + "\n")
    f.write("POS Tags: " + str(sample['upos']) + "\n")
    f.write("Dependencies: " + str(sample['deprel']) + "\n")

# Commit and push to GitHub
repo.git.add(all=True)
repo.index.commit("Added Dependency Parsing Project")
repo.git.push("origin", "main")

print("✅ Successfully pushed to GitHub!")
