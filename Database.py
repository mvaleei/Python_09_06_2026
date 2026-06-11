

#importiamo il modulo per ODBC
import pyodbc

#la lista dei driver odbc installati
#print(pyodbc.drivers())

#sql server
conn = pyodbc.connect( 'DRIVER={SQL Server};SERVER=DESKTOP-CO7TSJQ\\SQLEXPRESS;DATABASE=pythonDB;UID=sa;PWD=Coletti_1' )

cursor = conn.cursor()

cursor.execute('select * from immobili')

righe =cursor.fetchall()

print(type(righe))

for riga in righe:
    #print(type(riga))
    print(riga.Descrizione,riga.mq,riga.Proprietario,riga.idstanza)


#insert
cursor.execute("insert into immobili (mq,Descrizione,Proprietario) values (30,'Garage','Fabio')")
cursor.execute("insert into immobili (mq,Descrizione,Proprietario) values (120,'Sala','Angelo')")


cursor.commit()



print("Fine connessione ai dati")

