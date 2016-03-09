import sqlite3
from datetime import datetime
import os.path
import pyowm
import json
import azimuth

# openweathermap API key
# please use you own api key!
owm = pyowm.OWM('3ede2418f1124401efcd68e5ae3bddcb')
# Town
town = "Norilsk"
observation = owm.weather_at_place('{0},ru'.format(town))
w = observation.get_weather()


def local_time():
    # Текущее время и дата
    time = datetime.now().replace(microsecond=0)
    return time

#############################################################################
#           Test data

db_file_name = "weather.db"

date_time = local_time()
temperature = str(round(json.loads(json.dumps(w.get_temperature('celsius')))['temp']))
humidity = int(round(json.loads(json.dumps(w.get_humidity()))))
wind = "{0} м/с".format(str(round(json.loads(json.dumps(w.get_wind()))['speed'])))
wind_direction = str(azimuth.degree(round(json.loads(json.dumps(w.get_wind()), 1)['deg'])))
#############################################################################


def create_db(db_file_name_local):
    # База с погодными данными
    db_connection = sqlite3.connect(db_file_name_local)
    db_conn_cursor = db_connection.cursor()
    db_conn_cursor.execute('''CREATE TABLE weather
        (id INTEGER PRIMARY KEY, town TEXT, dtime TEXT, t_value TEXT, h_value INTEGER, w_value TEXT, w_dir TEXT)''')
    db_connection.commit()
    db_connection.close()
    print("File created")


def open_and_write_db(db_file_name_local):
    # База с погодными данными
    db_connection = sqlite3.connect(db_file_name_local)
    db_conn_cursor = db_connection.cursor()
    db_conn_cursor.execute('''INSERT INTO weather(town, dtime, t_value, h_value, w_value, w_dir)
                  VALUES(?,?,?,?,?,?)''', (town, date_time, temperature, humidity, wind, wind_direction))
    # Save (commit) the changes
    db_connection.commit()
    for row in db_conn_cursor.execute('SELECT * FROM weather ORDER BY id'):
            print(row)

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    db_connection.close()

if not (os.path.isfile(db_file_name)):
    create_db(db_file_name)

open_and_write_db(db_file_name)
