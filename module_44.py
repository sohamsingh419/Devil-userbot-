
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd44$")
async def cmd44_cmd(event):
    await event.edit("✅ This is the `cmd44` module from 100+ pack.")
