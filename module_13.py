
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd13$")
async def cmd13_cmd(event):
    await event.edit("✅ This is the `cmd13` module from 100+ pack.")
