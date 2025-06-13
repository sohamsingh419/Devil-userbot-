
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd80$")
async def cmd80_cmd(event):
    await event.edit("✅ This is the `cmd80` module from 100+ pack.")
