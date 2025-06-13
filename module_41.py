
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd41$")
async def cmd41_cmd(event):
    await event.edit("✅ This is the `cmd41` module from 100+ pack.")
