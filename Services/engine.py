import re
from typing import Tuple
from Classes.random_bag import RandomBag

class Engine():

    '''
        Decodifica i comandi inviati tramite regex, e ritorna i numeri interi nella frase

        param: <sentence> - comando in ingresso inserito da un utente

        return: <lista> - numeri interi estratti dal comando
    '''
    def extract_integers_from_sentence(self, sentence: str) -> list:
        integer_pattern = r'\b\d+\b'
        match = re.search(integer_pattern, sentence)
        if match:
            integer_values = re.findall(integer_pattern, sentence)
            integer_values = [int(value) for value in integer_values]
            return integer_values
        else:
            return []
        

    '''
        La funzione converte un array in una stringa separata dal carattere ','

        param: <valori> - lista (array) di numeri interi

        return: <str> contenente i numeri interi separati da virgola
    '''    
    def numerical_array_to_string(self, valori : list) -> str:
        # Converti ogni valore numerico in una stringa
        valori_str = [str(valore) for valore in valori]
        # Unisci le stringhe separate da una virgola
        return ", ".join(valori_str)
            

    """
        Simula l'estrazione di token da un sacchetto contenente Tupla 

        sta roba deve diventá un oggetto

        - num_token_bianche token bianche 
        - num_token_nere token nere.
        
        :param num_token_da_estrarre: Numero di token da estrarre dal sacchetto.
        :param num_token_bianche: Numero di token bianche nel sacchetto.
        :param num_token_nere: Numero di token nere nel sacchetto.
        
        :return: Una tupla contenente il numero di token bianche e nere estratte (int, int).
    """
    def simple_trail(self, lowered : str) -> 'RandomBag':

        numbers = self.extract_integers_from_sentence(lowered) # decode the command params

        if not numbers and len(numbers) < 2:
            raise ValueError('Invalid Params for function simple trail')
        
        eToken = numbers[0]
        wToken = numbers[1]
        bToken = numbers[2]

        return RandomBag(wToken, bToken, eToken).extract_token()


    """
        Simula un l'estrazione di num_token_da_estrarre token da un sacchetto contenente
        num_token_bianche token bianche e num_token_nere token nere.
        
        :param num_token_da_estrarre: Numero di token da estrarre dal sacchetto.
        :param num_token_bianche: Numero di token bianche nel sacchetto.
        :param num_token_nere: Numero di token nere nel sacchetto.
        :return: Una tupla contenente il numero di token bianche e nere estratte (int, int).
    """
    def confused_trail(self, lowered: str) -> Tuple[int, int]:

        numbers = self.extract_integers_from_sentence(lowered) # decode the command params

        eToken = numbers[0]
        rndToken = numbers[1]
        btoken = numbers[2]

        return RandomBag(0, btoken, eToken, rndToken).extract_cursed_token()

    
