#!/usr/bin/env python3
import json
import pyowm
import serial
import sys
import time
import os.path
import logging
from time import time as tm

"""
This file contain essence from other files in this project,
and needed for display data on the serial interface LCD display
plugged to Arduino
"""

checker = True                      # update display, if first run
close_app = False
poll_interval = 3600                  # polling interval in seconds 3600 - 1 hour
init_time = int(tm())

device_file_name = "/dev/ttyUSB{0}"   # device file name in linux

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='system.log')
# openweathermap API key
# please use you own api key!
API_KEY = '3ede2418f1124401efcd68e5ae3bddcb'
town = 'Norilsk'
area = 'ru'

########################
serial_port = '/dev/ttyUSB'
serial_baudrate = '9600'
serial_parity = 'N'
########################

owm = pyowm.OWM(API_KEY)

observation = owm.weather_at_place('{0},{1}'.format(town, area))
w = observation.get_weather()


def get_weather_wind_direction(mode=True):
    return str(degree(round(json.loads(json.dumps(w.get_wind()), 1)['deg']), mode))


def get_weather_wind_speed():
    return str(round(json.loads(json.dumps(w.get_wind()))['speed']))


def get_weather_temperature():
    return str(round(json.loads(json.dumps(w.get_temperature('celsius')))['temp']))


def get_weather_humidity():
    return int(round(json.loads(json.dumps(w.get_humidity()))))


def weather_wind():
    return "Ветер: " + get_weather_wind_direction() + " " + get_weather_wind_speed() + " м/с"


def weather_temp():
    return "Температура: " + get_weather_temperature()


def weather_humidity():
    return "Влажность: " + str(get_weather_humidity()) + " %"


def send_data():
    ans = bytes("{temp} {wind} {winddir} {hum} \n".format(temp=get_weather_temperature(),
                                                          wind=get_weather_wind_speed(),
                                                          winddir=get_weather_wind_direction(mode=False),
                                                          hum=get_weather_humidity()), encoding="UTF-8")
    try:
        serial_instance = serial.serial_for_url(serial_port,
                                                serial_baudrate,
                                                parity=serial_parity,
                                                xonxoff=0,
                                                rtscts=0,
                                                do_not_open=True)
        serial_instance.dtr = False
        # serial_instance.rts = False
        serial_instance.open()
        time.sleep(5)  #
        serial_instance.write(ans)

    except serial.SerialException as e:
        sys.stderr.write('could not open port {}: {}\n'.format(repr(serial_port), e))


if __name__ == '__main__':
    logging.debug('running application')
    for num_port in range(0, 10):
        print('search device')
        if os.path.exists(device_file_name.format(num_port)):
            serial_port = device_file_name.format(num_port)
            device_file_name = device_file_name.format(num_port)
            print("Found: " + device_file_name.format(num_port))
            break

    while not close_app:
        if int(tm()) > (init_time + poll_interval):
            checker = True
        else:
            if not os.path.exists(device_file_name):
                checker = True

        if checker & os.path.exists(device_file_name):
            time.sleep(5)
            print("{0} seconds pause".format(poll_interval))
            checker = False
            init_time = int(tm())
            try:
                if os.path.exists(device_file_name):
                    print('connected')
                    logging.debug('device connected')
                    send_data()
                else:
                    print("device not connected")

            except FileNotFoundError:
                print("not connected")
