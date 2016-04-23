from time import time
import os.path
import logging

checker = False
close_app = False
poll_interval = 5                  # seconds
init_time = int(time())

device_file_name = "/dev/ttyUSB0"

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
        print(os.path.exists(device_file_name))
        try:
            if os.path.exists(device_file_name):
                print('connected')
                logging.debug('device connected')
            else:
                print("device not connected")

        except FileNotFoundError:
            print("not connected")

