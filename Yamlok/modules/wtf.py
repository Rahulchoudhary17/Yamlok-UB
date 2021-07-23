"""Emoji
Available Commands:
.wtf"""

from telethon import events

import asyncio

from Yamlok.utils import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "wtf":
        await event.edit(input_str)
        animation_chars = [
            "What",
            "What The",
            "What The F",
            "What The F Brah",
            "[What The F Brah](https://telegra.ph/file/9ae153cf13158d795cb64.jpg)"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %5 ])
