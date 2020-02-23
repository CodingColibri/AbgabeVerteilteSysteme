from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.static_folder = 'static'
app.debug = True
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST']) #allow GET & Post requests
def enter_client():
    if request.method == 'POST': #called by  POST request | first and last name mandatory
        req_data = request.get_json()

        client = Client(first_name = req_data['first_name'], last_name = req_data['last_name']\
            ,company = req_data['company'], mail = req_data['mail'], tel = int(req_data['tel']))

        db.session.add(client)
        db.session.commit()

        return req_data['first_name'] + ' ' + req_data['last_name'] + ' added to client list.'

    return render_template('verteiltesysteme.html') #standard return

#call: /query?name=<value>&mandatory=<value>
@app.route('/query')
def test_query():
    first = request.args.get('first')
    last = request.args.get('last')
    company = request.args.get('company')
    mail = request.args.get('mail')
    tel = request.args.get('tel')

    sql = "SELECT * FROM client WHERE "
    sql += "first_name Like '" + first + "'" if first is not None else ""

    results = db.engine.execute(text(sql))
    names = []
    for row in results:
        names.append(list(row._row))
        print(type(names[0]))

    print (names[0][3])
    return '''<h1>{}</h1>
              <p>Company: {}</p>
              <p>E-Mail: {}</p>
              <p>Tel.: {}</p>'''.format(names[0][1] + " " + names[0][2], names[0][3], names[0][4], names[0][5])

@app.route('/getclient', methods=['POST', 'GET'])
def get_client():
    if request.method == 'POST':
        req_date = request.get_json()
    return None

#Database Stuff
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80), nullable=False)
    company = db.Column(db.String(80))
    mail = db.Column(db.String(120))
    tel = db.Column(db.Integer, unique=True)


if __name__ == '__main__':
    app.run()