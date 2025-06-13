
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd40$")
async def cmd40_cmd(event):
    await event.edit("✅ This is the `cmd40` module from 100+ pack.")
