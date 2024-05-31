from pyrogram import filters, Client
from AbdoX import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AbdoX.core.call import Alina
from AbdoX.utils.database import *
from pytgcalls.exceptions import NoActiveGroupCall,TelegramServerError 

@app.on_message(filters.regex("اسم المساعد"))
async def tom_name(client, message):
    assistant = await group_assistant(Alina, message.chat.id)
    await message.reply("ارسل اسم المساعد الجديد:")
    try:
        new_name = await client.ask(message.chat.id, "اكتب اسم المساعد الجديد:")
        await assistant.update_profile(first_name=new_name)
        await message.reply(f"تم تغيير اسم المساعد الى {new_name}")
    except Exception as e:
        await message.reply("حدث خطأ اثناء تغيير اسم المساعد!")
