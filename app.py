

#django
#Flask

from flask import Flask, request,render_template,jsonify

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



#servizi get/post/put/delete
@app.route('/api/utente', methods=["GET"])
def get_data():
    dati ={"utente2":"mrossi","password":"verdi","citta":"Bolzano"}
    return jsonify(dati)

@app.route('/api/utente', methods=["POST"])
def post_data():
    datiRicevuti = request.get_json()
    print(datiRicevuti)
    datiRicevuti['ricevuti'] ='si'
    return jsonify(datiRicevuti)


@app.route('/api/utente' , methods =['DELETE'])
def delete_data():
    datiCancella = request.get_json()
    ritorno ={"cancellato":"si","idcancellato":datiCancella['id']}
    return jsonify(ritorno)


@app.route('/api/utente', methods=['PUT'])
def change_data():
    datiCancella = request.get_json()
    datiCancella['user']="Pierbaldo"
    return jsonify(datiCancella)



#avvio il server 
if __name__ == '__main__':
    app.run()
