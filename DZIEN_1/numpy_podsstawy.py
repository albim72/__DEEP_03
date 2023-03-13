import numpy as np

zero = np.zeros(9)
print(zero)

jeden = np.ones(5)
print(jeden)

lista = np.array(["Piotr","Anna","Ula","Olga","Olaf"])
print(lista)

imie = ["Piotr","Anna","Ula","Olga","Olaf"]

print(imie)
print(type(lista))
print(type(imie))

n = np.arange(1,77,3)
print(n)

k= np.linspace(0,10,num=5)
print(k)

kl = (9,5,6,8.88,9,1.2)
npk = np.array(kl)
print(npk)
print(type(npk))

zb = {6,9,0,123,6,56,8,9,12,33}
print(zb)
npz = np.array(zb)
print(npz)
print(type(npz))
