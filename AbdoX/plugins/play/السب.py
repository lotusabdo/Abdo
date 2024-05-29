import random
from config import *
from AbdoX import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatMemberStatus


def Who(m, user_id):
  user = m.chat.get_member(user_id)
  if user.status == ChatMemberStatus.OWNER:
    return "المالك"
  elif user.status == ChatMemberStatus.ADMINISTRATOR:
    return "مشرف"
  elif user.status == ChatMemberStatus.MEMBER:
    return "العضو"

forward = []
cursing = []
mute = []
 

@app.on_message(filters.command("قفل الدردشه", "") & filters.group)
def of_chat(c, m):
  idchat = m.chat.id
  mention = m.from_user.mention
  a = c.get_chat_member(m.chat.id, m.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not m.from_user.id == OWNER_ID:
    return m.reply("يجب انت تكون ادمن للقيام بذلك •")
  c.set_chat_permissions(idchat, ChatPermissions())
  m.reply(f"• تم قفل الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command("فتح الدردشه", "") & filters.group)
def on_chat(c, m):
  idchat = m.chat.id
  mention = m.from_user.mention
  a = c.get_chat_member(m.chat.id, m.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not m.from_user.id == OWNER_ID:
    return m.reply("يجب انت تكون ادمن للقيام بذلك •")
  c.set_chat_permissions(idchat, ChatPermissions(can_send_messages=True, can_send_media_messages=True))
  m.reply(f"• تم فتح الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command("قفل السب ", "") & filters.group)
def of_cursing(c, m):
  idchat = m.chat.id
  name = m.from_user.mention
  a = c.get_chat_member(m.chat.id, m.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not m.from_user.id == OWNER_BOT:
    return m.reply("يجب انت تكون ادمن للقيام بذلك •")
  cursing.append(idchat)
  m.reply(f"• تم قفل السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("فتح السب ", "") & filters.group)
def on_cursing(c, m):
  idchat = m.chat.id
  name = m.from_user.mention
  a = c.get_chat_member(m.chat.id, m.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not m.from_user.id == OWNER_BOT:
    return m.reply("يجب انت تكون ادمن للقيام بذلك •")
  cursing.remove(idchat)
  m.reply(f"• تم فتح السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("قفل التوجيه ", "") & filters.group)
def of_forward(c, m):
  idchat = m.chat.id
  name = m.from_user.mention
  a = c.get_chat_member(m.chat.id, m.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not m.from_user.id == OWNER_BOT:
    return m.reply("يجب انت تكون ادمن للقيام بذلك •")
  forward.append(idchat)
  m.reply(f"• تم قفل التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command("فتح التوجيه ", "") & filters.group)
def on_forward(c, m):
  idchat = m.chat.id
  name = m.from_user.mention
  a = c.get_chat_member(m.chat.id, m.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not m.from_user.id == OWNER_ID:
    return m.reply("يجب انت تكون ادمن للقيام بذلك •")
  forward.remove(idchat)
  m.reply(f"• تم فتح التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.text & filters.group)
def msg(c, m):
  text = m.text
  idchat = m.chat.id

  if m.from_user.id in mute:
    m.delete()

  insults = ["كس","كسمك","كسختك","عير","كسخالتك","خرا بالله","عير بالله","كسخواتكم","كحاب","مناويج","مناويج","كحبه","ابن الكحبه","فرخ","فروخ","طيزك","طيزختك","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","ابن العرص","منايك","متناك","احا","ابن المتناكه","زبك","عرص","زبي","خول","لبوه","لباوي","ابن اللبوه","منيوك","كسمكك","متناكه","احو","احي","يا عرص","يا خول","قحبه","القحبه","شراميط","العلق","العلوق","العلقه","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","االمنيوك","كسمككك","الشرموطه","ابن العرث","ابن الحيضانه","زبك","خول","زبي","قاحب","تيزك"]
  if str(text) in insults:
    if idchat in cursing:
      a = c.get_chat_member(idchat, m.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not m.from_user.id == OWNER_BOT:
         m.delete()
         mute.append(m.from_user.id)
         Text =f"""
♪ عذرا {m.from_user.mention} ⚡ .
♪ ممنوع الشتائم ⚡ .
"""
         m.reply(Text,quote=True)

  if m.forward_date:
    if idchat in forward:
      a = c.get_chat_member(idchat, m.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not m.from_user.id == OWNER_BOT:
         m.delete()
         mute.append(m.from_user.id)
         Text =f"""
♪ عذرا {m.from_user.mention} ⚡ .
♪ ممنوع التوجيه هنا ⚡ .
"""
         m.reply(Text,quote=True)
