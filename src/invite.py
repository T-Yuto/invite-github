from logger import logger
from conf import env
import requests
from team import get_team_ids

ACCESS_TOKEN = env['ACCESS_TOKEN'] # 'ghp_XXXXXXXXXXXXXXXXXXXXXXXX'
org_name = env['org_name']         # 'my-org'
email = env['email']               # 'xxxxx@yyy.zz'
team_names = env['team_names']     # ['team1', 'team2', 'team3']

# GitHub Organizationへの招待を送信する関数
def send_organization_invitation() -> bool:
    '''
    GitHub Organizationへの招待を送信する関数
    :param team_ids: チームID [Number, Number, ...]
    :return: 成功した場合はTrue 失敗した場合はFalse
    Docs : https://docs.github.com/en/rest/orgs/members?apiVersion=2022-11-28#create-an-organization-invitation
    curl -L \
        -X POST \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer <YOUR-TOKEN>" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        https://api.github.com/orgs/ORG/invitations \
        -d '{"email":"octocat@github.com","role":"direct_member","team_ids":[12,26]}'
    '''
    url = f'https://api.github.com/orgs/{org_name}/invitations'
    team_ids = get_team_ids(team_names)
    headers = {
        'Authorization': f'token {ACCESS_TOKEN}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'Content-Type': 'application/json'
    }
    payload = {
        'email': email,
        'role': 'direct_member',
        'team_ids': team_ids
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        logger.info(f'Successfully invited {email} to the organization.')
        return True
    else:
        logger.error(f'Failed to invite {email} to the organization. Status code: {response.status_code}. Response: {response.text}')
        return False


def send_organization_team_invitation() -> bool:
    '''
    GitHub Organizationのチームへの招待を送信する関数
    :param team_ids: チームID [Number, Number, ...]
    :return: 成功した場合はTrue 失敗した場合はFalse
    '''
    pass

invite_organization = send_organization_invitation()