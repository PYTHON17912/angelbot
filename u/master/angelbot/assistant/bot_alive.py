from telethon import events
from . import *
#from angelbot import YOUR_NAME
from angelbot import bot

angel_USER = bot.me.first_name
d3krish = bot.uid
angel_mention = f"[{angel_USER}](tg://user?id={d3krish})"

angel_pic = Config.ALIVE_PIC or "https://telegra.ph/file/5abfcff75e1930dcdfaf3.mp4"
pm_caption = "  __**🔥🔥Aɴɢᴇʟʙᴏᴛ 𝗔𝗦𝗦𝗜𝗦𝗧𝗔𝗡𝗧 𝗜𝗦 𝗔𝗟𝗜𝗩𝗘🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 ↼𝗠𝗔𝗦𝗧𝗘𝗥⇀\n  **『 {angel_mention} 』**\n\n"
)
pm_caption += f"╔══════════════════╗\n"
pm_caption += f"╠•➳➠ `𝖳𝖾𝗅𝖾𝗍𝗁𝗈𝗇:` `1.23.0` \n"
pm_caption += f"╠•➳➠ `𝖵𝖾𝗋𝗌𝗂𝗈𝗇:` `2.0.6`\n"
pm_caption += f"╠•➳➠ `𝖢𝗁𝖺𝗇𝗇𝖾𝗅:` [𝙹𝗈𝗂𝗇](https://t.me/im_angel_girl00)\n"
pm_caption += f"╠•➳➠ `𝖢𝗋𝖾𝖺𝗍𝗈𝗋:` [⋆𝗔𝘆𝘂𝘀𝗵𝗮™⋆](https://t.me/im_angel_girl00)\n"
pm_caption += f"╠•➳➠ `𝖮𝗐𝗇𝖾𝗋:` [⋆𝗔𝘆𝘂𝘀𝗵𝗮™⋆](https://t.me/im_angel_girl00)\n"
pm_caption += f"╚══════════════════╝\n"
pm_caption += " [⚡REPO⚡](https://github.com/TEAM-angel/angelBot) 🔹 [📜License📜](https://github.com/TEAM-angel/angelBot/blob/main/LICENSE)"

@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, angel_pic, caption=pm_caption)
