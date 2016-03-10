import sqlite3
from datetime import datetime
import os.path
import pyowm
import json
import azimuth
from collect_weather import get_weather_humidity
from collect_weather import get_weather_temperature
from collect_weather import get_weather_wind_direction
from collect_weather import get_weather_wind_speed
from collect_weather import GetWeather


# openweathermap API key
# please use you own api key!
owm = pyowm.OWM('3ede2418f1124401efcd68e5ae3bddcb')
# Town
town = "Norilsk"

norilsk = GetWeather(town, '3ede2418f1124401efcd68e5ae3bddcb')
print(norilsk.wind_direction())
#print(GetWeather(town, '3ede2418f1124401efcd68e5ae3bddcb').wind_direction())


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
temperature = get_weather_temperature()
humidity = get_weather_humidity()
wind = "{0} м/с".format(get_weather_wind_speed())
wind_direction = get_weather_wind_direction()
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
