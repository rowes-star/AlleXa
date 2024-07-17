import asyncio
from pyrogram import Client,filters,enums,idle
from config import *
from asyncio import get_event_loop
from autoname import main as name

async def main():
  await app.start()
  await bot.start()
  try :
    await app.join_chat("qkpqp")
    await app.join_chat("zxzlz")
    await app.join_chat("uplake")
  except :
    pass
  starkbot = await bot.get_me()
  perf = "[ الزوز ]"
  bot_name = starkbot.first_name
  botname = f"@{starkbot.username}"
  if bot_name.endswith("Assistant"):
    print(" لقد عاد البوت للعمل...√ ")
  else:
    try:
        await app.send_message("@BotFather", "/setinline")
        await asyncio.sleep(1)
        await app.send_message("@BotFather", botname)
        await asyncio.sleep(1)
        await app.send_message("@BotFather", perf)
        await asyncio.sleep(2)
    except Exception as e:
        print(e)
  await name()
  await idle()
  


loop = get_event_loop()
loop.run_until_complete(main())
