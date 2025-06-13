
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd51$")
async def cmd51_cmd(event):
    await event.edit("✅ This is the `cmd51` module from 100+ pack.")
