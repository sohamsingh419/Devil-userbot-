
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd73$")
async def cmd73_cmd(event):
    await event.edit("✅ This is the `cmd73` module from 100+ pack.")
