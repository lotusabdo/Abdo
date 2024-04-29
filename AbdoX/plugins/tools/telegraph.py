from telegraph import upload_file
from pyrogram import filters
from AbdoX  import app
from pyrogram.types import InputMediaPhoto
from strings.filters import command

@app.on_message(command(["/tgm" , "تلجراف", "ميديا"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("**𝐌𝙰𝙺𝙴 𝐀 𝐋𝙸𝙽𝙺...**")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'**•⎆┊تم انشاء رابط الوسائط🕷** {url}')


