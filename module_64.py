
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd64$")
async def cmd64_cmd(event):
    await event.edit("✅ This is the `cmd64` module from 100+ pack.")
