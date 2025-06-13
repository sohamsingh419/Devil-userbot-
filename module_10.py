
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd10$")
async def cmd10_cmd(event):
    await event.edit("✅ This is the `cmd10` module from 100+ pack.")
