
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd71$")
async def cmd71_cmd(event):
    await event.edit("✅ This is the `cmd71` module from 100+ pack.")
