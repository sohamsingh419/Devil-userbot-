
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd96$")
async def cmd96_cmd(event):
    await event.edit("✅ This is the `cmd96` module from 100+ pack.")
