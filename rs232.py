from collect_weather import get_weather_temperature
import serial
import sys
import time


########################
serial_port = '/dev/ttyUSB0'
serial_baudrate = '9600'
serial_parity = 'N'
########################

ans = bytes("{0}\n".format(get_weather_temperature()), encoding="UTF-8")

try:
    serial_instance = serial.serial_for_url(serial_port, serial_baudrate, parity=serial_parity, do_not_open=True)
    serial_instance.dtr = 0  # a little hack for Arduino. It doesn't reset
    serial_instance.open()
    time.sleep(5)  #
    serial_instance.write(ans)
    time.sleep(5)  #

except serial.SerialException as e:
    sys.stderr.write('could not open port {}: {}\n'.format(repr(serial_port), e))

else:
    sys.exit(0)
