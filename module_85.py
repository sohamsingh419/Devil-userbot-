
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd85$")
async def cmd85_cmd(event):
    await event.edit("✅ This is the `cmd85` module from 100+ pack.")
