
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^cmd95$")
async def cmd95_cmd(event):
    await event.edit("✅ This is the `cmd95` module from 100+ pack.")
