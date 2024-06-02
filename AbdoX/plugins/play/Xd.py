import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from AbdoX import (Apple, Resso, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest



@app.on_message(filters.command(["تفعيل التواصل","تعطيل التواصل"], ""))
async def byyye(client, message):
    user = message.from_user.username
    dev = await get_dev(client.me.username)
    if user in OWNER or message.from_user.id == dev:
        text = message.text
        if text == "تفعيل التواصل":
          if not client.me.username in OFFPV:
             await message.reply_text("♪ التواصل مفعل من قبل  💎 .")
          try:
            OFFPV.remove(client.me.username)
            await message.reply_text("♪ تم تفعيل التواصل  💎 .")
            return
          except:
             pass
        if text == "تعطيل التواصل":
          if client.me.username in OFFPV:
             await message.reply_text("♪ التواصل معطل من قبل  💎 .")
          try:
            OFFPV.append(client.me.username)
            await message.reply_text("♪ تم تعطيل التواصل  💎 .")

