import re
from random import randint
from engine.engine import RollNTE

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    # Check if the message starts with '!' or is null
    if not (lowered.startswith('!')) or (lowered == ''):
        return None
    elif 'hello' == lowered:
        return 'Hello there!'
    elif 'roll' == lowered:
        return f'You rolled: {randint(1, 10)} between 1 and 10'
    elif 'dice' == lowered:
        # Using regular expression to find the pattern !roll(x,y,z)
        match = re.search(r'!roll\((\d+),(\d+),(\d+)\)', lowered)
        if match:
            params = match.groups()
            numbers = [int(param) for param in params]
            print(f"[#] numbers: {numbers}")
            return RollNTE(numbers)
        else:
            return 'Invalid roll command. Use !roll(x,y,z) where x, y, and z are integers.'
    else:
        return None