#!/usr/local/bin/python
from github3 import login
import requests

usernames = []
repo_names = []
SLACK_APP_HOOK = ""
ORG = ""
GITHUB_TOKEN = ""

def get_pulls(org):
    results = []

    for repo in org.repositories():
        if repo.name in repo_names
            for pr in repo.pull_requests():
                if pr.state == 'open':
                    results.append(pr)

    return results

def format_prs(prs):
    lines = []
    for p in prs:
        creater = p.user.login
        reviewers = []
        for r in p.requested_reviewers:
            if r.get('login') in usernames:
                reviewers.append(r.get('login'))
            else:
                next
        line = '*[<{0}|{1} - by {2} - requested reviewers: {3}>]'.format(
                p.html_url, p.title, creater, ', '.join(reviewers))
        lines.append(line)

    return lines


def get_users(gh):
    users = []
    for username in usernames:
        users.append(gh.user(username))
    return users

def send_to_slack(prs):
    text = 'These are the PRs ready for review: \n' + '\n'.join(prs)
    load = {
        'text': text
    }

    response = requests.post(SLACK_APP_HOOK, json=load)

gh= login(token=GITHUB_TOKEN)
org = gh.organization(ORG)
users = get_users(gh)
prs = get_pulls(org)
prs = format_prs(prs)
send_to_slack(prs)
