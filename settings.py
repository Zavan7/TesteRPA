import platform
import logging
import dotenv
import os

BASE_DIR = os.path.dirname(__file__)
BASE_NAME = os.path.basename(BASE_DIR)
LOG_FILE = os.path.join(BASE_DIR, f'{BASE_NAME}.log')
DOWLOADS_DIR = os.path.join(BASE_DIR, 'downloads')

config = dotenv.dotenv_values()

ENVIROMENT = config.get('ENVIROMENT', 'production')

if not os.path.exists(DOWLOADS_DIR):
    os.makedirs(DOWLOADS_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    encoding='utf-8',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s [module:(%(module)s) line:%(lineno)d]: %(message)s',  # noqa E501
    datefmt='%d-%m-%Y %H:%M',
)

logger = logging.getLogger(BASE_NAME)

DB_HOST = config.get('DB_HOST', 'localhost')
DB_PORT = int(config.get('DB_PORT', 27017))
DB_USERNAME = config.get('DB_USERNAME', 'root')
DB_PASSWORD = config.get('DB_PASSWORD', 'root')
DATABASE_NAME = config.get('DATABASE_NAME', 'automation_logs')

COMPUTERNAME = platform.node()
USERNAME_PC = os.getlogin()
