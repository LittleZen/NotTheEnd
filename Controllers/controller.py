import os
from Services.engine import Engine
from random import randint
from discord import Message
from typing import Tuple


class Controller():


# La funzione definisce la lettura dei comandi inviati al bot.
    def get_response(self, user_input: str) -> str:
        engine = Engine()
        lowered: str = user_input.lower()
        
        # Check if the message starts with '!' or is null
        if not lowered.startswith('!') or lowered == '':
            return None
        
        elif 'Ciao' in lowered:
            return 'Hey ^^'
        
        elif 'd10' in lowered:
            return f'You rolled: {randint(1, 10)} between 1 and 10'
        
        elif 'estrai' in lowered:
            return self.trail_response(engine.estrai_token(lowered))
        
        elif 'confusione' in lowered:
            try:
                return self.trail_response(engine.confusione(lowered))  
            except ValueError as erVal:
                return f'Attento: {erVal}'
            except Exception as e:
                return f'[FATAL]: {e}'
        
        else:
            return 'Scrivi bene i comandi, coglione :rage:'
        

# Gestore: invio dei messaggi 
    async def send_message(self, message: Message, user_message: str) -> None:
        if not user_message.startswith('!') and not user_message:
            return
        
        if not user_message:
            print('[FATAL]: Message was empty because intents were not enabled on discord bot dashboard')
            return
        
        if is_private := user_message[0] == '?':
            user_message = user_message[1:]

        try:
            response: str = self.get_response(user_message)
            if(response != None):
                await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:
            print(f"[FATAL]: {e}")


# Sistema di risposte per le prove
    def trail_response(self, wbtuple: Tuple[int, int]) -> str:

        wtoken, btoken = wbtuple
        if(wtoken > 0):
            wtoken = wtoken - 1
            reply = f'Hai superato la prova!\n\nDevi ancora spende:\n:white_circle: {wtoken} bianchi\n:black_circle: {btoken} neri'
        else:
            btoken = btoken - 1
            reply = f'Non hai superato la prova!\n\nTi rimangono inoltre:\n:black_circle: {btoken} neri da spendere.'
        return reply
    
    