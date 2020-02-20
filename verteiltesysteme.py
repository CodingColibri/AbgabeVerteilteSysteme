from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST']) #allow GET & Post requests
def test():
    if request.method == 'POST': #called by  POST request | first and last name mandatory
        req_data = request.get_json()

        """first_name = request.form.get('first_name')
        last_name = request.form['last_name']
        company = request.form.get('company')
        mail = request.form.get('mail')
        tel = request.form.get('tel')"""

        client = Client(first_name = req_data['first_name'], last_name = req_data['last_name']\
            ,company = req_data['company'], mail = req_data['mail'], tel = int(req_data['tel']))

        db.session.add(client)
        db.session.commit()

        return 'POST ist da'

    return render_template('verteiltesysteme.html') #standard return

#call: /query?name=<value>&mandatory=<value>
@app.route('/query')
def test_query():
    name = request.args.get('name')
    mandatory = request.args['mandatory'] #no .get -> Error 400 for none value

    return '''<h1>The name is: {}</h1>
              <h2>The mandatory value is: {}</h2>'''.format(name, mandatory)


#Database Stuff
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True)
    last_name = db.Column(db.String(80), unique=True, nullable=False)
    company = db.Column(db.String(80))
    mail = db.Column(db.String(120))
    tel = db.Column(db.Integer, unique=True)


if __name__ == '__main__':
    app.run()