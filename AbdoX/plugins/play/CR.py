#_____كسمك تحياتي 
#_____@EU_TM

import asyncio
import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AbdoX import (Apple, Resso, Spotify, Telegram, YouTube, app)
from AbdoX import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://t.me/HQ_BX/5",
        caption=f"𝐖𝐞𝐥𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐁𝐨𝐝𝐚 𝐌𝐮𝐬𝐢𝐜",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐆𝐑𝐎𝐔𝐏", url=f"https://t.me/jx_xll"), 
                 InlineKeyboardButton(
                   " 𝐒𝐎𝐔𝐑𝐂𝐄",       url=f"https://t.me/l2_2Y"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "𝐀 𝐁 𝐃 𝐎", url=f"https://t.me/EU_TM"), 
                      
             ],[ 
                  InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك⚡",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )










@app.on_message(
    command(["بوده" , "فوديكا","مطور السورس"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("EU_TM")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"مــعلومـات مــطور الـسـورس \n\n 𝐃𝐄𝐕 :{name}\n\n 𝐔𝐒𝐄𝐑 :@{usr.username}\n\n 𝐈𝐃 :`{usr.id}`\n\n 𝐁𝐈𝐎 :{usr.bio}\n\n 𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


