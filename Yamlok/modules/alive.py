# (c) Copyright 2021-2022 Yamlok
# Made By @AT-WORLDS-END


from Yamlok import bot
from Yamlok.utils import admin_cmd
@bot.on(admin_cmd(pattern=r"alive"))
async def amialivedad(event): 
   chat = event.chat_id 
   message = " Master ! I am alive :)" 
   await event.edit(message)
