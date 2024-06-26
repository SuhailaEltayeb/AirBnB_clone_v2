#!/usr/bin/python3
'''Script to start Flask web application'''
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    '''Displaying 'Hello HBNB!' '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''Displaying 'HBNB' '''
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    '''Displaying 'C' followed by text variable value '''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_is_cool(text):
    '''Displaying 'Python' followed by  text variable value '''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    '''Displaying 'n is a number' only if n is integer '''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    '''Displaying an HTML page only if n is integer '''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    '''Displays whether intiger is even or odd '''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
