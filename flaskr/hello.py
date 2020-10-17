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
        # regex_email = '[^@]+@[^@]+\.[^@]+'
        regex_bday = '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
        if not (20 > len(firstName) > 0 and 20 > len(lastName) > 0 and 20 > len(username) > 0 and 20 > len(
                password) > 6):
            return "Email/password invalid length", 400
        if not re.search(regex_bday, birthDate):
            return "birthDate invalid format", 400
        # if not re.search(regex_email, email):
        #    return "Record not found email", 400

        data = [firstName, lastName, username, password, email, birthDate]
        print(data)
        try:
            cursor.execute(
                "INSERT INTO users (firstName, lastName ,username, password, email, birthDate) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(
                    data[0], data[1], data[2], data[3], data[4], data[5]))
        except mysql.connector.Error:
            return ("User with username already exists", 400)
        cursor.execute(
            "CREATE TABLE events{0} (name varchar(255), expectedTime int , startDateTime DATETIME, repeatTime varchar(255), numTimesMissed int)".format(
                data[2]))
        cnx.commit()
        return "Success", 200


@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        cursor.execute("DELETE FROM users WHERE username = '{0}' AND password = '{1}'".format(
            username, password))
        cnx.commit()
        return "Success", 200


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        if 20 < len(username) < 6 and 20 < len(password) < 6:
            return "Username/password invalid length", 400
        d = {'username': username, 'password': password}
        return d, 200


@app.route('/event/add', methods=['POST'])
def addEvent():
    if request.method == 'POST':
        username, checkPassword, name, expectedTime, startDateTime, repeat, numTimesMissed = request.form['username'], \
                                                                                             request.form['password'], \
                                                                                             request.form['name'], \
                                                                                             request.form[
                                                                                                 'expectedTime'], \
                                                                                             request.form[
                                                                                                 'startDateTime'], \
                                                                                             request.form['repeat'], \
                                                                                             request.form[
                                                                                                 'numTimesMissed']
        print(username)
        regex_startDateTime = '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9][0-9]'
        if not 0 < len(name) < 20:
            return "Name invalid length", 400
        elif not re.search(regex_startDateTime, startDateTime):
            return "startDateTime invalid format", 400
        elif not repeat in ('daily', 'weekly', 'monthly', 'none'):
            return "repeat invalid format", 400
        cursor.execute(
            "SELECT * FROM users WHERE username='{}'".format(username))
        for (firstName, lastName, username, password, email, birthDate) in cursor:
            print(password, 1, checkPassword)
            if (password == checkPassword):
                cursor.execute(
                    "INSERT INTO events{0} (name, expectedTime, startDateTime, repeatTime, numTimesMissed) VALUES ('{1}','{2}','{3}','{4}','{5}')".format(
                        username, name, expectedTime, startDateTime, repeat, numTimesMissed))
                cnx.commit()
                return "Success", 200
        event_data = [name, expectedTime,
                      startDateTime, repeat, numTimesMissed]
        return "Invalid credentials", 400


@app.route('/event/get', methods=['POST'])
def getEvents():
    if request.method == 'POST':
        username, checkPassword = request.form['username'], request.form['password']
        print(username)
        cursor.execute(
            "SELECT * FROM users WHERE username='{}'".format(username))
        for (firstName, lastName, username, password, email, birthDate) in cursor:
            print(password, 1, checkPassword)
            if password == checkPassword:
                cursor.execute("SELECT * FROM events{0} ".format(username))
                for name, expectedTime, startDateTime, repeat, numTimesMissed in cursor:
                    print(name, expectedTime, startDateTime,
                          repeat, numTimesMissed)
                name, expectedTime, startDateTime, repeat, numTimesMissed = cursor
                d = {'name': name, 'expectedTime': expectedTime, 'startDateTime': startDateTime, 'repeat': repeat,
                     'numTimesMissed': numTimesMissed}
                # execute
                return d
        return "Invalid credentials", 400
