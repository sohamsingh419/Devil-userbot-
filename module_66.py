
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd66$")
async def cmd66_cmd(event):
    await event.edit("✅ This is the `cmd66` module from 100+ pack.")
