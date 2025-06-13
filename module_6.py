
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd6$")
async def cmd6_cmd(event):
    await event.edit("✅ This is the `cmd6` module from 100+ pack.")
