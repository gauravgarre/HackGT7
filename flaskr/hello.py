from flask import Flask, Response
from flask import request
#import re

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['firstName']
        username = request.form['firstName']
        password = request.form['firstName']
        email = request.form['firstName']
        birthDate = request.form['firstName']

        max = 50
        #regex_email = '[^@]+@[^@]+\.[^@]+'

        if len(firstName) > max and len(lastName) > max and len(username) > max and len(password) > max and len(
                birthDate) > max:
            return "Record not found", 400
        #if not re.search(regex_email, email):
        #    return "Record not found email", 400

        data = [firstName, lastName, username, password, email, birthDate]
        return "Success", 200
