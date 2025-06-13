
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd76$")
async def cmd76_cmd(event):
    await event.edit("✅ This is the `cmd76` module from 100+ pack.")
