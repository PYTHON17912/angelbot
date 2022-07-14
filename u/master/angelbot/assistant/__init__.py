from . import *
from telethon import Button, custom

from angelbot import bot

from angelbot import *
OWNER_NAME = "{angel_mention}"
OWNER_ID = bot.uid


angel_USER = bot.me.first_name
d3krish = bot.uid

angel_mention = f"[{angel_USER}](tg://user?id={d3krish})"

angel_logo = "./resources/Pics/angelkrish_logo.jpg"
angel_logo1 = "./resources/Pics/angelkrish_logo.jpg"
angel_logo2 = "./resources/Pics/angelbot_logo.jpg"
angel_logo3 = "./resources/Pics/angelbot_logo.jpg"
angel_logo4 = "./resources/Pics/angelkrish_logo.jpg"
angelversion = "2.𝙾"

perf = "[ 𝚃𝙷𝙴 𝙳3𝚅𝙸𝙻𝙱𝙾𝚃 ]"


DEVLIST = [
    "1676629806"
]

async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
