
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd18$")
async def cmd18_cmd(event):
    await event.edit("✅ This is the `cmd18` module from 100+ pack.")
