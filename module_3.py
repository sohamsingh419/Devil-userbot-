
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd3$")
async def cmd3_cmd(event):
    await event.edit("✅ This is the `cmd3` module from 100+ pack.")
