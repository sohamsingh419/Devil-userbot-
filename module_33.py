
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd33$")
async def cmd33_cmd(event):
    await event.edit("✅ This is the `cmd33` module from 100+ pack.")
