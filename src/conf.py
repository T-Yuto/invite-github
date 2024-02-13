import os
from dotenv import load_dotenv
import argparse
from logger import logger


def load_env() -> str:
    '''
    環境変数を読み込む関数
    :return: {
        ACCESS_TOKEN: str,
    }
    '''
    logger.info('Loading environment variables')
    load_dotenv()
    ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN') | ''
    return {
        'ACCESS_TOKEN': ACCESS_TOKEN,
    }

def parse_args() -> argparse.Namespace:
    '''
    コマンドライン引数をパースする関数
    :return: argparse.Namespace
    '''
    parser = argparse.ArgumentParser('Send invitation to GitHub Organization')
    parser.add_argument('email', help='招待するユーザのメールアドレス (例: xxxx@yyy.zz)')
    parser.add_argument('org_name', help='GitHub Organization名 (例: my-org)')
    parser.add_argument('org_role', help='GitHub Organizationの役割 (例: direct_member or admin or billing_manager or hirer)')
    parser.add_argument('team_names', help='GitHub Organizationのチーム名 カンマ区切り (例: team1,team2,team3)')
    return parser.parse_args()

def set_params() -> dict:
    '''
    設定を読み込む関数
    :return: dict
    '''
    logger.info('Loading parameters')

    try:
        args = parse_args()
    except Exception as e:
        logger.error(f'Failed to parse arguments. {e}')
        exit(1)
    
    # 引数のチェック
    if args.email == '' \
    or args.org_name == '' \
    or args.team_names == '':
        logger.error('Invalid arguments provided. Please provide email, org_name and team_names. See --help for more information.')
        exit(1)
    
    return {
        'email': args.email,
        'org_name': args.org_name,
        'org_role': args.org_role | 'direct_member',
        'team_names': args.team_names.split(','),
    }


# 環境変数の読み込み
env = load_env() 
params = set_params()