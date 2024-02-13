from logger import logger
from conf import env
import requests
from team import get_team_ids

ACCESS_TOKEN = env['ACCESS_TOKEN'] # 'ghp_XXXXXXXXXXXXXXXXXXXXXXXX'
org_name = env['org_name']         # 'my-org'
email = env['email']               # 'xxxxx@yyy.zz'
team_names = env['team_names']     # ['team1', 'team2', 'team3']

def get_organization_members() -> list:
    '''
    GitHub Organizationのメンバーを取得する関数
    :return: メンバー情報 [login, login, ...]
    Docs : https://docs.github.com/en/rest/orgs/members?apiVersion=2022-11-28#list-organization-members

    Requests Example(cURL):
    curl -L \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer <YOUR-TOKEN>" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        https://api.github.com/orgs/ORG/members  <<<  url

    Response Example:
    [
        {
            "login": "octocat",  <<<  member['login']
            "id": 1,
            "node_id": "MDQ6VXNlcjE=",
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "gravatar_id": "",
            "url": "https://api.github.com/users/octocat",
            "html_url": "https://github.com/octocat",
            "followers_url": "https://api.github.com/users/octocat/followers",
            "following_url": "https://api.github.com/users/octocat/following{/other_user}",
            "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
            "organizations_url": "https://api.github.com/users/octocat/orgs",
            "repos_url": "https://api.github.com/users/octocat/repos",
            "events_url": "https://api.github.com/users/octocat/events{/privacy}",
            "received_events_url": "https://api.github.com/users/octocat/received_events",
            "type": "User",
            "site_admin": false
        }
    ]
    '''
    url = f'https://api.github.com/orgs/{org_name}/members'
    headers = {
        'Authorization': f'token {ACCESS_TOKEN}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        members = [member['login'] for member in response.json()]
    else:
        logger.error(f'Failed to get organization members. Status code: {response.status_code}. Response: {response.text}')
        members = []
    return members
