
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd4$")
async def cmd4_cmd(event):
    await event.edit("✅ This is the `cmd4` module from 100+ pack.")
