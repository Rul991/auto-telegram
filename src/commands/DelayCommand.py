from pyrogram.client import Client
from pyrogram.types import Message

from src.commands.Command import Command
from src.utils import get_until_date

class DelayCommand(Command):
    _args = ['int', 'int', 'str']
    description = 'add scheduled messages'

    @property
    def name(self) -> str:
        return 'delay'
    
    def _get_args_messages(self) -> list[str]:
        return ['count', 'delay in seconds', 'message']

    async def execute(self, client: Client,  msg: Message, values: list[str]): # pyright: ignore[reportIncompatibleMethodOverride]
        count = int(values[0])
        delay = int(values[1])
        text = ' '.join(values[2:])

        for i in range(count):
            date = get_until_date((i + 1) * delay)
            await client.send_message(
                msg.chat.id,
                text,
                schedule_date=date
            )