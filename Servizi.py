

#importare il modulo per collegarmi verso l'esterno
import requests



#dichiarare l'url da contattare
urlChiamato ="https://jsonplaceholder.typicode.com/users"


#chiamata GET
chiamata = requests.get(urlChiamato)


print(type(chiamata))

datiConvertiti = chiamata.json()

print(type(datiConvertiti))

print(len(datiConvertiti))

for utente in datiConvertiti:
    #print(type(utente))
    print(utente["username"],utente["email"],utente["name"],utente["address"]["geo"]["lat"])


#post
nuovoutente ={"id":99, "name":"Pippo snc","username":"User di prova","email":"Pippo@pippo.it"}
utenteInserito = requests.post(urlChiamato, json=nuovoutente)

utenteRicevuto = utenteInserito.json()
print(type(utenteRicevuto))

print(utenteRicevuto)




print("Fine programma")
