
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd20$")
async def cmd20_cmd(event):
    await event.edit("✅ This is the `cmd20` module from 100+ pack.")
