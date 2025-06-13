
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd99$")
async def cmd99_cmd(event):
    await event.edit("✅ This is the `cmd99` module from 100+ pack.")
