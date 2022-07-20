import os
import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from bot.config import config

BOT_TOKEN = config.BOT_TOKEN
APP_ID = config.APP_ID
API_HASH = config.API_HASH
DATABASE_URL = config.DATABASE_URL
SUDO_USERS = config.SUDO_USERS
SUPPORT_CHAT_LINK = config.SUPPORT_CHAT_LINK
DOWNLOAD_DIRECTORY = config.DOWNLOAD_DIRECTORY
SUDO_USERS = config.SUDO_USERS # list(set(int(x) for x in SUDO_USERS.split()))
