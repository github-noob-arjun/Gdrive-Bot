import os
import logging
from pyrogram import Client
from bot import (
  APP_ID,
  API_HASH,
  BOT_TOKEN,
  DOWNLOAD_DIRECTORY
  )

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

GdriveBot = Client(
    "G-DriveBot",
    bot_token=BOT_TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH
    # plugins=plugins,
    # parse_mode="markdown",
    # workdir=DOWNLOAD_DIRECTORY
)
