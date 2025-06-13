
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd65$")
async def cmd65_cmd(event):
    await event.edit("✅ This is the `cmd65` module from 100+ pack.")
