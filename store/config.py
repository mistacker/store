import os

DEBUG = True
SECRET_KEY = os.urandom(24)
DB_URI = "sqlite:///store.sql"
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

SESSION_NAME = "youGuess"

MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = '2584688424@qq.com'
MAIL_PASSWORD = 'heegkqckptljecde'
MAIL_DEFAULT_SENDER = '2584688424@qq.com'


GOODS_COUNT = "all_goods_count"
MODULE_COUNT = "all_module_count"
MODULE_NAME = "save_module_name"
