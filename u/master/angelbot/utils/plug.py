import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from angelbot import *
from angelbot.helpers import *
from angelbot.config import *
from angelbot.utils import *


# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from angelbot.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import angelbot.utils

        path = Path(f"angelbot/plugins/{shortname}.py")
        name = "angelbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("𝚃𝙴𝙰𝙼 𝙳3𝚅𝙸𝙻 - 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙸𝙼𝙿𝙾𝚁𝚃𝙴𝙳 " + shortname)
    else:
        import angelbot.utils

        path = Path(f"angelbot/plugins/{shortname}.py")
        name = "angelbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.tgbot = bot.tgbot
        mod.command = command
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = angelbot.utils
        mod.Config = Config
        mod.borg = bot
        mod.angelbot = bot
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_angel = delete_angel
        mod.eod = delete_angel
        mod.Var = Config
        mod.admin_cmd = angel_cmd
        mod.angel_cmd = angel_cmd
        # support for other userbots
        sys.modules["userbot.utils"] = angelbot.utils
        sys.modules["userbot"] = angelbot
        # support for paperplaneextended
        sys.modules["userbot.events"] = angelbot
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["angelbot.plugins." + shortname] = mod
        LOGS.info("✘ 𝚃𝙴𝙰𝙼 𝐃3𝚅𝙸𝙻 ✘  - 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙸𝙼𝙿𝙾𝚁𝚃𝙴𝙳 " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"angelbot.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError

#Assistant
def start_assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"angelbot/assistant/{shortname}.py")
        name = "angelbot.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Starting Your Assistant Bot.")
        print("Assistant Sucessfully imported " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"angelbot/assistant/{shortname}.py")
        name = "angelbot.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = bot.tgbot
        spec.loader.exec_module(mod)
        sys.modules["angelbot.assistant" + shortname] = mod
        print("Assistant Has imported " + shortname) 

#Assistant
def start_assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"angelbot/assistant/{shortname}.py")
        name = "angelbot.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Starting Your Assistant Bot.")
        print("Assistant Sucessfully imported " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"angelbot/assistant/{shortname}.py")
        name = "angelbot.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = bot.tgbot
        spec.loader.exec_module(mod)
        sys.modules["angelbot.assistant" + shortname] = mod
        print("[⚡Assistant⚡ 2.0] ~ HAS ~ •Installed۝۝"+ shortname)  

#Addons...

def load_addons(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import userbot.utils
        import sys
        import importlib
        from pathlib import Path
        path = Path(f"angelADDONS/{shortname}.py")
        name = "angelADDONS.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("♦️Extra Plugin♦️ ~ " + shortname)
    else:
        import userbot.utils
        import sys
        import importlib
        from pathlib import Path
        path = Path(f"angelADDONS/{shortname}.py")
        name = "angelADDONS.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
#        mod.angel = angel
        mod.bot = bot
        mod.bot = bot
        mod.command = command
        mod.borg = bot
        mod.angelbot = bot
        mod.tgbot = bot.tgbot
        mod.Var = Config
        mod.Config = Config
        mod.edit_or_reply = edit_or_reply
        mod.delete_angel = delete_angel
        mod.eod = delete_angel
        mod.admin_cmd = angel_cmd
        mod.logger = logging.getLogger(shortname)
        # support for angelBOT originals
#        sys.modules["userbot.utils"] = angelbot.utils
#        sys.modules["userbot"] = angelbot
        # support for paperplaneextended
#        sys.modules["userbot.events"] = angelbot
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["angelADDONS." + shortname] = mod
        LOGS.info("🔱Extra Plugin🔱 ~ " + shortname)
#angelbot
