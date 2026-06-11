

#importo il modulo per collegarmi  verso l'esterno
import requests

#importo il modulo per leggere contenuti di pagine web
from bs4 import BeautifulSoup


#leggiamo la pagina
urlChiamato ="http://www.inps.it"
sitoweb = requests.get(urlChiamato)

print(sitoweb)

#convertire i dati ricevuti (stringhe) in dati leggibili
datihtml = BeautifulSoup(sitoweb.content,'html.parser')

print(datihtml)


tagh2= datihtml.h2      #il primo tag  di tipo h2

print(tagh2)
print(tagh2.text)

tuttitagh2 = datihtml.find_all('h2')

print(len(tuttitagh2))
for tagh2letto in tuttitagh2:
    print('\n', tagh2letto.text)

#leggiamo il contenuto di un tag con id assegnato
lingua = datihtml.find(id = 'browserObsoletoLang')
print(lingua)
print("La lingua del sito è: ", lingua.text)


#leggiamo i dati in base alla classe e al tipo di tag
tagClasse = datihtml.find_all ('a',class_='nav-link')

print(len(tagClasse))

for ancor in tagClasse:
    print(ancor.text)

