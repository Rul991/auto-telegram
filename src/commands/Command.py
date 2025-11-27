from abc import ABC, abstractmethod
from pyrogram.types import Message
from pyrogram.client import Client

from src.types import CommandArgs
from src.utils import is_convertible_to_number

class Command(ABC):
    _args: CommandArgs = []
    description: str = ''
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    async def execute(self, client: Client, msg: Message, values: list[str]):
        pass

    def can_use(self, msg: Message) -> bool:
        args_len = len(self._args)

        if args_len <= 0:
            return True

        message_args = self._get_args(msg)

        if len(message_args) < args_len:
            return False
        
        for i in range(args_len):
            if message_args[i] != self._args[i]:
                return False

        return True
    
    def _get_args_messages(self) -> list[str]:
        result: list[str] = []

        for arg in self._args:
            result.append('число' if arg == 'int' else 'строка')

        return result
    
    def get_syntax_message(self) -> str:
        result = ''

        for arg in self._get_args_messages():
            result += f'[{arg}] '

        return f'.{self.name} {result}'

    def _get_args(self, msg: Message) -> CommandArgs:
        result: CommandArgs = []
        parts = msg.text.split()[1:]

        for part in parts:
            if is_convertible_to_number(part):
                result.append('int')
            else:
                result.append('str')

        return result