import random
from AbdoX import app
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus


def Who(m, user_id):
  user = m.chat.get_member(user_id)
  if user.status == ChatMemberStatus.OWNER:
    return "المالك"
  elif user.status == ChatMemberStatus.ADMINISTRATOR:
    return "مشرف"
  elif user.status == ChatMemberStatus.MEMBER:
    return "العضو"

@app.on_message(filters.command("كشف", "") & filters.group)
def jabwa(c, m):
  name = m.reply_to_message.from_user.first_name
  id = m.reply_to_message.from_user.id
  user = m.reply_to_message.from_user.username
  rank = f"{Who(m,m.reply_to_message.from_user.id)}"
  money = random.randint(1, 100)
  Text =f"""
⌯𝐍𝐚𝐦𝐞 «» {name}
⌯𝐈𝐝 «» {id}
⌯𝐔𝐬𝐞𝐫 «» {user}
⌯𝐑𝐚𝐧𝐤 «» {rank}
⌯𝐌𝐨𝐧𝐞𝐲 «» {money} جنيه 😂❤️"""
  return m.reply(Text)

