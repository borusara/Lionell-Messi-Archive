import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as x
from telethon import __version__ as y
from pyrogram import __version__ as z
from Messi.events import register
from Messi import telethn as tbot


PHOTO = "https://telegra.ph/file/c6df4d4c432a2f178bc2f.mp4"

@register(pattern=("awake shoushuke"))
@register(pattern=("Awake shoushuke"))
@register(pattern=("Awake Komi"))
@register(pattern=("/awake"))
@register(pattern=("/alive"))
          
          


async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Shoushuke Komi** \n\n"
  TEXT += "🗡 **I'm Working Properly** \n\n"
  TEXT += f"🗡 **My Developers : [Shoushuke creators](https://t.me/shoushuke_updates/3)** \n\n"
  TEXT += f"🗡 **Library Version :** `{x}` \n\n"
  TEXT += f"🗡 **Telethon Version :** `{y}` \n\n"
  TEXT += f"🗡 **Pyrogram Version :** `{z}` \n\n"
  TEXT += "**🗿 Thanks For Adding Me Here 🗿**"
  BUTTON = [[Button.url("Help", "https://t.me/shoushuke_komi_bot?start=help"), Button.url("My Headquarters", "https://t.me/shoushuke_support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
