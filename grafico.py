

import matplotlib.pyplot as plt
import pandas as pn
import numpy as np

datiFile = pn.read_csv("Fatturazionen1.csv", header=0)



print(datiFile)


y = datiFile['importo']
x = np.arange(0,len(y))


'''
plt.figure(figsize=(7,4))



plt.title('Fatturato annuo')


plt.xlabel('Ascissa: Lista fatture')
plt.ylabel('Ordinata: Importo')

plt.axhline( y=y.mean() , c="y", linestyle='dotted' )
'''


#multigrafico
plt.figure(figsize=(15,15))
plt.subplot(2,2,1 )
plt.plot(x,y)


plt.subplot(2,2,2)
plt.scatter(x,y,c='orange')


#plt.figure(figsize=(4,4))
plt.subplot(2,2,3 )
plt.plot(x,y)


plt.subplot(2,2,4)
plt.scatter(x,y,c='blue')


plt.plot(x,y)

plt.show()
