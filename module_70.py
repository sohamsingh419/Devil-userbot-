
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd70$")
async def cmd70_cmd(event):
    await event.edit("✅ This is the `cmd70` module from 100+ pack.")
