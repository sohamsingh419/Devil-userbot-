
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd7$")
async def cmd7_cmd(event):
    await event.edit("✅ This is the `cmd7` module from 100+ pack.")
