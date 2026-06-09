

#list       dinamiche sia nel tipo di dato che nella dimensione
'''
frutta=["Mela","Arancio","Susina",1500,True,[50,60,20,19,55]]

print(type(frutta))

print(len(frutta))

print(frutta[0])

frutta[1]='Melone'

print(frutta)

frutta.append("Arancio")

print(frutta)

nuovaFrutta=["Cocomero","Ananas","Mango"]


programmazione imperativa
for fruit in nuovaFrutta:
    print(fruit)
    frutta.append(fruit)

print(frutta)



#programmazione funzionale
frutta.extend(nuovaFrutta)

print(frutta)

print(frutta[5])

print(frutta[5][3])


citta="San Benedetto del Tronto"
for carattere in citta:
    print(carattere)


for f in frutta:
    for oggetto in f:
        print(oggetto)
    #print(f)


#frutta.sort()#SOLO PER LISTE CONTENENTI DATI DELLO STESSO TIPO  
#print(frutta)


anni=[80,60,12,90,45]

anni.sort()
print(anni)

frutta.append("Mela")
frutta.append("Mango")
print(frutta)


#filtri delle liste
def filtro(fruttoDaLeggere):
    if fruttoDaLeggere == "Mango":
        return True
    return False

datiFiltrati = filter(filtro, frutta )

print(list(datiFiltrati))

persona ="Dario,Grigi,45,Domodossola,Dirigente,Viale Angelico, 69"
print(type(persona))
nuovaLista = persona.split(',')
print(len(nuovaLista))


#tupla      totalmente statico come valori e dimensione
sport = ("Nuoto","Tennis","Calcio","Rugby")
print(type(sport))
#sport.append("Pallavolo")


#sport[0]="Polo"

#sport.sort()

tuplaOrdinata = sorted(sport)

print(type(tuplaOrdinata))
print(tuplaOrdinata)




#set        #non accettano valori duplicati
citta = {"Roma","Napoli","Milano","Napoli"}
print(citta)
citta.add("Parma")
print(citta)
citta.add("Milano")
print(citta)

setOrdinato = sorted(citta)
print(type(setOrdinato))
print(setOrdinato)

print(citta)

nuovaCitta = list(citta)
print(type(nuovaCitta))
'''


#dict (dictionary)
persona ={"nome":"Mario","cognome":"Rossi","anni":42}
print(type(persona))
print(persona)

print(persona['cognome'])

persona["indirizzo"]="Piazza Albania"

print(persona)


print(persona.keys())

for chiave in persona:
    #print(chiave)
    print(persona[chiave],chiave)

