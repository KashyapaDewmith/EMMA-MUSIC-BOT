from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from kashyapa.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from kashyapa  import app, LOGGER
from kashyapa .kashyapa import ignore_blacklisted_users
from kashyapa .sql.chat_sql import add_chat_to_db

start_text = """
👋 Hay [{}](tg://user?id={}),
Powered By 🔰kashyapa dewmith🔰

Send The Name of the Song You Want..
𝐄𝐠. ```/song black pink how you like that```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [
               [
                   InlineKeyboardButton(text="📣 contact me 📣", url="https://telegram.me/IMkashyapaa"),
                   InlineKeyboardButton(text="👥 my main bot 👥", url="https://telegram.me/Lanka_ehi_files_bot")
               ],
               
               [
                   InlineKeyboardButton(text="🎓 DEVELOPER 🎓", url='https://telegram.me/IMkashyapaa'),
                   
               
          ]     
    )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Send The Name of the Song You Want..\n /song (song name) "
    await message.reply(text)

OWNER_url.append("https://telegram.me/IMkashyapaa")
app.start()
LOGGER.info(" 𝐊𝐚𝐬𝐡𝐲𝐚𝐩𝐚 𝐦𝐮𝐬𝐢𝐜 Was Deployed Successfully! ✅")
idle()
