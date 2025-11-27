import asyncio

from src.App import App
from src.commands.CasinoCommand import CasinoCommand
from src.commands.LoopMessagesCommand import LoopMessagesCommand
from src.commands.DelayCommand import DelayCommand
from src.commands.HelpCommand import HelpCommand

async def main():
    app = App()

    app.add_commands(
        LoopMessagesCommand(),
        DelayCommand(),
        HelpCommand(app),
        CasinoCommand()
    )
    
    await app.run()
    await asyncio.Event().wait()

asyncio.run(main()) # type: ignore