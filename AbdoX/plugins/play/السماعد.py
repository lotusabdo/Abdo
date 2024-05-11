import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AbdoX import (Apple, Resso , Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from AbdoX import app
from AbdoX.misc import SUDOERS

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

ASS_US = getenv("ASS_US")

ASS_US = getenv("ASS_US")

ASS_ID = getenv("ASS_ID")




def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj



@app.on_message(
    command(["انضم","الحساب المساعد","حساب مساعد"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(ASS_ID)
    name = usr.first_name
    async for photo in client.iter_profile_photos(ASS_ID, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""❲ معلومات الحساب المساعد ❳
— — — — — — — — —
- اسم الحساب المساعد : [{usr.first_name}](https://t.me/{ASS_US})
- يوزر الحساب المساعد : @{ASS_US}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"tg://user?id={ASS_ID}")
                ],[
                    InlineKeyboardButton(
                        "࿈ ضيف الحساب المساعد لمجموعتك .", url=f"https://t.me/{ASS_US}?startgroup=true"),
                ],
            ]
        ),
    )
