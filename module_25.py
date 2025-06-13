
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd25$")
async def cmd25_cmd(event):
    await event.edit("✅ This is the `cmd25` module from 100+ pack.")
