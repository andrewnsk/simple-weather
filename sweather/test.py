import warnings
import serial
import serial.tools.list_ports

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    ]
if not arduino_ports:
    pass    # raise IOError("No Arduino found")
if len(arduino_ports) > 1:
    warnings.warn('Multiple Arduinos found - using the first')

ser = serial.Serial(arduino_ports[1])
print(ser)

for p in serial.tools.list_ports.comports():
    print(p.description, p.serial_number)


