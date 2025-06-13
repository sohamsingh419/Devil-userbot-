
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd26$")
async def cmd26_cmd(event):
    await event.edit("✅ This is the `cmd26` module from 100+ pack.")
