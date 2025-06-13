
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd93$")
async def cmd93_cmd(event):
    await event.edit("✅ This is the `cmd93` module from 100+ pack.")
