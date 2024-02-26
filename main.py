import os
import discord
from typing import Final
from dotenv import load_dotenv
from discord import Intents
from discord.ext import commands
from Controllers.controller import Controller

# Carica il token e avvia le fasi preliminari del bot
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Dichiarazione d'intenti (utilizzata da discord)
intents: Intents = Intents.default()
intents.message_content = True

# Crea l'istanza del bot con un prefisso per i comandi
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

class DClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = Controller()

    # Evento: on_ready
    async def on_ready(self) -> None:
        print(f'\n> Logged on as {self.user}!\n')

    @bot.command(name='somma')
    async def somma(ctx, *numeri: int):
        risultato = sum(numeri)
        await ctx.send(f'La somma dei valori è {risultato}.')

    # Gestore: della ricezione da parte di un utente dei messaggi [move?] [cambiare?]
    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.user:
            return

        username: str = str(message.author)
        user_message: str = message.content
        channel: str = str(message.channel)

        #print(f'{LOG_STATUS} [Channel: {channel}]: {username} --> "{user_message}"')
        await self.controller.send_message(message, user_message)


 # =================================================================================================== #

# Funzione main, avvia il bot
def main() -> None:
    #client = DClient(intents=intents)
    #client.run(token=TOKEN)
    # Crea l'istanza del bot con un prefisso per i comandi
    bot.run(TOKEN)

# Gestore: esecuzione dello script python
if __name__ == '__main__':
    main()