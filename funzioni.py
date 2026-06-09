

def funzione1():
    print("Sono una funziona che lavora in modo autonomo")


funzione1()
    





def funzione2(citta):  #,valore2,valore3......
    if citta == "Padova":
        print("Ti trovi nel nord Italia")
    else:
        print("Sei in altro posto")


funzione2("Livorno")
funzione2("Padova")






def funzione3():
    #
    #
    #
    return "Sono la funzione3",1600,[10,30,60]


variabile=funzione3()
print(variabile)





def funzione4(anni):
    tipo=""
    if anni>17:
        tipo = "Maggiorenne"
    else:
        tipo="Minorenne"
    return tipo


tipologia =funzione4(23)
tipologia2=funzione4(15)

print(tipologia,tipologia2)



#Le funzioni 2 e 4, sono provviste di firma (parametri richiesti e inseriti tra le ()   
