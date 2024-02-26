import os
from Services.engine import Engine
from random import randint
from discord import Message
from typing import Tuple
from Classes.random_bag import RandomBag


class Controller():

# Costruttore di Controller, inizializza un oggetto di tipo engine utilizzato dall'istanza della classe
    def __init__(self):
        self.engine = Engine()


# Sistema di risposte per le prove {manca la classe <sacchetto> invece della tupla}
    def trail_response(self, random_bag: RandomBag) -> str:
        if(random_bag.exwToken > 0):
            random_bag.exwToken = random_bag.exwToken - 1
            reply = f'Hai superato la prova!\n\nDevi ancora spende:\n:white_circle: {random_bag.exwToken} bianchi\n:black_circle: {random_bag.exbToken} neri'
        else:
            random_bag.exbToken = random_bag.exbToken - 1
            reply = f'Non hai superato la prova!\n\nTi rimangono inoltre:\n:black_circle: {random_bag.exbToken} neri da spendere.'
        return reply

# La funzione definisce la lettura dei comandi inviati al bot.
    def get_response(self, user_input: str) -> str:
        if 'Ciao' in user_input:
            return 'Hey ^^'
        
        elif 'd10' in user_input:
            return f'You rolled: {randint(1, 10)} between 1 and 10'
        
        elif 'estrai' in user_input:
            try: 
                return self.trail_response(self.engine.simple_trail(user_input))
            except ValueError as errVal:
                print(f"[ESTRAI - FATAL_ERROR]: {errVal}")
                return None
            except Exception as e:
                print(f"[ESTRAI - FATAL_ERROR]: {e}")
                return None

        elif 'confusione' in user_input:
            try:
                return self.trail_response(self.engine.confused_trail(user_input))  
            except ValueError as erVal:
                return f'[CONFUSIONE - FATAL_ERROR]: {erVal}'
            except Exception as e:
                return f'[CONFUSIONE - FATAL_ERROR]: {e}'
        
        else:
            return 'Scrivi bene i comandi, coglione :rage:'
        

# Gestore: invio dei messaggi 
    async def send_message(self, message: Message, user_message: str) -> None:
        if not user_message.startswith('!') and not user_message:
            return
        
        if not user_message:
            print('> [send_message - FATAL_ERROR]: Message was empty, probably because intents were not enabled on discord bot dashboard')
            return
        
        # verifica se il messaggio é in un canale privato o da un server
        if is_private := user_message[0] == '?':
            user_message = user_message[1:]

        try:
            response: str = self.get_response(user_message.lower())
            if(response != None):
                await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:
            print(f"[FATAL]: {e}")



    
    