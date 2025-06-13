
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd43$")
async def cmd43_cmd(event):
    await event.edit("✅ This is the `cmd43` module from 100+ pack.")
