
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd1$")
async def cmd1_cmd(event):
    await event.edit("✅ This is the `cmd1` module from 100+ pack.")
