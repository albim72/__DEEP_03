import numpy as np
import matplotlib.pyplot as plt

#deklaracja danych
x1 = np.linspace(0.0,5)
y1 = np.cos(2*np.pi*x1)*np.exp(-x1)

x2 = np.linspace(0.0,2)
y2 = np.cos(2*np.pi*x1)

#kreślenie wykresu

fig,(ax1,ax2) = plt.subplots(2,1)
fig.suptitle("dwa wykresy: drgania tłumione i nietłumione")

ax1.plot(x1,y1,'o-')
ax1.set_ylabel('amplituda drgań tłumionych')

ax2.plot(x2,y2,'.-')
ax2.set_ylabel('amplituda drgań nietłumionych')
ax2.set_xlabel('czas [s]')

plt.show()

labels = 'Warszawa','Kraków','Lublin','Katowice','Gdańsk'
sizes = [56,34,26,24,30]
explode = (0,0.1,0,0,0.2)

fig,ax = plt.subplots()
ax.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%',shadow=True,startangle=90)
ax.axis()
plt.show()
