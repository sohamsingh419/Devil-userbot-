
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd23$")
async def cmd23_cmd(event):
    await event.edit("✅ This is the `cmd23` module from 100+ pack.")
