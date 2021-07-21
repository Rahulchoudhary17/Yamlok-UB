# (c) Copyright 2021-2022 Yamlok
# modify by AT-WORLDS-END
# credits shivam 

import os

from Yamlok import CMD_HELP
from Yamlok.events import remove_plugin
from Yamlok.utils import admin_cmd, remove_plugin


@bot.on(admin_cmd(pattern=r"^uninstall (?P<shortname>\w+)$"))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path = f"./DaisyX/modules/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await event.edit(f"**Uɴɪɴsᴛᴀʟʟᴇᴅ** `{shortname}` **Sᴜᴄᴄᴇssғᴜʟʟʏ**")
    except OSError as e:
        await event.edit("Error: %s : %s" % (dir_path, e.strerror))


CMD_HELP.update(
    {
        "uninstall": "**Plugin : **`uninstall`\
    \n\n**Syntax : **`.uninstall`\
    \n**Function : **use this plugin to uninstall any plug"
    }
)
