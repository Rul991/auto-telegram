from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv('API_ID') or input('api id: '))
API_HASH = getenv('API_HASH') or input('api hash')
PASSWORD = getenv('PASSWORD') or ''
PHONE = getenv('PHONE') or ''
APP_NAME = getenv('APP_NAME') or 'auto-telegram'

DELAY = 2