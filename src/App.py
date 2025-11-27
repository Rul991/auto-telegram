from pyrogram.client import Client
from pyrogram import filters
from pyrogram.types import Message

from src.commands.Command import Command
from src.consts import API_HASH, API_ID, APP_NAME, PASSWORD, PHONE
from src.utils import log

class App:
    _client: Client
    _commands: dict[str, Command]
    _default_command: Command | None

    def __init__(
        self, 
        default_command: Command | None = None
    ) -> None:
        self._client = Client(
            APP_NAME,
            API_ID,
            API_HASH,
            password=PASSWORD,
            phone_number=PHONE
        )
        self.set_default_command(default_command)
        self._commands = {}
        

    def add_commands(self, *commands: Command):
        for command in commands:
            self._commands[command.name] = command

    def set_default_command(self, command: Command | None):
        self._default_command = command

    def get_commands(self) -> list[Command]:
        result: list[Command] = []

        for _, value in self._commands.items():
            result.append(value)

        return result

    def handle_commands(self):
        @self._client.on_message(filters.me & filters.text) # pyright: ignore[reportUnknownMemberType, reportUntypedFunctionDecorator]
        async def _(client: Client, msg: Message):
            text = msg.text
            
            if text.startswith('.'):
                await client.delete_messages(msg.chat.id, msg.id)

                parts = text.split()
                name = parts[0][1:]
                command = self._commands.get(name, self._default_command)

                if command and command.can_use(msg):
                    try:
                        log('client', f'command "{command.name}" is started')
                        await command.execute(client, msg, parts[1:])
                        log('client', f'command "{command.name}" is ended')

                    except Exception as e:
                        error_str = str(e)
                        log('error', error_str)
                        await client.send_message(msg.chat.id, f'Error: {error_str}')

                elif command:
                    log('client', f'command "{command.name}" cant use')
                    await client.send_message(msg.chat.id, f'<code>Syntax: {command.get_syntax_message()}</code>')

                else:
                    log('client', f'command "{name}" not exist')


    async def run(self) -> None:
        self.handle_commands()
        await self._client.start()
        log('client', 'client is started')