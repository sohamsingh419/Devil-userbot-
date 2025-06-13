
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd91$")
async def cmd91_cmd(event):
    await event.edit("✅ This is the `cmd91` module from 100+ pack.")
