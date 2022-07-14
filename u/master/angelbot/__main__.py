import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from angelbot import LOGS, bot, tbot
from angelbot.config import Config
from angelbot.utils import load_module, start_assistant, load_addons
from angelbot.version import __angel__ as angelver
hl = Config.HANDLER
angel_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/5abfcff75e1930dcdfaf3.mp4"

LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)    

# let's get the bot ready
async def angel_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"angelBOT_SESSION - {str(e)}")
        sys.exit()


# Userbot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("༆𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 𝚄𝚂𝙴𝚁𝙱𝙾𝚃༆")
            bot.loop.run_until_complete(angel_bot(Config.BOT_USERNAME))
            LOGS.info("✵𝙳3𝚅𝙸𝙻𝙱𝙾𝚃 𝚂𝚃𝙰𝚁𝚃𝚄𝙿 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳✵")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "angelbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# Assistant.....
assistant = os.environ.get("ASSISTANT", None)
async def assistants():
    if assistant == "ON":
        path = "angelbot/assistant/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_assistant(shortname.replace(".py", ""))


bot.loop.run_until_complete(assistants())

# Extra Modules...
addon = os.environ.get("EXTRA_REPO", None)             
async def addons():
    if addon == "True":
        extra_repo = "https://t.me/im_angel_girl00"
        try:
            os.system(f"git clone {extra_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("🔱Loading Extra Plugin🔱")
        path = "angelADDONS/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"[angel-BOT 2.0] - Addons -  ✅Installed✅ - {shortname}")
                except Exception as e:
                    LOGS.warning(f"[angel-BOT 2.0] - Addons - ⚠️⚡ERROR⚡⚠️ - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Addons Not Loading")

bot.loop.run_until_complete(addons())

# let the party begin...
LOGS.info("➪𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 𝙱𝙾𝚃")
tbot.start()
LOGS.info(
    "𝖧𝖾𝖺𝖽 𝗍𝗈 @im_angel_girl00 𝖿𝗈𝗋 𝖴𝗉𝖺𝖽𝗍𝖾 𝖭𝖾𝗐. 𝖠𝗅𝗌𝗈 𝗃𝗈𝗂𝗇 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 to 𝗀𝖾𝗍 𝗎𝗉𝖽𝖺𝗍𝖾s."
)
LOGS.info("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

# that's life...
async def angel_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                angel_PIC,
                caption=f"ʟɛɢɛռɖaʀʏ ᴀғ Aɴɢᴇʟʙᴏᴛ\n\n**𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ➪ {angelver}**\n\n𝐓𝐲𝐩𝐞 `{hl}ping` or `{hl}alive` 𝐭𝐨 𝐜𝐡𝐞𝐜𝐤! \n\nJoin [ᴀɴɢᴇʟʙᴏᴛ](t.me/im_angel_girl00) for Updates & [ᴀɴɢᴇʟʙᴏᴛ](t.me/im_angel_girl00) 𝐟𝐨𝐫 𝐚𝐧𝐲 𝐪𝐮𝐞𝐫𝐲 𝐫𝐞𝐠𝐚𝐫𝐝𝐢𝐧𝐠 ᴀɴɢᴇʟʙᴏᴛ",
            )
    except Exception as e:
        LOGS.info(str(e))


    try:
        await bot(JoinChannelRequest("@im_angel_girl00"))
    except BaseException:
        pass


bot.loop.create_task(angel_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()


