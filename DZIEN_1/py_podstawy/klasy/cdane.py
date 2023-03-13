from funkcje.bfunkcje import *

class CDane:

    def __init__(self,lista,slownik):
        self.lista=lista
        self.slownik=slownik

    def czytajlst(self):
        return czytaj_liste(self.lista)
    
    def czytajdict(self):
        return czytaj_slownik(self.slownik)
