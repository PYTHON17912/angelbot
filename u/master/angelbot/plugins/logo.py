import os
import random
import time

from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterDocument

from . import *


PICS_STR = []

@bot.on(angel_cmd(pattern=r"logo ?(.*)"))
@bot.on(sudo_cmd(pattern=r"logo ?(.*)", allow_sudo=True))
async def lg1(angelevent):
    event = await eor(angelevent, "`Processing.....`")
    fnt = await get_font_file(angelevent.client, "@angel_AND_MAFIA_FONTS")
    if angelevent.reply_to_msg_id:
        rply = await angelevent.get_reply_message()
        logo_ = await rply.download_media()
    else:
        async for i in bot.iter_messages("@angel_GFX_BG", filter=InputMessagesFilterPhotos):
    	    PICS_STR.append(i)
        pic = random.choice(PICS_STR)
        logo_ = await pic.download_media()
    text = angelevent.pattern_match.group(1)
    if len(text) <= 8:
        font_size_ = 160
        strik = 10
    elif len(text) >= 9:
        font_size_ = 50
        strik = 5
    else:
        font_size_ = 160
        strik = 20
    if not text:
        await eod(event, "**gιvε  sσмε тεxт тσ мαкε α ℓσgσ !!**")
        return
    img = Image.open(logo_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(fnt, font_size_)
    image_widthz, image_heightz = img.size
    w, h = draw.textsize(text, font=font)
    h += int(h * 0.21)
    image_width, image_height = img.size
    draw.text(
        ((image_width - w) / 2, (image_height - h) / 2),
        text,
        font=font,
        fill=(255, 255, 255),
    )
    w_ = (image_width - w) / 2
    h_ = (image_height - h) / 2
    draw.text(
        (w_, h_), text, font=font, fill="white", stroke_width=strik, stroke_fill="black"
    )
    file_name = "angelBot.png"
    img.save(file_name, "png")
    await bot.send_file(
        angelevent.chat_id,
        file_name,
        caption=f"**мα∂ε вү :** {angel_mention}\n ωιтн тнε нεℓρ σғ [∂3vιℓ вαcкgяσυη∂'s](t.me/im_angel_girl00)",
    )
    await event.delete()
    try:
        os.remove(file_name)
        os.remove(fnt)
        os.remove(logo_)
    except:
    	pass


async def get_font_file(client, channel_id):
    font_file_message_s = await client.get_messages(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        limit=None,
    )
    font_file_message = random.choice(font_file_message_s)

    return await client.download_media(font_file_message)


CmdHelp("logo").add_command(
  "logo", "<reply to pic + text> or <text>", "Makes a logo with the given text. If replied to a picture makes logo on that else gets random BG."
).add_info(
  "Logo Maker.\n**🙋🏻‍♂️ Note :**  Currently only supports custom pics. Fonts are choosen randomly."
).add()
