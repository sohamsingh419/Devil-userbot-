
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd62$")
async def cmd62_cmd(event):
    await event.edit("✅ This is the `cmd62` module from 100+ pack.")
