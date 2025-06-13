
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd27$")
async def cmd27_cmd(event):
    await event.edit("✅ This is the `cmd27` module from 100+ pack.")
