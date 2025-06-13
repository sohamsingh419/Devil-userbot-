
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd8$")
async def cmd8_cmd(event):
    await event.edit("✅ This is the `cmd8` module from 100+ pack.")
