import re
from random import randint
from engine.engine import *

def trail_response(tuple: Tuple[int, int]) -> str:

    wtoken, btoken = tuple
    if(wtoken > 0):
        wtoken = wtoken - 1
        reply = f'Hai superato la prova! Ti rimangono {wtoken} bianchi e {btoken} neri da spendere.'
    else:
        btoken = btoken - 1
        reply = f'Non hai superato la prova! Ti rimangono {btoken} neri da spendere.'
    return reply


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    # Check if the message starts with '!' or is null
    if not lowered.startswith('!') or lowered == '':
        return None
    elif 'Ciao' in lowered:
        return 'Hey ^^'
    elif 'd10' in lowered:
        return f'You rolled: {randint(1, 10)} between 1 and 10'
    elif 'estrai' in lowered:
        wtoken, btoken = estrai_token(lowered)
        return f"Hai estratto:\n\nWhite Token: {wtoken} :flag_white:\nBlack Token: {btoken} :pirate_flag:"
    elif 'confusione' in lowered:
           try:
              return trail_response(confusione(lowered))  
           except ValueError as erVal:
               return f'Attento: {erVal}'
           except Exception as e:
               return f'[FATAL]: {e}'
    else:
        return 'Scrivi bene i comandi, coglione :rage:'