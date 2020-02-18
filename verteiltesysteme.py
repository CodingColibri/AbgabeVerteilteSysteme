from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('verteiltesysteme.html')

"""
    use: export FLASK_APP=verteiltesysteme.py 
    and: flask run 
"""

