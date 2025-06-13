
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd17$")
async def cmd17_cmd(event):
    await event.edit("✅ This is the `cmd17` module from 100+ pack.")
