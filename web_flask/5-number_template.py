#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns Hello HBNB!"""
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB"""
    return('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def CText(text):
    """ returns C followed by text"""
    return("C " + text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>', strict_slashes=False)
def PythonText(text="is cool"):
    """ returns Python followed by text or "is cool" as default """
    return("Python " + text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def ifNumber(n):
    """ displays “n is a number” only if n is an integer"""
    return("{:d} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def NumTemplate(n):
    """ display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
