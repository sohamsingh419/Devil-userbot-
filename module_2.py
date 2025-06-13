
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd2$")
async def cmd2_cmd(event):
    await event.edit("✅ This is the `cmd2` module from 100+ pack.")
