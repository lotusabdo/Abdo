import asyncio

import random

from AbdoX import app

from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)


from pyrogram import filters, Client




txt = [


"ها عايز اي 🙄",
"ايوااا جااااي 😂",
"عاوزني اشقطلك مين يروحي 🥺",
"ايوة قول عاوز اي 🤔",
"قلب البوت 🥺",
"يعم تعبتنا معاك 🙁",
"استنا يعم بشقط وجايبك علطول 😂",
"بس يا شخه 😂",
"انت اهطل ياض 😁",
"انا قولت حمار محدش صدقني 😎",
"ياربي في اي 🤬",
"است طيب 😏",

        ]


        


@app.on_message(filters.command(["بوت","يا بوت"], ""), group=1442)

async def khyrok(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
