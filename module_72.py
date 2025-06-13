
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd72$")
async def cmd72_cmd(event):
    await event.edit("✅ This is the `cmd72` module from 100+ pack.")
