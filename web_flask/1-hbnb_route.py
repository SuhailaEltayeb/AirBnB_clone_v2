#!/usr/bin/python3
'''Script to start Flask web application'''
from flask import Flask

def create_app():
    '''creating Flask application'''
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.route('/')
    def hello_hbnb():
        '''Displaying Hello HBNB!'''
        return 'Hello HBNB!'

    @app.route('/hbnb')
    def hbnb():
        '''Displaying HBNB'''
        return 'HBNB'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
