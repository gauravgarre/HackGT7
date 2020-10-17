from flask import Flask, Response
from flask import request
import mysql.connector
import mysql
import uuid
import re

cnx = mysql.connector.connect(user='root', password='dreamTeam135',
                              host='104.198.46.183',
                              database='users')
cnx.database = 'users'
cursor = cnx.cursor()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        birthDate = request.form['birthDate']
        #regex_email = '[^@]+@[^@]+\.[^@]+'
        regex_bday = '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
        if not (20 > len(firstName) > 0 and 20 > len(lastName) > 0 and 20 > len(username) > 0 and 20 > len(password) > 6):
            return "Record not found", 400
        if not re.search(regex_bday, birthDate):
            return "Record not found", 400
        # if not re.search(regex_email, email):
        #    return "Record not found email", 400

        data = [firstName, lastName, username, password, email, birthDate]
        print(data)
        try:
            cursor.execute("INSERT INTO users (firstName, lastName ,username, password, email, birthDate) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(
            data[0], data[1], data[2], data[3], data[4], data[5]))
        except mysql.connector.Error:
            return ("User with username already exists",400)
        cursor.execute("CREATE TABLE events{0} (name varchar(255), expectedTime int , startDateTime DATETIME, repeatTime varchar(255), numTimesMissed int)".format(data[0]))
        cnx.commit()
        return "Success", 200
        
@app.route('/delete',methods=['POST'])
def delete():
    if request.method == 'POST':
        username, password = request.form['username'],request.form['password']
        cursor.execute("DELETE FROM users WHERE username = '{0}' AND password = '{1}'".format(username, password))
        cnx.commit()
        return "Success", 200

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        if 20 < len(username) < 0 and 20 < len(password) < 6:
            return "Record not found", 400
        #cursor.execute("")
        #cnx.commit()
        return "Success", 200