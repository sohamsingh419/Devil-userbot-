
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd22$")
async def cmd22_cmd(event):
    await event.edit("✅ This is the `cmd22` module from 100+ pack.")
