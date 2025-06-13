
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd69$")
async def cmd69_cmd(event):
    await event.edit("✅ This is the `cmd69` module from 100+ pack.")
