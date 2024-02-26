from random import sample
import random
import time

class RandomBag():

    '''
        _wtoken   --> Numero di token bianchi
        _btoken   --> Numero di token neri
        _etoken   --> Numero di token da estrarre
        _rndToken --> Numero di token da randomizzare

        exbToken --> Numero di token neri estratti
        exwToken --> numero di token bianchi estratti
    '''
    def __init__(self, _wtoken: int = 0, _btoken: int = 0, _etoken: int = 0, _rndToken: int = 0):
        self.wtoken = _wtoken 
        self.btoken = _btoken
        self.eToken = _etoken
        self.rndToken = _rndToken
        self.exbToken = 0
        self.exwToken = 0

    
    '''
        Migliora la randomizzazione
    '''
    def ImprovedRnd(self) -> None:
        rand = random.randint(1, 5)  # Genera un numero casuale di volte per reinizializzare il seed
        for _ in range(rand):
            random.seed(time.time())


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
    

    '''
        Randomizza i token caricati in rndToken fra bianchi e neri
    '''
    def BagRandomizer(self) -> None:
        self.ImprovedRnd()
        self.wtoken = random.randint(0, self.rndToken)
        self.btoken = self.btoken + (self.rndToken - self.wtoken)


    '''
        Randomizza i token caricati in rndToken fra bianchi e neri
    '''
    def extract_token(self) -> 'RandomBag':
        if self.eToken > self.wtoken + self.btoken:
            raise ValueError("The number of tokens to extract exceeds the total number of tokens in the bag.")

        #print(f"Extraction formed as: {self.wtoken}w/{self.btoken}b")

        tokens = ["W"] * self.wtoken + ["B"] * self.btoken
        self.ImprovedRnd()
        extracted_tokens = sample(tokens, self.eToken)
        
        self.exwToken = extracted_tokens.count("W")
        self.exbToken = extracted_tokens.count("B")
        
        return self
    

    def extract_cursed_token(self) -> 'RandomBag':
        if self.eToken > self.rndToken + self.btoken:
            raise ValueError("The number of tokens to extract exceeds the total number of tokens in the bag.")
        
        self.BagRandomizer()
        return self.extract_token()



        
       
