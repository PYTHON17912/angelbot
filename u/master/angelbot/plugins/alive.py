from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

angel_pic = Config.ALIVE_PIC or "https://te.legra.ph/file/5963540f94376ddf8d1f7.jpg"
pm_caption = "  __**🔥🔥ᴀɴɢᴇʟ ʙᴏᴛ ɪꜱ ᴀʟɪᴠᴇ🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 ↼𝗠𝗔𝗦𝗧𝗘𝗥⇀\n  **『 {angel_mention} 』**\n\n"
)
pm_caption += f"╔══════════════════╗\n"
pm_caption += f"╠•➳➠ `𝖳𝖾𝗅𝖾𝗍𝗁𝗈𝗇:` `{tel_ver}` \n"
pm_caption += f"╠•➳➠ `𝖵𝖾𝗋𝗌𝗂𝗈𝗇:` `{angel_ver}`\n"
pm_caption += f"╠•➳➠ `𝖲𝗎𝖽𝗈:` `{is_sudo}`\n"
pm_caption += f"╠•➳➠ `𝖢𝗁𝖺𝗇𝗇𝖾𝗅:` [𝙹𝗈𝗂𝗇](https://t.me/im_angel_girl00)\n"
pm_caption += f"╠•➳➠ `𝖢𝗋𝖾𝖺𝗍𝗈𝗋:` [𝗔𝘆𝘂𝘀𝗵𝗮™](https://t.me/im_angel_girl00)\n"
pm_caption += f"╠•➳➠ `𝖮𝗐𝗇𝖾𝗋:` [𝗔𝘆𝘂𝘀𝗵𝗮™](https://t.me/im_angel_girl00)\n"
pm_caption += f"╚══════════════════╝\n"
pm_caption += " [⚡REPO⚡](https://t.me/im_angel_girl00) 🔹 [📜License📜](https://t.me/im_angel_girl00)"


#-------------------------------------------------------------------------------

@angelbot.on(angel_cmd(outgoing=True, pattern="alive$"))
@angelbot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(angel):
    if angel.fwd_from:
        return
    await angel.get_chat()
    await angel.delete()
    await bot.send_file(angel.chat_id, angel_pic, caption=pm_caption)
    await angel.delete()

msg = f"""
**⚡ ᴀɴɢᴇʟ ʙᴏᴛ ɪꜱ ᴏɴʟɪɴᴇ ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**↼𝗠𝗔𝗦𝗧𝗘𝗥⇀   :**  **『{angel_mention}』**
**╔══════════════════╗**
**╠➳➠ ᴛᴇʟᴇᴛʜᴏɴ :**  `{tel_ver}`
**╠➳➠ ᴀɴɢᴇʟʙᴏᴛ  :**  **{angel_ver}**
**╠➳➠ ᴜᴩᴛɪᴍᴇ   :**  `{uptime}`
**╠➳➠ ᴀʙᴜꜱᴇ    :**  **{abuse_m}**
**╠➳➠ ꜱᴜᴅᴏ      :**  **{is_sudo}**
**╚══════════════════╝
"""
botname = Config.BOT_USERNAME

@angelbot.on(angel_cmd(pattern="angel$"))
@angelbot.on(sudo_cmd(pattern="angel$", allow_sudo=True))
async def angel_a(event):
    try:
        angel = await bot.inline_query(botname, "alive")
        await angel[0].click(event.chat_id)
        if event.sender_id == d3krish:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "angel", None, "Shows Inline Alive Menu with more details."
).add()
