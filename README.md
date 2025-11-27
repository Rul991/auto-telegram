# Auto-Telegram

Auto-Telegram is a Python-based Pyrogram app designed to automate message sending on Telegram. It interact with Telegram's API, allowing you to create and manage custom commands for seamless message automation.

## Features

- **Scheduled Messages**: Schedule messages to be sent at specific times.
- **Loop Messages**: Send a series of messages in a loop.
- **Casino Command**: Send dice roll messages in a loop.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Rul991/auto-telegram.git .
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with the following content:
   ```ini
   API_ID = # api_id in my.telegram.org
   API_HASH = # api_hash in my.telegram.org
   PASSWORD = # your telegram's password
   PHONE = # your telegram's phone number
   APP_NAME = auto-telegram # name of app
   ```

## Usage

1. Run the bot:
   ```sh
   python main.py
   ```

2. Use the available commands:
   - `.help`: Show all available commands.
   - `.loop <count> <texts>`: Send a specified number of messages in a loop.
   - `.delay <count> <delay in seconds> <message>`: Schedule messages to be sent at specific intervals.
   - `.casino`: Send a casino dice message every 2 seconds.

## Configuration

You can configure the bot by modifying the `.env` file with your Telegram API credentials and other settings.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.