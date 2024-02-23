from random import sample
from typing import Tuple
import random

def estrai_fiche(num_fiche_da_estrarre: int, num_fiche_bianche: int, num_fiche_nere: int) -> Tuple[int, int]:
    
    """
    Simula l'estrazione di num_fiche_da_estrarre fiche da un sacchetto contenente
    num_fiche_bianche fiche bianche e num_fiche_nere fiche nere.
    
    :param num_fiche_da_estrarre: Numero di fiche da estrarre dal sacchetto.
    :param num_fiche_bianche: Numero di fiche bianche nel sacchetto.
    :param num_fiche_nere: Numero di fiche nere nel sacchetto.
    :return: Una tupla contenente il numero di fiche bianche e nere estratte (int, int).
    """
    sacchetto = ["B"] * num_fiche_bianche + ["N"] * num_fiche_nere

    if num_fiche_da_estrarre > len(sacchetto):
        raise ValueError("Il numero di fiche da estrarre supera il numero totale di fiche nel sacchetto.")
    
    fiche_estratte = sample(sacchetto, num_fiche_da_estrarre)
    fiche_bianche_estratte = fiche_estratte.count("B")
    fiche_nere_estratte = fiche_estratte.count("N")
    
    return fiche_bianche_estratte, fiche_nere_estratte


def confusion(num_fiche_da_estrarre: int, num_fiche_random: int, num_fiche_nere: int) -> Tuple[int, int]:
    
    """
    Simula l'estrazione di num_fiche_da_estrarre fiche da un sacchetto contenente
    num_fiche_bianche fiche bianche e num_fiche_nere fiche nere.
    
    :param num_fiche_da_estrarre: Numero di fiche da estrarre dal sacchetto.
    :param num_fiche_bianche: Numero di fiche bianche nel sacchetto.
    :param num_fiche_nere: Numero di fiche nere nel sacchetto.
    :return: Una tupla contenente il numero di fiche bianche e nere estratte (int, int).
    """

    # Randomizzazione delle fish, tra bianche e nere, prima dell'estrazione finale
    tmpBianche = random.randint(0,num_fiche_random)
    tmpBlack = num_fiche_random - tmpBianche
    fiche_bianche_random, fiche_nere_random = estrai_fiche((tmpBianche + tmpBlack), tmpBianche , tmpBlack)

    num_fiche_nere += fiche_nere_random

    sacchetto = ["B"] * fiche_bianche_random + ["N"] * num_fiche_nere

    if num_fiche_da_estrarre > len(sacchetto):
        raise ValueError("Il numero di fiche da estrarre supera il numero totale di fiche nel sacchetto.")
    
    fiche_estratte = sample(sacchetto, num_fiche_da_estrarre)
    fiche_bianche_estratte = fiche_estratte.count("B") 
    fiche_nere_estratte = fiche_estratte.count("N") 
    
    return fiche_bianche_estratte, fiche_nere_estratte


# Esempio di utilizzo
num_fiche_da_estrarre = 3
num_fiche_da_randomizzare = 4
num_fiche_bianche = 5 # solo per estrazione normale
num_fiche_nere = 2

#fiche_bianche_estratte, fiche_nere_estratte = estrai_fiche(num_fiche_da_estrarre, num_fiche_bianche, num_fiche_nere)
fiche_bianche_estratte, fiche_nere_estratte = confusion(num_fiche_da_estrarre, num_fiche_da_randomizzare, num_fiche_nere) # num_fiche_bianche = numero di fiche random in questo caso
print(f"Fiche bianche estratte: {fiche_bianche_estratte}, Fiche nere estratte: {fiche_nere_estratte}")