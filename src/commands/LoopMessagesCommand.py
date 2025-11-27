import asyncio
from pyrogram.client import Client
from pyrogram.types import Message

from src.commands.Command import Command
from src.consts import DELAY
from src.utils import split_text

class LoopMessagesCommand(Command):
    _args = ['int', 'str']
    description = 'sends a specified number of messages in a loop (text inside double quotes is treated as a single message)'

    @property
    def name(self) -> str:
        return 'loop'
    
    def _get_args_messages(self) -> list[str]:
        return ['count', 'texts']

    async def execute(self, client: Client,  msg: Message, values: list[str]): # pyright: ignore[reportIncompatibleMethodOverride]
        count = int(values[0])
        raw_messages = ' '.join(values[1:])
        messages = split_text(raw_messages)

        for _ in range(count):
            for message in messages:
                await client.send_message(msg.chat.id, message)
                await asyncio.sleep(DELAY)