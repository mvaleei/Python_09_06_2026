

#funzione per gestire l'afggressività data la razza
aggre ={"Carlino":2,"Lupo":3,"Maremmano":4,"Bassotto":4}


def aggr(descr):
    valoreAggressivita=0
    if descr == "Carlino":
        valoreAggressivita=2
    elif descr == "Lupo":
        valoreAggressivita=3
    elif descr == "Maremmano":
        valoreAggressivita=4
    elif descr == "Bassotto":
        valoreAggressivita=4
    return valoreAggressivita
    



def controlla(boxDesiderato,listaCani):
    nuovaLista=[]
    for dog in listaCani:
        if dog["box"] == boxDesiderato:
            nuovaLista.append(dog)
    return nuovaLista



def media(listaCani):
    sommaAnni=0
    for dog in listaCani:
        sommaAnni += int( dog["anni"])
    return len(listaCani),sommaAnni
        
    


#input
canile=[]

altri="s"
while altri =="s":
    nome=input("Nome del cane")
    anni=input("Anni del cane")
    razza =input("Razza del cane")
    box = input("Box di inserimento")

    #compongo l'oggetto cane da inserire nella lista (definita ad inizio programma)
    cane = {"nome":nome,"anni":anni,"razza":razza,"box":box,"aggressivita":aggr(razza)}  #aggre[razza]}

    #aggiungo il cane nel canile
    #prima di aggiungere, controllo la presenza di massimo 1 cane
    #altrimenti non posso aggiungere
    if len(controlla(box,canile)) <2:
        canile.append(cane)
    else:
        print("Attenzione box saturo")
    

    altri = input("Hai altri cane da inserire")

#elaborazione
statistica=media(canile)
print("La media degli anni inseriti è: ", statistica[1]/statistica[0] )


#print(canile)


#output
altri="s"
while altri=="s":
    filtro=input("Di quale box, vuoi conoscere la lista dei cani")

    #presento la lista dei cani
    filtrati=controlla(filtro,canile)

    for dog in filtrati:
        print(dog["nome"],dog["anni"],dog["razza"],dog["aggressivita"])   


    altri=input("Vuoi consultare un altro box: s/n")
    



    
