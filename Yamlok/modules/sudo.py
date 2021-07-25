import os
import asyncio
import heroku3

from telethon.tl.functions.users import GetFullUserRequest
from telethon import events

from Yamlok import bot, SUDO_USERS
from Yamlok.utils import admin_cmd


# Function From TeleBoT

''' async def edit_or_reply(event, text):
    Try
     if event.user_id == SUDO_USERS:
            reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(text)
        return await event.reply(text)
    return await event.edit(text) '''


Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USERS", None)

@bot.on(admin_cmd(pattern="sudo")) 
async def sudo(event):
     sender = await event.get_input_sender()
     sudolelo = os.environ.get("SUDO_USERS", None) 
     await edit_or_reply(event.chat_id, f"** sᴜᴅᴏʟɪsᴛ ᴏғ ** bot.me.username\n {sudolelo}")

@bot.on(admin_cmd(pattern="addsudo"))
async def tb(event):
    ok = await eor(event, "α∂∂ιηg υsεя αs sυ∂σ υsεя...")
    Lion = "SUDO_USERS"
    if Var.HEROKU_APP_NAME is not None:
        app = Heroku.app(Var.HEROKU_APP_NAME)
    else:
        await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
        return
    heroku_var = app.config()
    if event is None:
        return
    try:
        target = await get_user(event)
    except Exception:
        await ok.edit(f"Reply to a user.")
    if sudousers:
        newsudo = f"{sudousers} {target}"
    else:
        newsudo = f"{target}"
    await ok.edit(
        f"Aᴅᴅᴇᴅ `{target}` ᴀs ᴀ sᴜᴅᴏ ᴜsᴇʀ. ɴᴏᴡ ʀᴇsᴛᴀʀᴛɪɴɢ ʟɪᴏɴ X.. ɢɪᴍᴍᴇ sᴏᴍᴇ ᴍɪɴᴜᴛᴇs..."
    )
    heroku_var[Lion] = newsudo
