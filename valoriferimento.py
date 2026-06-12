
'''
cittaNascita ="Roma"

cittaLavoro=cittaNascita

print(cittaNascita,cittaLavoro)

cittaLavoro="Ancona"

print(cittaNascita,cittaLavoro)


print("Gestione oggetti")
sports =['Nuoto','Tennis','Rugby']

sportPraticati=sports

#print(sports)
#[print(sportPraticati)

sportPraticati.append('Pattinaggio')

#print(sports)
#print(sportPraticati)

#print("NON POSSONO ESSERE COPIATI-LAVORANO PER RIFERIMENTO INDIRIZZO DI MEMORIA")

nuoviSport=sportPraticati

nuoviSport.append('Calcio')

print(sports)
print(sportPraticati)
print(nuoviSport)
'''


def inserisci(nuovo,listaSports):
    listaSports.append(nuovo)
    #return listaSports


sports =['Nuoto','Tennis','Rugby']


altri="s"

while altri == "s":
    nuovoSport = input("Quale nuovo sport vuoi inserire")
    inserisci(nuovoSport,sports)
    #sports.append(nuovoSport)
    altri= input("Hai altri sport da inserire")


print(sports)







