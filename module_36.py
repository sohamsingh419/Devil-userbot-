
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd36$")
async def cmd36_cmd(event):
    await event.edit("✅ This is the `cmd36` module from 100+ pack.")
