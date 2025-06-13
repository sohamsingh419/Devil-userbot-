
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd88$")
async def cmd88_cmd(event):
    await event.edit("✅ This is the `cmd88` module from 100+ pack.")
