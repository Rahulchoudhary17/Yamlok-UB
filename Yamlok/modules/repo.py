from telethon import events, Button, custom
from Yamlok import bot, xbot
from Yamlok.utils import admin_cmd, sudo_cmd
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@xbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 
 YAMLOK = event.builder
 X= [[custom.Button.inline("🔥 Cʟɪᴄᴋ Hᴇʀᴇ 🔥",data="obhai")]]
 query = event.text
 
 result = YAMLOK.article("Yamlok",text="**yamlok's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Sᴜᴘᴘᴏʀᴛ\n\n© @yamlokofficial**",buttons=X,link_preview=False)
 await event.answer([result])
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event):
  await event.edit(text=f"**yamlok's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Gʀᴏᴜᴘ Lɪɴᴋ\n\n© @yamlokofficial**",buttons=[
                [
                    Button.url(f"⚜️ Rᴇᴘᴏ ⚜️", url="https://github.com/AT-WORLDS-END/Yamlok-userbot"),
                    Button.url(f"🌚 Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ 🌝", url="https://t.me/yamloksuport")],
                    [Button.url(f"🔰 Dᴇᴘʟᴏʏ 🔰", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FAT-WORLDS-END%2FYamlok-userbot&template=https%3A%2F%2Fgithub.com%2FAT-WORLDS-END%2FYamlok-userbot"),
                     Button.url(f"💠 Sᴛʀɪɴɢ 💠", url="https://repl.it/@SpEcHiDe/GenerateStringSession"),
                ]
            ]
                   
                  )
© 2021 GitHub, Inc.
