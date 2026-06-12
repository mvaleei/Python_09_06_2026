

#django
#Flask

from flask import Flask, request,render_template

app = Flask(__name__)


'''
#il codice per interagire con il client
@app.route('/')     #url da ricevere
def homemia():
    return "Sono la home page del sito"


@app.route('/taghtml')
def tagHTML():
    return '<h1>Pagina di tag html. Tornati dal server</h1>'
'''

@app.route('/')
def homepage():
    print('carico la home page')
    return render_template('Home.html')


@app.route('/registra')
def registrare():
    return render_template('Inserisci.html')



@app.route('/inserimento', methods=['POST'])
def ricezioneDati():
    user = request.form['nomeUtente']
    password =request.form['passwordUtente']
    print(user,password)

    print("Sto per ricevere i dati dal form del front-end")
    #return render_template('Loggato.html', nomeInserito = user , passwordInserita=password)
    return render_template('Loggato.html', dati =[ user ,password])

#avvio il server 
if __name__ == '__main__':
    app.run()
