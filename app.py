#config
from flask import Flask
app = Flask(__name__)

#index route
@app.route('/')
def index():
    return 'Hello, this is PetFax!'

#pets route
@app.route('/pets')
def pets():
    return 'These pets are up for adoption!'

#about rout
@app.route('/about')
def about():
    return 'what you know about us? I know all about us!'


