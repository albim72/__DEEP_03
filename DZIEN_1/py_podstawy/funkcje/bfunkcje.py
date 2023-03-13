def czytaj_liste(lista):
    for i,j in enumerate(lista):
        # (i,j) -> i -> indeks elementu, j -> wartość elementu
        print(f"Element listy nr {i+1} o wartości: {j}")
        
def czytaj_slownik(slownik):
    for key,value in slownik.items():
        print(f"--> klucz: {key}, wartość: {value}")
