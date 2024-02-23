import re
from random import randint
from engine.engine import *


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
              wtoken, btoken = confusione(lowered)  
           except ValueError as erVal:
               return f'Attento: {erVal}'
           return f"Il tuo tiro confusione:\n\nWhite Token: {wtoken} :white_circle:\nBlack Token: {btoken} :black_circle:"
    else:
        return 'Scrivi bene i comandi, coglione :rage:'