import os
import logging
from pyrogram import Client

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

GdriveBot = Client(
      "G-DriveBot",
      bot_token="5318793234:AAHtik1DzBw7qpL_YZcWI_i3M9E1Noxm9w0",
      api_id="6015447",
      api_hash="0e96dd0dd4c4c9ded27c2ef58e6ab112"
)
