

#importiamo il modulo per ODBC
import pyodbc

#la lista dei driver odbc installati
print(pyodbc.drivers())

#sql server
conn = pyodbc.connect( 'DRIVER={SQL Server};SERVER=DESKTOP-CO7TSJQ\\SQLEXPRESS;DATABASE=pythonDB;UID=sa;PWD=Coletti_1' )

cursor = conn.cursor()

cursor.execute('select * from immobili')

righe =cursor.fetchall()



for riga in righe:
    #print(type(riga))
    print(riga.Descrizione,riga.mq,riga.Proprietario,riga.idstanza)


#inserimento
cursor.execute("insert into Immobili (Descrizione,mq,Proprietario) values ('Salotto',25,'Gino')")

conn.commit()

cursor.close()
conn.close()

print("Fine connessione ai dati")

