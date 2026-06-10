

#creo le specifiche tecniche (CLASSE)
class cane:
    nome=""
    anni=0
    razza =""
    box = 0
    __aggr=0

    #costruttore
    #un metodo che serve a customizzare la creazione dell'oggetto
    def __init__(self,nomeRicevuto,anniRicevuti,razzaRicevuta,boxRicevuto):
        self.nome=nomeRicevuto
        self.anni = anniRicevuti
        self.razza =razzaRicevuta
        self.box =boxRicevuto
        self.funzione_Aggr(razzaRicevuta)
        

    #costruttore di default che non va esplicitato


    #metodi
    def globale(self):
        return self.nome + "-" + str(self.anni) + "-" + self.razza + "-" + str(self.box) + "-Aggressività: " + str(self.__aggr)



    def funzione_Aggr(self,razza):
      if razza == 'Carlino':
          self.__aggr = 2
      elif razza == 'Maremmano':
          self.__aggr = 4
      elif razza == 'Lupo':
          self.__aggr = 3
      elif razza == 'Bassotto':
          self.__aggr = 4

    
'''
fido =cane()        #nomeNuovoOggetto = nomeclasse()

pluto= cane()

bianca = cane()

print(type(fido))
print(type(pluto))
print(type(bianca))

print(fido.nome)    #valore della proprietà nome dell'oggetto fido che deriva dall'istanza della classe cane
print(pluto.nome)
print(bianca.nome)

fido.nome="Fido"
pluto.nome="Pluto"
bianca.nome="Bianca"
print(fido.nome)
print(pluto.nome)
print(bianca.nome)
'''

fido = cane("Fido",2,"Lupo",1)
pluto = cane("Pluto",7,"Maremmano",2)
bianca = cane("Bianca",13,"Carlino",1)
#print(fido.nome)
#print(pluto.nome)
#print(bianca.nome)


print(fido.globale())
print(pluto.globale())
print(bianca.globale())

fido.aggr=1
print(fido.globale())
print(fido.aggr)
#print(pluto.aggr)


