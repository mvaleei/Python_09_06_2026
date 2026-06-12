


#pip install pandas
#pip install openpyxl

#importo pandas
import pandas as pn

'''
import requests


url = "https://jsonplaceholder.typicode.com/users"

risposta = requests.get(url)

datiConvertiti = risposta.json()

#print(len(datiConvertiti))


oggettoDatiGlobali = pn.DataFrame(datiConvertiti,columns=["name","username","email"])

print(oggettoDatiGlobali)
print(type(oggettoDatiGlobali))
'''


datiFile = pn.read_csv("FattureVirgola.csv", header=0,sep=',')
#print(type(datiFile))


solounaColonna = datiFile['nome']
#print(solounaColonna)
#print(type(solounaColonna))

dueoPiuColonne = datiFile[  ['nome', 'Importo'] ]

#print(dueoPiuColonne)
#print(type(dueoPiuColonne))


#aggiunta di una colonna con valore asseganto
#datiFile['Fatturato']="Annuale"
#print(datiFile)


#creato una nuova colonna, in base a dei criteri
datiFile['BuonFatturato']= datiFile['Importo']>=3000
#print(datiFile)

datiFile['Ivato'] = datiFile['Importo'] + datiFile['Importo']*22/100
#print(datiFile)



#creo una nuova colonna con lo sconto, MA solo a chi ha speso almeno 2000 euro
def calcoloSconto(singolaFattura):
    if singolaFattura.Importo >2000:
        return singolaFattura.Importo- singolaFattura.Importo*10/100
    else:
        return singolaFattura.Importo

datiFile['Importo Scontato'] = datiFile.apply(calcoloSconto,axis=1)

#print(datiFile)


#dimensione dell'oggetto
#print(datiFile.shape)

dimensione=datiFile.shape
#print(type(dimensione))

#prime 5 righe
#print(datiFile.head())

#ultime 5 righe
#print(datiFile.tail())


#fornisce informazioni statistiche sulla tabella
#print(datiFile.describe())



#print('Inizio raggruppamento')
datiRaggruppati = datiFile.groupby(['cognome'])['Importo'].mean()#.min()#.max()
#print(datiRaggruppati)

#importiamo un file excel puro
fileLetto = pn.read_excel('fatture.xlsx')
#print(fileLetto)
#print(type(fileLetto))
#print(fileLetto['Importo'][4])

fileLetto['Saldare'] ='SI'
#print(fileLetto)

fileLetto.to_excel('Scritto.xlsx',sheet_name='Python pandas')


#print(datiFile)
#creare un documento esportabile, mediante dei filtri applicati

#creo un oggeto che contiene il filtro da applicare
maschera =  datiFile['BuonFatturato'] == True


#applicao il filtro
datiFiltrati = datiFile[maschera]

print(datiFiltrati)

datiFiltrati.to_excel("Filtro.xlsx",sheet_name="Fatturato ottimale")


#rinominamo le clonne del nuovo oggetto
nuoviDati =datiFiltrati[['nome','Importo']]  #elenca le colonne da rinominare

nuoveColonne =['Nominativo Cliente','Imponibile']  #crei i  nuovi nomi (delle colonne)

nuoviDati.columns=nuoveColonne   # assegna i nuovi nomi alle vecchie colonne

print(nuoviDati)

nuoviDati.to_excel("Commerciale.xlsx",sheet_name="Marketing")



