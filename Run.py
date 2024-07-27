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


if __name__ == "__main__":
    if not os.path.isdir(DOWNLOAD_DIRECTORY):
        os.makedirs(DOWNLOAD_DIRECTORY)
    plugins = dict(
        root="bot/plugins"
    )
    GdriveBot = Client(
        "G-DriveBot",
        bot_token=BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins,
        parse_mode="markdown",
        workdir=DOWNLOAD_DIRECTORY
    )
    LOGGER.info('Starting Bot !')
    GdriveBot.run()
    LOGGER.info('Bot Stopped !')

#--------

WEB_SUPPORT = "True"

class Bot(Client):
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)

    def __init__(self):
        super().__init__(
            name="simple-renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=100,
            plugins={"root": "main"},
            sleep_threshold=10,
        )
    async def start(self):
        await super().start()
        me = await self.get_me()      
        print(f"{me.first_name} | @{me.username} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...⚡️")
        if WEB_SUPPORT:
            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", 8000).start()
            print("Web Response Is Running......🌍🌎🌏")
       
    async def stop(self, *args):
       await super().stop()      
       print("Bot Restarting........")

Bot().run()
