
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd90$")
async def cmd90_cmd(event):
    await event.edit("✅ This is the `cmd90` module from 100+ pack.")
