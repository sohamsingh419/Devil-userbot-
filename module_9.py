
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd9$")
async def cmd9_cmd(event):
    await event.edit("✅ This is the `cmd9` module from 100+ pack.")
