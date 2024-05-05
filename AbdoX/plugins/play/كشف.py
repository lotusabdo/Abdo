import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AbdoX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AbdoX import app
from asyncio import gather






@app.on_message(command(["معلوماته", "كشف"]) & filters.group & ~filters.edited) 
async def hshs(client: Client, message: Message):      
    usr = await client.get_users(message.reply_to_message.from_user.id)
    name = usr.first_name#
    user_id = message.reply_to_message.from_user.id#
    chat_idd = message.chat.id#
    chat_username = f"@{message.chat.username}" #
    chat_name = message.chat.title#
    username = f"@{message.reply_to_message.from_user.username}"#
    async for photo in client.iter_profile_photos(message.reply_to_message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**[𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀](https://t.me/l2_2Y)\n\n🐉 ¦ ꪀᥲ️ꪔᥱ : {name}\n🤡 ¦ ᴜѕᴇ : {username}\n ¦ Ꭵَժ : `{user_id}`\n ¦ Ꭵժ ᥴ𝗁ᥲ️ƚ : `{chat_idd}`\n¦ 𝚌𝚑𝚊𝚝 : {chat_name}\n ¦ ᘜᖇ᥆υρ : {chat_username} \n**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.reply_to_message.from_user.username}")
                ],
            ]
        ),
    )     



@app.on_message(
    command(["بايو","البايو"])
    & filters.group
    & ~filters.edited
)
async def biio(client, message):
  nq = await client.get_chat(message.from_user.id)
  bio = nq.bio
  await message.reply_text(bio
  )
@app.on_message(
    command(["شخصيتي", "معلوماتي", "شخصيه"])
    & filters.group
    & ~filters.edited
)
async def ppdi(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**🐉 انـت »   {message.from_user.mention()} قلبي خد بالك**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
 
 
 
 


@app.on_message(command(["الكروب", "كروب"]) & filters.group & ~filters.edited)
async def ginnj(client: Client, message: Message):
    chat_idd = message.chat.id
    chat_name = message.chat.title
    chat_username = f"@{message.chat.username}"
    photo = await client.download_media(message.chat.photo.big_file_id)
    await message.reply_photo(photo=photo, caption=f"""**🔱 ¦ ꪀᥲ️ꪔᥱ » {chat_name}\n🐉 ¦ Ꭵժ ᘜᖇ᥆υρ »  -{chat_idd}\n🐊 ¦ ᥣᎥꪀk » {chat_username}**""",     
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        chat_name, url=f"https://t.me/{message.chat.username}")
                ],
            ]
        ),
    )
    
