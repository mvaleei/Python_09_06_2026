

class appartamento:
    mq=0
    citta=""
    indirizzo=""


    def __init__(self,mq,citta,indirizzo):
        self.mq=mq
        self.citta=citta
        self.indirizzo=indirizzo


    def riepilogo(self):
        ritorno=  "Citta:" + self.citta
        ritorno += " - Indirizzo:" + self.indirizzo
        ritorno += " - mq: " + str(self.mq)
        return ritorno

    def costototale(self,costomq):
        return self.mq*costomq



class villa(appartamento):
    #citta=""
    #mq=0
    #indirizzo=""
    trattativa=""



    def __init__(self,citta,mq,indirizzo,trattativa):
        #per creare la classe figlia, devo prima  chiamare il costruttore della classe padre
        #il costruttore della classe padre VA SEMPRE inserito come PRIMA RIGA DEL
        #costruttore della classe figlio
        super().__init__(mq,citta,indirizzo)  #la chiamata al costruttore della classe padre
        #self.mq=mq
        #self.citta=citta
        #self.indirizzo=indirizzo
        self.trattativa=trattativa

    def riepilogo(self):
        return "ciao"

    def totale(self):
        #ritorno=  "Citta:" + self.citta
        #ritorno += " - Indirizzo:" + self.indirizzo
        #ritorno += " - mq: " + str(self.mq)
        ritorno = super().riepilogo() + " - trattativa: " + self.trattativa
        return ritorno

    @staticmethod   #metodo utilizzato senza istanziare la classe
    def visualizzaTipoTrattativa():
        return "valori possibili della proprietà trattativa: Privata/Pubblica"


roma = appartamento(90,"Roma","Viale Europa, 55")
milano = appartamento(75,"Milano","Via Montenapoleone,1")
napoli = appartamento(100,"Napoli","Piazza Garibaldi,6")

print(roma.riepilogo())
print(milano.riepilogo())
print(napoli.riepilogo())

print("L'immobile di roma costa: ", roma.costototale(4500))
print("L'immobile di napoli costa: ", napoli.costototale(3700))
print("L'immobile di milano costa: ", milano.costototale(6400))
        

parioli = villa("Roma",120,"Viale parioli, 160","Pubblica")
grosseto = villa("Grosseto",180,"Via Roma, 160","Privata")
print(parioli.totale())
print(grosseto.totale())


#generico = villa("Pippo",0,"minni","")
print(villa.visualizzaTipoTrattativa())


