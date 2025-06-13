
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd78$")
async def cmd78_cmd(event):
    await event.edit("✅ This is the `cmd78` module from 100+ pack.")
