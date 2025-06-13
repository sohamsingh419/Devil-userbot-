
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd38$")
async def cmd38_cmd(event):
    await event.edit("✅ This is the `cmd38` module from 100+ pack.")
