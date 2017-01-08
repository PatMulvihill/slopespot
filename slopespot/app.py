from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

def get_app(settings=None):
    app = Flask(__name__)
    app.config.from_object(settings)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app

def get_db(app):
    db = SQLAlchemy(app)
    db.init_app(app)
    return db

app = get_app(settings=os.environ['APP_SETTINGS'])
db = get_db(app)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    pass
    #app.run(host='0.0.0.0', port=app.config['PORT'])
