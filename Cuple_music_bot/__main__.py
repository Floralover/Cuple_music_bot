import requests
from pyrogram import Client as Bot

from Cuple_music_bot.config import API_HASH
from Cuple_music_bot.config import API_ID
from Cuple_music_bot.config import BG_IMAGE
from Cuple_music_bot.config import BOT_TOKEN
from Cuple_music_bot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Cuple_music_bot.modules"),
)

bot.start()
run()
