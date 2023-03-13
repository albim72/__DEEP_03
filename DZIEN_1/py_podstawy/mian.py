#import dane
import dane as dn
from dane import nr_filii as filia
from dane import book as ksiazka
from funkcje.bfunkcje import czytaj_liste, czytaj_slownik
from klasy.cdane import CDane


print("________ WYŚWIETELENIE BEZPOŚREDNIE _____________")
print(filia)
print(ksiazka)

print("________ WYŚWIETELENIE ZA POMOCĄ FUNCKJI _____________")

czytaj_liste(filia)
czytaj_slownik(ksiazka)

print("________ WYŚWIETELENIE ZA POMOCĄ OBIEKTU /Klasy/ _____________")
cd = CDane(filia,ksiazka)

cd.czytajlst()
cd.czytajdict()
