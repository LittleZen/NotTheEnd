import re
from random import randint
from engine.engine import *


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    # Check if the message starts with '!' or is null
    if not lowered.startswith('!') or lowered == '':
        print("nothing for you here")
        return None
    elif 'hello' == lowered:
        return 'Hello there!'
    elif 'roll' == lowered:
        return f'You rolled: {randint(1, 10)} between 1 and 10'
    elif 'dice' in lowered:  # Corrected condition
        wtoken, btoken = estrai_token(lowered)
        return f"Hai estratto:\n\nWhite Token:{wtoken}\nBlack Token: {btoken}"    
    else:
        print(f">>{lowered}")
        return None