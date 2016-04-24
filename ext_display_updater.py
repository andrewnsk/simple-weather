from time import time
import os.path
import logging
from rs232 import send_data

checker = True                      # update display, if first run
close_app = False
poll_interval = 15                  # polling interval in seconds 3600 - 1 hour
init_time = int(time())

device_file_name = "/dev/ttyUSB0"   # device file name in linux

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='system.log')

while not close_app:
    if int(time()) > (init_time + poll_interval):
        checker = True

    if checker:
        print("{0} seconds pause".format(poll_interval))
        checker = False
        init_time = int(time())
        try:
            if os.path.exists(device_file_name):
                print('connected')
                logging.debug('device connected')
                send_data()
            else:
                print("device not connected")

        except FileNotFoundError:
            print("not connected")

