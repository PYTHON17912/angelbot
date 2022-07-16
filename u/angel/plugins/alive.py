from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

d3vil_pic = Config.ALIVE_PIC or "https://te.legra.ph/file/5963540f94376ddf8d1f7.jpg"
pm_caption = "  __**🔥🔥𝗗3𝗩𝗜𝗟 𝗕𝗢𝗧 𝗜𝗦 𝗔𝗟𝗜𝗩𝗘🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 ↼𝗠𝗔𝗦𝗧𝗘𝗥⇀\n  **『 {d3vil_mention} 』**\n\n"
)
pm_caption += f"╔══════════════════╗\n"
pm_caption += f"╠•➳➠ `𝖳𝖾𝗅𝖾𝗍𝗁𝗈𝗇:` `{tel_ver}` \n"
pm_caption += f"╠•➳➠ `𝖵𝖾𝗋𝗌𝗂𝗈𝗇:` `{d3vil_ver}`\n"
pm_caption += f"╠•➳➠ `𝖲𝗎𝖽𝗈:` `{is_sudo}`\n"
pm_caption += f"╠•➳➠ `𝖢𝗁𝖺𝗇𝗇𝖾𝗅:` [𝙹𝗈𝗂𝗇](https://t.me/im_angel_girl00)\n"
pm_caption += f"╠•➳➠ `𝖢𝗋𝖾𝖺𝗍𝗈𝗋:` [ᴀɴɢᴇʟ](https://t.me/im_angel_girl00)\n"
pm_caption += f"╠•➳➠ `𝖮𝗐𝗇𝖾𝗋:` [ᴀɴɢᴇʟ](https://t.me/im_angel_girl00)\n"
pm_caption += f"╚══════════════════╝\n"


#-------------------------------------------------------------------------------

@d3vilbot.on(d3vil_cmd(outgoing=True, pattern="alive$"))
@d3vilbot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(d3vil):
    if d3vil.fwd_from:
        return
    await d3vil.get_chat()
    await d3vil.delete()
    await bot.send_file(d3vil.chat_id, d3vil_pic, caption=pm_caption)
    await d3vil.delete()

msg = f"""
**⚡ 𝐃
"""
botname = Config.BOT_USERNAME

@d3vilbot.on(d3vil_cmd(pattern="d3vil$"))
@d3vilbot.on(sudo_cmd(pattern="d3vil$", allow_sudo=True))
async def d3vil_a(event):
    try:
        d3vil = await bot.inline_query(botname, "alive")
        await d3vil[0].click(event.chat_id)
        if event.sender_id == d3krish:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "d3vil", None, "Shows Inline Alive Menu with more details."
).add()
