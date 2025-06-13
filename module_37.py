
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd37$")
async def cmd37_cmd(event):
    await event.edit("✅ This is the `cmd37` module from 100+ pack.")
