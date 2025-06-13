
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd98$")
async def cmd98_cmd(event):
    await event.edit("✅ This is the `cmd98` module from 100+ pack.")
