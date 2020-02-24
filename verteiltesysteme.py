from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.static_folder = 'static'
app.debug = True
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST']) #Home seite / Client eingabe
def enter_client():
    if request.method == 'POST': #called by  POST request | first and last name mandatory
        req_data = request.get_json()
        try:
            tel_temp = None if req_data['tel'] == "" else int(req_data['tel'])
        except:
            return render_template('verteiltesysteme.html'), 422

        client = Client(first_name = req_data['first_name'], last_name = req_data['last_name']\
            ,company = req_data['company'], mail = req_data['mail'], tel = tel_temp) #Client objekt erstellt

        db.session.add(client) #client wird zur db hinzugefügt
        db.session.commit() #Änderung werden gespeichert

        return req_data['first_name'] + ' ' + req_data['last_name'] + ' added to client list.'

    return render_template('verteiltesysteme.html') #standard return


@app.route('/query') #DB anfragen via URL arguments
def db_query():
    first = request.args.get('first') #args aus url abfragen
    last = request.args.get('last')
    company = request.args.get('company')
    mail = request.args.get('mail')
    tel = request.args.get('tel')

    sql = "SELECT * FROM client WHERE " #SQL statement zusammen bauen
    sql += "first_name Like '" + first + "'" if first is not None else ""
    sql += "last_name Like '" + last + "'" if last is not None else ""
    sql += "company Like '" + company + "'" if company is not None else ""
    sql += "mail Like '" + mail + "'" if mail is not None else ""
    sql += "tel Like '" + tel + "'" if tel is not None else ""

    if sql == "SELECT * FROM client WHERE ":
        return render_template('suche.html') #falls die Seite ohne args aufgerufen wird

    results = db.engine.execute(text(sql)) #db abruf
    names = []
    for row in results:
        names.append(dict(zip(row.keys(),row))) #ergebnis auswerten
        print(type(row._row))
        print(names[0])
    if len(names) < 1:
        return "<h1>No Entry found</h1>"
    return jsonify(names)
    """return '''<h1>{}</h1>
              <p>Company: {}</p>
              <p>E-Mail: {}</p>
              <p>Tel.: {}</p>'''.format(names[0][1] + " " + names[0][2], names[0][3], names[0][4], names[0][5])"""


#Database Stuff
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80), nullable=False)
    company = db.Column(db.String(80))
    mail = db.Column(db.String(120))
    tel = db.Column(db.Integer, unique=True)

#Im here to run
if __name__ == '__main__':
    app.run()