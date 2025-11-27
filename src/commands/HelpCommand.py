from pyrogram.client import Client
from pyrogram.types import Message

from src.App import App
from src.commands.Command import Command

class HelpCommand(Command):
    _args = []
    _app: App
    description = 'show you all commands'

    @property
    def name(self) -> str:
        return 'help'
    
    def __init__(self, app: App) -> None:
        super().__init__()
        self._app = app

    async def execute(self, client: Client,  msg: Message, _values: list[str]): # pyright: ignore[reportIncompatibleMethodOverride]
        commands = self._app.get_commands()
        text = '**Commands:**'

        for command in commands:
            text += f'\n\n- `{command.get_syntax_message()}`- {command.description}'

        await client.send_message(
            msg.chat.id,
            text,
        )