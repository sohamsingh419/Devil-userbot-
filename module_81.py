
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd81$")
async def cmd81_cmd(event):
    await event.edit("✅ This is the `cmd81` module from 100+ pack.")
