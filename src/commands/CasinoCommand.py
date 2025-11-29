from pyrogram.client import Client
from pyrogram.types import Message
import asyncio
from src.commands.Config import Config
from src.commands.Command import Command
from src.consts import DELAY

class CasinoCommand(Command):
    _args = []
    description = f'sends a dice roll message every {DELAY} seconds'

    @property
    def name(self) -> str:
        return 'casino'

    def _get_args_messages(self) -> list[str]:
        return []

    async def execute(self, client: Client, msg: Message, values: list[str]):
        Config.is_casino_stopping = not Config.is_casino_stopping

        while True:
            if Config.is_casino_stopping:
                break

            await client.send_dice(
                msg.chat.id,
                emoji='🎰'
            )
            await asyncio.sleep(DELAY)