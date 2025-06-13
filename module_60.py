
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd60$")
async def cmd60_cmd(event):
    await event.edit("✅ This is the `cmd60` module from 100+ pack.")
