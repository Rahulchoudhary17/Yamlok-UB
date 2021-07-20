# COPYRIGHT (C) 2021-2022 BY Yamlok
# modify by AT-WORLDS-END

import datetime
import re
import time

from telethon import Button, custom, events

from Yamlok import BOT, PHOTO, VERSION, xbot
from Yamlok import StartTime, bot


@xbot.on(events.NewMessage(pattern=("/alive")))
async def awake(event):
    Yamlok = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
    Yamlok += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
    Yamlok += f"**{BOT} Vᴇʀsɪᴏɴ** : `{VERSION}`\n\n"
    Yamlok += f"**Usᴇʀ** : @{bot.me.username}\n\n"
    Yamlok += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
    Yamlok += "**Tᴇʟᴇᴛʜᴏɴ** : `1.20`\n\n"
    Yamlok += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
    BUTTON = [
        [
            Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"),
            Button.url(f"{BOT} Rᴇᴘᴏ", "......"),
        ]
    ]
    BUTTON += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="Yamlok")]]
    await xbot.send_file(event.chat_id, PHOTO, caption=Yamlok, buttons=BUTTON)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"SkemX")))
async def callback_query_handler(event):
    # inline by AT-WORLDS-END
    SkemX = [[Button.url("Rᴇᴘᴏ Yamlok", ".......")]]
    SkemX += [
        [
            Button.url(
                "Dᴇᴘʟᴏʏ Yamlok",
                "............................",
            )
        ]
    ]
    SkemX += [
        [
            Button.url(
                "Sᴛʀɪɴɢ Sᴇssɪᴏɴ", ".........."
            ),
        ]
    ]
    SkemX += [
        [
            Button.url("Rᴇᴅɪs", "https://redislabs.com"),
        ]
    ]
    SkemX += [
        [
            Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ", "............."),
            Button.url("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", "............"),
        ]
    ]
    SkemX += [[custom.Button.inline("«« Aʟɪᴠᴇ", data="Skem")]]
    await event.edit(text=f"Aʟʟ Dᴇᴛᴀɪʟs Oғ Rᴇᴘᴏs", buttons=SkemX)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Skem")))
async def callback_query_handler(event):
    # inline by AT-WORLDS-END
    Yamlok = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
    Yamlok += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
    Yamlok += f"**{BOT} Vᴇʀsɪᴏɴ** : `{VERSION}`\n\n"
    Yamlok += f"**Usᴇʀ** : @{bot.me.username}\n\n"
    Yamlok += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
    Yamlok += "**Tᴇʟᴇᴛʜᴏɴ** : `1.20`\n\n"
    Yamlok += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
    BUTTONS = [
        [
            Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"),
            Button.url(f"{BOT} Rᴇᴘᴏ", "............."),
        ]
    ]
    BUTTONS += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="Yamlok")]]
    await event.edit(text=Yamlok, buttons=BUTTONS)


@xbot.on(events.NewMessage(pattern=("/repo")))
async def repo(event):
    await xbot.send_message(
        event.chat,
        "**Hᴇʀᴇ Is Tʜᴇ Rᴇᴘᴏ Fᴏʀ Yamlok Usᴇʀʙᴏᴛ** \n\nFᴏʀ Aɴʏ Hᴇʟᴘ :- @YamlokOT",
        buttons=[
            [
                Button.url("⚜️ Rᴇᴘᴏ ⚜️", ".................."),
                Button.url(
                    "🔰 Dᴇᴘʟᴏʏ 🔰",
                    "............................",
                ),
            ]
        ],
    )


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@xbot.on(events.NewMessage(pattern=None))
async def ok(event):
    msg = str(event.text)
    if not msg == "/ping":
        return

    start_time = datetime.datetime.now()
    message = await event.reply("_.._.._Pinging_.._.._")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b><i>☞ Pᴏɴɢ !!</i></b>\n"
        "<b>➥ Tɪᴍᴇ Tᴀᴋᴇɴ:</b> <code>{}</code>\n"
        "<b>➥ Sᴇʀᴠɪᴄᴇ Uᴘᴛɪᴍᴇ:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode="html",
    )
