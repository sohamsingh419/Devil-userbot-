
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd89$")
async def cmd89_cmd(event):
    await event.edit("✅ This is the `cmd89` module from 100+ pack.")
