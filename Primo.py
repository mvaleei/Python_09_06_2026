

#commento su una riga

'''
commento su più righe
commento su più più righe

debolmente tipizzato: Non obbliga a dichiarare il tipo di dato
OGNI VARIABILE è UN OGGETTO

Orientato agli oggetti


scripting/compilato (semicompilato)

linguaggio posizionale


'''

nome="Carlo"

print(nome)
print(type(nome))

nome=500

print(nome)
print(type(nome))

nome='Piero'
anni=33
maggiorenne=False#True   #true/false

print(type(nome))
print(type(anni))
print(type(maggiorenne))

if anni>17:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")



cognome,citta,annilavorativi="Verdi","Firenze",66

if anni == 66:
    print("Sei adulto")  #è obbligatorio
elif anni==25:              #non obbligatori
    print("Sei giovane")
elif anni <18:
    print("Sei una teen ager")
else:                       #non obbligatorio
    print("Età non contemplata")


while anni >18 :
    print("Sei maggiorenne")
    #obbligo a far diventare falsa la condizione
    #anni = anni-1
    anni -=1  #-=  +=  *=  /=


entrare =True

while entrare == True:
    print("Sono nel ciclo while")
    entrare =False

for pippo in nome:
    print('Il carattere letto è: ' + pippo)


serieNumeri = range(0,10)


for numeroLetto in serieNumeri:
    print(numeroLetto)

numeroCaratteri = range(0,len(nome))

for numero in numeroCaratteri:
    print(nome[numero])

stringa ="1500"

stringaConvertita = int(stringa)

numMio =6000

numeroConvertito = str(numMio)

print(type(stringaConvertita))
print(type(numeroConvertito))

print(stringa,numMio,maggiorenne)   #conversione implicita - vale solo per il print

#interazione con l'utente
nomeDigitato=input("Qual'è il tuo nome")
print("Il nome dichiarato è: ",nomeDigitato)

anni=input("Quanti anni hai")
print(type(anni))


