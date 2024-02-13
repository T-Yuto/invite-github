import requests
from logger import logger
from conf import env

org_name = env['org_name']
ACCESS_TOKEN = env['ACCESS_TOKEN']

def get_team_id(team_name: str) -> int:
    '''
    GitHub OrganizationのチームIDを取得する関数
    :param org_name: GitHub Organization名
    :param team_name: チーム名
    :return: チームID Int (0 if not found)
    Docs : https://docs.github.com/en/rest/teams/teams?apiVersion=2022-11-28#list-teams
    gh api \
        -H "Accept: application/vnd.github+json" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        /orgs/ORG/teams
    '''
    url = f'https://api.github.com/orgs/{org_name}/teams'
    headers = {
        'Authorization': f'token {ACCESS_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        teams = response.json()
        team_id=next((team['id'] for team in teams if team['name'] == team_name), 0)
    else:
        logger.error(f'Failed to get teams. Status code: {response.status_code}. Response: {response.text}')
        team_id = 0
    return team_id


def get_team_ids(team_names: list) -> list: # [Number, Number, ...]
    '''
    GitHub OrganizationのチームIDを取得する関数
    :param org_name: GitHub Organization名
    :param team_name: チーム名
    :return: チームID
    '''
    return [team_id for team_name in team_names if (team_id := get_team_id(team_name))>0]
