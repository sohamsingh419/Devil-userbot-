
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd87$")
async def cmd87_cmd(event):
    await event.edit("✅ This is the `cmd87` module from 100+ pack.")
