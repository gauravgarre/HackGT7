# import mysql.connector
# import mysql
import datetime
import json
import requests

"""
cnx = mysql.connector.connect(user='root', password='dreamTeam135',
                              host='104.198.46.183',
                              database='users')
cnx.database = 'users'
cursor = cnx.cursor()
"""
username = 'username'
password = 'password'
name = "Math Test"
type = 'assignment'
startDateTime = '2020-10-03 12:22'
endDateTime = '2020-10-07 17:23'
expectedTime = 60
repeat = 'weekly'
numTimesMissed = 0

# assuming eventType, expectedTime, startDateTime, endDateTime, numTimesMissed is defined
def suggestEvent():
    date1, time1 = startDateTime.split()
    date2, time2 = endDateTime.split()
    datetime1 = datetime.datetime(int(date1[:4]), int(date1[5:7]), int(date1[8:]), int(time1[:2]), int(time1[3:]))
    datetime2 = datetime.datetime(int(date2[:4]), int(date2[5:7]), int(date2[8:]), int(time2[:2]), int(time2[3:]))
    days = datetime2.day - datetime1.day
    eventdts = []
    session_ = []
    if type == 'test':
        """
        session = expectedTime // 3
        session_.append(session)

        delta = ((datetime2 - datetime1) - timedelta(minutes=expectedTime)) / 3
        ts = []
        datetimex = datetime2
        while datetimex > datetime1:
            datetimex -= timedelta(minutes=session) + delta
            ts.append(datetimex)
        """
        ts = []
        days_split = days // 3
        session = expectedTime // 3
        session_.append(session)
        datetimex = datetime1
        while datetimex.day < datetime2.day - 1:
            datetimex += datetime.timedelta(days=days_split)
            datetimex = datetimex.replace(hour=20)
            datetimex = datetimex.replace(minute=0)
            ts.append(datetimex)

        for i in range(len(ts)):
            startDateTimex = str(ts[i].year)+'-'+str(ts[i].month).zfill(2)+'-'+str(ts[i].day).zfill(2)+' '+str(ts[i].hour).zfill(2)+':'+str(ts[i].minute).ljust(2, '0')
            eventdts.append(startDateTimex)

    elif type == 'quiz':
        ts = []
        days_split = days // 3
        session = expectedTime // 3
        session_.append(session)
        datetimex = datetime1
        while datetimex.day < datetime2.day - 1:
            datetimex += datetime.timedelta(days=days_split)
            datetimex = datetimex.replace(hour=20)
            datetimex = datetimex.replace(minute=0)
            ts.append(datetimex)

        for i in range(len(ts)):
            startDateTimex = str(ts[i].year) + '-' + str(ts[i].month).zfill(2) + '-' + str(ts[i].day).zfill(
                2) + ' ' + str(ts[i].hour).zfill(2) + ':' + str(ts[i].minute).ljust(2, '0')
            eventdts.append(startDateTimex)

    elif type == 'assignment':
        ts = []
        days_split = days // 2
        session = expectedTime // 2
        session_.append(session)
        datetimex = datetime1
        while datetimex.day < datetime2.day - 1:
            datetimex += datetime.timedelta(days=days_split)
            datetimex = datetimex.replace(hour=16)
            datetimex = datetimex.replace(minute=0)
            ts.append(datetimex)

        for i in range(len(ts)):
            startDateTimex = str(ts[i].year) + '-' + str(ts[i].month).zfill(2) + '-' + str(ts[i].day).zfill(
                2) + ' ' + str(ts[i].hour).zfill(2) + ':' + str(ts[i].minute).ljust(2, '0')
            eventdts.append(startDateTimex)

    elif type == 'project':
        ts = []
        days_split = days // 3
        session = expectedTime // 3
        session_.append(session)
        datetimex = datetime1
        while datetimex.day < datetime2.day - 1:
            datetimex += datetime.timedelta(days=days_split)
            datetimex = datetimex.replace(hour=16)
            datetimex = datetimex.replace(minute=0)
            ts.append(datetimex)

        for i in range(len(ts)):
            startDateTimex = str(ts[i].year) + '-' + str(ts[i].month).zfill(2) + '-' + str(ts[i].day).zfill(
                2) + ' ' + str(ts[i].hour).zfill(2) + ':' + str(ts[i].minute).ljust(2, '0')
            eventdts.append(startDateTimex)

    count = 1
    suggested_events = []
    for dt in eventdts:
        xname = name + ' Session ' + str(count)
        print(dt)
        _username, _password, _name, _type, _expectedTime, _startDateTime, _repeat, _numTimesMissed = username, password, xname, type, session_[0], dt, repeat, numTimesMissed
        d = {'username': _username, 'password': _password, 'name': _name, 'type': _type, 'expectedTime': _expectedTime,
             'startDateTime': _startDateTime, 'repeat': _repeat, 'numTimesMissed': _numTimesMissed}
        while True:
            if not checkDuplicates(d, username, password):
                #r = requests.post('http://127.0.0.1:5000/event/add', d)
                #print(r.text)
                suggested_events.append(d)
                count += 1
                break
            else:
                print("Duplicate entry")
                date1, time1 = d['startDateTime'].split()
                datetime_ = datetime.datetime(int(date1[:4]), int(date1[5:7]), int(date1[8:]), int(time1[:2]), int(time1[3:5]))
                hour_ = datetime_.hour + 1
                datetime_ = datetime_.replace(hour=hour_)
                startDateTimexNEW = str(datetime_.year) + '-' + str(datetime_.month).zfill(2) + '-' + str(datetime_.day).zfill(
                    2) + ' ' + str(datetime_.hour).zfill(2) + ':' + str(datetime_.minute).ljust(2, '0')
                d['startDateTime'] = startDateTimexNEW

    print(suggested_events)



def checkDuplicates(checkEvent, username, password):
    r = requests.post('http://127.0.0.1:5000/event/get', {'username': 'username', 'password': 'password'})
    #print(r.text)

    for event in r.json():
        date1, time1 = event['startDateTime'].split()
        date2, time2 = checkEvent['startDateTime'].split()
        datetime1 = datetime.datetime(int(date1[:4]), int(date1[5:7]), int(date1[8:]), int(time1[:2]), int(time1[3:5]))
        datetime2 = datetime.datetime(int(date2[:4]), int(date2[5:7]), int(date2[8:]), int(time2[:2]), int(time2[3:5]))

        if datetime1.day == datetime2.day and datetime1.hour == datetime2.hour:
            return True

    return False

suggestEvent()

#r = requests.post('http://127.0.0.1:5000/event/get', {'username': 'username', 'password': 'password'})
#print(r.text)