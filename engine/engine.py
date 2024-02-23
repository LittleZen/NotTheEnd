import re
import time
import random
from random import sample
from typing import Tuple


'''
    Decode the command raised, and extract the params
'''
def extract_integers_from_sentence(sentence: str) -> list:
    integer_pattern = r'\b\d+\b'
    match = re.search(integer_pattern, sentence)
    if match:
        integer_values = re.findall(integer_pattern, sentence)
        integer_values = [int(value) for value in integer_values]
        return integer_values
    else:
        return []
    
def numerical_array_to_string(valori : list) -> str:
    # Converti ogni valore numerico in una stringa
    valori_str = [str(valore) for valore in valori]
    # Unisci le stringhe separate da una virgola
    return ", ".join(valori_str)
        

"""
    Simula l'estrazione di num_token_da_estrarre token da un sacchetto contenente
    num_token_bianche token bianche e num_token_nere token nere.
    
    :param num_token_da_estrarre: Numero di token da estrarre dal sacchetto.
    :param num_token_bianche: Numero di token bianche nel sacchetto.
    :param num_token_nere: Numero di token nere nel sacchetto.
    :return: Una tupla contenente il numero di token bianche e nere estratte (int, int).
"""
def estrai_token(lowered : str) -> Tuple[int, int]:
    numbers = extract_integers_from_sentence(lowered) # decode the command params

    num_token_da_estrarre = numbers[0] 
    num_token_bianche =  numbers[1] 
    num_token_nere =  numbers[2] 

    sacchetto = ["B"] * num_token_bianche + ["N"] * num_token_nere

    if num_token_da_estrarre > len(sacchetto):
        raise ValueError("Il numero di token da estrarre supera il numero totale di token nel sacchetto.")
    
    token_estratte = sample(sacchetto, num_token_da_estrarre)
    token_bianche_estratte = token_estratte.count("B")
    token_nere_estratte = token_estratte.count("N")
    
    return token_bianche_estratte, token_nere_estratte


"""
    Simula un l'estrazione di num_token_da_estrarre token da un sacchetto contenente
    num_token_bianche token bianche e num_token_nere token nere.
    
    :param num_token_da_estrarre: Numero di token da estrarre dal sacchetto.
    :param num_token_bianche: Numero di token bianche nel sacchetto.
    :param num_token_nere: Numero di token nere nel sacchetto.
    :return: Una tupla contenente il numero di token bianche e nere estratte (int, int).
"""
def confusione(lowered: str) -> Tuple[int, int]:   # [TO DO ]

    numbers = extract_integers_from_sentence(lowered) # decode the command params

    print(f">>>{numbers}")
    num_token_da_estrarre = numbers[0]
    num_token_random = numbers[1]
    num_token_nere = numbers[2]

    # Randomizzazione delle fish, tra bianche e nere, prima dell'estrazione finale
    random.seed(time.time())
    tmpBianche = random.randint(0,num_token_random)
    tmpBlack = num_token_random - tmpBianche
    token_bianche_random, token_nere_random = estrai_token(numerical_array_to_string([(tmpBianche + tmpBlack), tmpBianche , tmpBlack]))

    num_token_nere += token_nere_random

    sacchetto = ["B"] * token_bianche_random + ["N"] * num_token_nere

    if num_token_da_estrarre > len(sacchetto):
        raise ValueError("Il numero di token da estrarre supera il numero totale di token nel sacchetto.")
    
    token_estratte = sample(sacchetto, num_token_da_estrarre)
    token_bianche_estratte = token_estratte.count("B") 
    token_nere_estratte = token_estratte.count("N") 
    
    return token_bianche_estratte, token_nere_estratte

