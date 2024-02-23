from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# LOAD DISCORD TOKEN FROM ENV
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
LOG_STATUS: Final[bool] = os.getenv('LOG_STATUS')

# BOT SETTINGS
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


# MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:

    if not user_message.startswith('!') and not user_message:
        return
    
    if not user_message:
        print('[FATAL]: Message was empty because intents were not enabled on discord bot dashboard')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        if(response != None):
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(f"[FATAL]: {e}")


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'\n> {client.user} is now running...\n')


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    if LOG_STATUS:
        print(f'[Channel: {channel}]: {username} --> "{user_message}"')
    await send_message(message, user_message)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()