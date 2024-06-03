from pyrogram import Client
from pyrogram import filters
from AbdoX import app

@app.on_message(filters.text)
async def delete_text(client, message):
    word_list = ["سكس", "كسمك","خول","متناك"]
    if message.text in word_list:
        await client.delete_messages(message.chat.id, message.id)
        await client.send_message(message.chat.id, f"ممنوع السب هنا {message.from_user.first_name}")
