import re
import random
from random import sample
from typing import Tuple

'''
    Decode the command raised, and extract the params
'''
def decode_commands_parameter(command : str) -> list:
    command_pattern = r'!(\w+)\((\d+(?:,\d+)*)\)'
    match = re.search(command_pattern, command)
    if match:
        integer_values = match.group(2).split(',')
        integer_values = [int(value) for value in integer_values]
        return integer_values
        

"""
    Simula l'estrazione di num_token_da_estrarre token da un sacchetto contenente
    num_token_bianche token bianche e num_token_nere token nere.
    
    :param num_token_da_estrarre: Numero di token da estrarre dal sacchetto.
    :param num_token_bianche: Numero di token bianche nel sacchetto.
    :param num_token_nere: Numero di token nere nel sacchetto.
    :return: Una tupla contenente il numero di token bianche e nere estratte (int, int).
"""
def estrai_token(lowered : str) -> Tuple[int, int]:
    
    numbers = decode_commands_parameter(lowered) # decode the command params

    num_token_da_estrarre = numbers[0] 
    num_token_bianche =  numbers[1] 
    num_token_nere =  numbers[2] 

    print(f">TOKEN SET: extract:{num_token_da_estrarre}, wtoken:{num_token_bianche}, btoken {num_token_nere}")

    sacchetto = ["B"] * num_token_bianche + ["N"] * num_token_nere

    if num_token_da_estrarre > len(sacchetto):
        raise ValueError("Il numero di token da estrarre supera il numero totale di token nel sacchetto.")
    
    token_estratte = sample(sacchetto, num_token_da_estrarre)
    token_bianche_estratte = token_estratte.count("B")
    token_nere_estratte = token_estratte.count("N")
    
    return token_bianche_estratte, token_nere_estratte


"""
    Simula l'estrazione di num_token_da_estrarre token da un sacchetto contenente
    num_token_bianche token bianche e num_token_nere token nere.
    
    :param num_token_da_estrarre: Numero di token da estrarre dal sacchetto.
    :param num_token_bianche: Numero di token bianche nel sacchetto.
    :param num_token_nere: Numero di token nere nel sacchetto.
    :return: Una tupla contenente il numero di token bianche e nere estratte (int, int).
"""
def confusion(lowered: str) -> Tuple[int, int]:   # [TO DO ]

    numbers = decode_commands_parameter(lowered) # decode the command params

    num_token_da_estrarre = numbers[0]
    num_token_random = numbers[1]
    num_token_nere = numbers[2]

    # Randomizzazione delle fish, tra bianche e nere, prima dell'estrazione finale
    tmpBianche = random.randint(0,num_token_random)
    tmpBlack = num_token_random - tmpBianche
    token_bianche_random, token_nere_random = estrai_token((tmpBianche + tmpBlack), tmpBianche , tmpBlack)

    num_token_nere += token_nere_random

    sacchetto = ["B"] * token_bianche_random + ["N"] * num_token_nere

    if num_token_da_estrarre > len(sacchetto):
        raise ValueError("Il numero di token da estrarre supera il numero totale di token nel sacchetto.")
    
    token_estratte = sample(sacchetto, num_token_da_estrarre)
    token_bianche_estratte = token_estratte.count("B") 
    token_nere_estratte = token_estratte.count("N") 
    
    return token_bianche_estratte, token_nere_estratte

