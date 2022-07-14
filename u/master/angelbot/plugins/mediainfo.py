import os

from . import *


@bot.on(angel_cmd(pattern="mediainfo$"))
@bot.on(sudo_cmd(pattern="mediainfo$", allow_sudo=True))
async def mediainfo(event):
    angel_MEDIA = None
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "Reply to a media to fetch info...")
    if not reply.media:
        return await eod(event, "Reply to a media file to fetch info...")
    angel = await eor(event, "`Fetching media info...`")
    angel_MEDIA = reply.file.mime_type
    if not angel_MEDIA:
        return await angel.edit("Reply to a media file to fetch info...")
    elif angel_MEDIA.startswith(("text")):
        return await angel.edit("Reply to a media file to fetch info ...")
    d3vl_ = await mediadata(reply)
    file_path = await reply.download_media(Config.TMP_DOWNLOAD_DIRECTORY)
    out, err, ret, pid = await runcmd(f"mediainfo '{file_path}'")
    if not out:
        out = "Unknown Format !!"
    paster = f"""
<h2>📃 MEDIA INFO 📃</h2>
<code>
{d3vl_}
</code>
<h2>🧐 MORE DETAILS 🧐</h2>
<code>
{out} 
</code>"""
    paste = await telegraph_paste(f"{angelL_MEDIA}", paster)
    await angel.edit(f"📌 Fetched  Media Info Successfully !! \n\n**Check Here :** [{angel_MEDIA}]({paste})")
    os.remove(file_path)

CmdHelp("mediainfo").add_command(
  "mediainfo", "<reply to a media>", "Fetches the detailed information of replied media."
).add()
