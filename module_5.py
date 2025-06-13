
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd5$")
async def cmd5_cmd(event):
    await event.edit("✅ This is the `cmd5` module from 100+ pack.")
