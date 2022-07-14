import re
from . import *

# Credits goes to developer of angelBot.
# This is  first plugin that he made when he released first angelBot.
# Modified to work in groups with inline mode disabled.
# Added error msg if no voice is found.
# So please dont remove credit. 
# You can use it in your repo. But dont remove these lines...
#Now this plugin on angel BOT

@bot.on(angel_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(angelkrish):
    angel = angelkrish.pattern_match.group(1)
    if not angel:
        if angelkrish.is_reply:
            (await angelkrish.get_reply_message()).message
        else:
            await edit_or_reply(angelkrish, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(angel))}")
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
    	await eod(angelkrish, "**Error 404:**  Not Found")
    	
@bot.on(angel_cmd(pattern="meev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="meev(?: |$)(.*)", allow_sudo=True))
async def nope(angelkrish):
    angel = angelkrish.pattern_match.group(1)
    if not angel:
        if angelkrish.is_reply:
            (await angelkrish.get_reply_message()).message
        else:
            await edit_or_reply(angelkrish, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("Myinstantsbot", f"{(deEmojify(angel))}")
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
    	await eod(angelkrish, "**Error 404:**  Not Found")


CmdHelp("memevoice").add_command(
	"mev", "<query>", "Searches the given meme and sends audio if found."
).add_command(
	"meev", "<query>", "Same as {hl}mev"
).add()
