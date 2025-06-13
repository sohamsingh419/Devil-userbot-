
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd50$")
async def cmd50_cmd(event):
    await event.edit("✅ This is the `cmd50` module from 100+ pack.")
