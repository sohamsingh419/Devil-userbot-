
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd11$")
async def cmd11_cmd(event):
    await event.edit("✅ This is the `cmd11` module from 100+ pack.")
