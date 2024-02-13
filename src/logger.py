import logging

def setup_logger():
    # ロガーの作成
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # ログフォーマット
    formatter = logging.Formatter('''{time: %(asctime)s,Name: %(name)s,Level:%(levelname)s,Message: %(message)s}''')

    # コンソールハンドラの設定
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger

# ロガーのインスタンス化
logger = setup_logger()
