
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd61$")
async def cmd61_cmd(event):
    await event.edit("✅ This is the `cmd61` module from 100+ pack.")
