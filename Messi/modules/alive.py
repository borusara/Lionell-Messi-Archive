import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as x
from telethon import __version__ as y
from pyrogram import __version__ as z
from Messi.events import register
from Messi import telethn as tbot


PHOTO = "https://telegra.ph/file/9b2f5c511b0ecdfbabdcf.mp4"

@register(pattern=("awake messi"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Shoushuke Komi** \n\n"
  TEXT += "🗡 **I'm Working Properly** \n\n"
  TEXT += f"🗡 **My Masters : [Shoushuke creators](https://t.me/Knights_X_association/34)** \n\n"
  TEXT += f"🗡 **Library Version :** `{x}` \n\n"
  TEXT += f"🗡 **Telethon Version :** `{y}` \n\n"
  TEXT += f"🗡 **Pyrogram Version :** `{z}` \n\n"
  TEXT += "**⚽️ Thanks For Adding Me Here ⚽️**"
  BUTTON = [[Button.url("Help", "https://t.me/Messi_Probot?start=help"), Button.url("My Headquarters", "https://t.me/shoushuke_support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
