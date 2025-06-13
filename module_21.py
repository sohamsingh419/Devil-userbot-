
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd21$")
async def cmd21_cmd(event):
    await event.edit("✅ This is the `cmd21` module from 100+ pack.")
