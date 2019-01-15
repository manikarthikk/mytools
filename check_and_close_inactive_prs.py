from github import Github
from datetime import datetime

def github_credentials(token):
    return Github(token)

def create_commit_and_close_pr(pr, message):
    pr.create_issue_comment(message)
    pr.edit(state='closed')

def get_all_repos_for_organization(git, org):
    r = git.get_organization(org)
    repos =  r.get_repos()
    all_repos_list = []
    for each_repo in repos:
        all_repos_list.append(each_repo)
    return all_repos_list

def is_pr_inactive(pr, number_of_days):
    # Returns True if the Pull request created date is greater than provided number of days 
    if abs((pr.created_at - datetime.now()).days) > number_of_days:
        return True
    else:
        return False

def main():
    token = 'relace_with_your_githubtoken'
    git = github_credentials(token)
    number_of_days = 1
    commit_message = 'Closing due to inactivity. re-open at anytime to proceed with original request'
    github_org = 'YourGithubOrgName'
    # Iterate through  all the repositories for a provided org and commit and close based on inactivity days
    all_repos = get_all_repos_for_organization(git, github_org)
    for each_repo in all_repos:
        get_repo_prs = each_repo.get_pulls()
        for each_pr in get_repo_prs:
            if is_pr_inactive(each_pr, number_of_days):
                create_commit_and_close_pr(each_pr, commit_message)

main()
