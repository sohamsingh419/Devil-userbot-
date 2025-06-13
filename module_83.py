
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd83$")
async def cmd83_cmd(event):
    await event.edit("✅ This is the `cmd83` module from 100+ pack.")
