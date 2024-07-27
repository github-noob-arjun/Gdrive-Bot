from pyrogram import Client
from bot.config import *
import os
from aiohttp import web
from bot.web import web_server

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
