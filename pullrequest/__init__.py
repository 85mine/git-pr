from github import Github, BadCredentialsException

# First create a Github instance:
# Using username and password

username, password = "xxx", "xxx"

if not username:
    print('username is required.')
    exit(1)
if not password:
    print('password is required.')
    exit(1)

g = Github(username, password)

# Define base params
base_branch = 'master'
head_branch = 'create_pull_request_template'
pull_request_title = "Create pull request template"
pull_request_body = ""


def create_pull_request(re, title, body, base, head):
    # Check pull request exist
    pulls = re.get_pulls(state='open', sort='created', base=base_branch, head=username + ":" + head_branch)
    pulls_count = len(list(pulls))
    if pulls_count == 0:
        pull_request = re.create_pull(title, body, base, head, True)
    elif pulls_count == 1:
        pull_request = pulls[0]
        pull_request.edit(title, body, 'open', base)
    else:
        RuntimeError("More than one pull request")
    return pull_request


for repo in g.get_user().get_repos():
    # Create pull request
    try:
        pull = create_pull_request(repo, pull_request_title, pull_request_body, base_branch, head_branch)
        print(pull.html_url)
    except Exception as e:
        pass
