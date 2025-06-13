
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd100$")
async def cmd100_cmd(event):
    await event.edit("✅ This is the `cmd100` module from 100+ pack.")
