
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd97$")
async def cmd97_cmd(event):
    await event.edit("✅ This is the `cmd97` module from 100+ pack.")
