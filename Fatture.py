

importo = int(input("Importo fattura"))


prodotto =input("Tipologia prodotto: A/E/I/L")


iva =0

descrizione=""

if prodotto =="A":
    iva =5
    descrizione="Alimentari"
elif prodotto =="E":
    iva =10
    descrizione="Edilizia"
elif prodotto =="I":
    iva =22
    descrizione="Informatica"
elif prodotto =="L":
    iva =45
    descrizione="Lusso"

saldo=importo + importo*iva/100

print("Con il prodotto di tipologia: ", descrizione, " hai un’iva al: ", iva , "% e un saldo di: ", saldo)

