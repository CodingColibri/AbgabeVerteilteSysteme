from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('verteiltesysteme.html')

#call: /query?name=<value>&mandatory=<value>
@app.route('/query')
def test_query():
    name = request.args.get('name')
    mandatory = request.args['mandatory'] #no .get -> Error 400 for none value

    return '''<h1>The name is: {}</h1>
              <h2>The mandatory value is: {}</h2>'''.format(name, mandatory)

if __name__ == '__main__':
    app.run()