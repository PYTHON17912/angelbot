import cv2
import os
import io
import random
import shutil
import re
import textwrap
import lottie

from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps

from . import *


path = "./angelmify/"
if not os.path.isdir(path):
    os.makedirs(path)


@bot.on(angel_cmd(pattern="mmf ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mmf ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eod(event, "You need to reply to an image with .mmf` 'text on top' ; 'text on bottom'")
        return
    await eor(event, "🤪 **Memifying...**")
    reply = await event.get_reply_message()
    imgs = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(imgs) 
    tal, semx = img.read()
    cv2.imwrite("angelkrish.webp", semx)
    text = event.pattern_match.group(1)
    webp_file = await draw_meme_text("angelkrish.webp", text)
    await event.client.send_file(
        event.chat_id, webp_file, reply_to=event.reply_to_msg_id
    )
    await event.delete()
    shutil.rmtree(path)
    os.remove("angelkrish.webp")
    os.remove(webp_file)


@bot.on(angel_cmd(pattern="mms ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mms ?(.*)", allow_sudo=True))
async def sed(angelboy):
    if angelboy.fwd_from:
        return
    if not angelboy.reply_to_msg_id:
        await eod(angelboy, "You need to reply to an image with .mms` 'text on top' ; 'text on bottom'")
        return
    await eor(angelboy, "🤪 **Memifying...**")
    reply = await angelboy.get_reply_message()
    imgs = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(imgs) 
    tal, semx = img.read()
    cv2.imwrite("angelkrish.webp", semx)
    text = angelboy.pattern_match.group(1)
    photo = await draw_meme("angelkrish.webp", text)
    await angelboy.client.send_file(
        angelboy.chat_id, photo, reply_to=angelboy.reply_to_msg_id
    )
    await angelboy.delete()
    shutil.rmtree(path)
    os.remove("angelkrish.webp")
    os.remove(photo)
    
@bot.on(angel_cmd(pattern="doge(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="doge(?: |$)(.*)", allow_sudo=True))
async def nope(angelkrish):
    angel = angelkrish.pattern_match.group(1)
    if not angel:
        if angelkrish.is_reply:
            (await angelkrish.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(angelkrish, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(angelkrish, "Doge need some text to make sticker.")

    troll = await bot.inline_query("DogeStickerBot", f"{(deEmojify(angel))}")
    if troll:
        await angelkrish.delete()
        d3vl_ = await troll[0].click(Config.LOGGER_ID)
        if d3vl_:
            await bot.send_file(
                angelkrish.chat_id,
                d3vl_,
                caption="",
            )
        await d3vl_.delete()
    else:
     await eod(angelkrish, "Error 404:  Not Found")
     
@bot.on(angel_cmd(pattern="gg(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="gg(?: |$)(.*)", allow_sudo=True))
async def nope(angelkrish):
    angel = angelkrish.pattern_match.group(1)
    if not angel:
        if angelkrish.is_reply:
            (await angelkrish.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(angelkrish, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(angelkrish, "I need some text to make sticker.")

    troll = await bot.inline_query("GooglaxBot", f"{(deEmojify(angel))}")
    if troll:
        await angelkrish.delete()
        d3vl_ = await troll[0].click(Config.LOGGER_ID)
        if d3vl_:
            await bot.send_file(
                angelkrish.chat_id,
                d3vl_,
                caption="",
            )
        await d3vl_.delete()
    else:
     await eod(angelkrish, "Error 404:  Not Found")
    

CmdHelp("memify").add_command(
  "mmf", "<reply to a img/stcr/gif> <upper text> ; <lower text>", "Memifies the replied image/gif/sticker with your text and sends output in sticker format.", "mmf <reply to a img/stcr/gif> hii ; hello"
).add_command(
  "mms", "<reply to a img/stcr/gif> <upper text> ; <lower text>", "Memifies the replied image/gif/sticker with your text and sends output in image format.", "mms <reply to a img/stcr/gif> hii ; hello"
).add_command(
  "gg", "<text>", "Make gogle search Sticker."
).add_command(
  "doge", "<text>", "Makes A Sticker of Doge with given text."
).add()
