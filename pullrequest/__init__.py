from github import Github

# First create a Github instance:
# Using username and password
g = Github("dienncrelipa", "dienncrelipa2018")

# Get repo
repo = g.get_repo("dienncrelipa/test")

# Define base params
base_branch = 'master'
head_branch = 'create_pull_request_template'

# Create pull request

pulls = repo.get_pulls(state='open', sort='created', base='master', )

pull_request = repo.create_pull("title","body","master","devff",True)

print(repo(pull_request.number))
