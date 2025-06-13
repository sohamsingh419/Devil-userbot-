
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd77$")
async def cmd77_cmd(event):
    await event.edit("✅ This is the `cmd77` module from 100+ pack.")
