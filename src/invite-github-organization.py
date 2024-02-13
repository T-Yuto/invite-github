# pip install requests python-dotenv
from logger import logger
import sys

from conf import env
from team import get_team_ids
from invite import invite_organization


'''
Usage:
$ python invite-github-organization.py $EMAIL $ORG_NAME $TEAM_NAME,$TEAM_NAME2,...
'''

# ログの出力
logger.info('Start')
# チームのIDを取得する関数




def main():

    # チームのIDを取得
    team_ids = get_team_id(teams)

    # GitHub Organizationへの招待を送信
    invite(team_ids)


if __name__ == "__main__":
    main()


logger.info('End')
