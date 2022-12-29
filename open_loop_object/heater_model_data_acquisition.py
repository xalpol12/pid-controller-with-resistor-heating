import serial #pip install pyserial
import numpy as np
from time import sleep
import time
import json
import matplotlib.pyplot as plt
import keyboard #pip install keyboard

plt.ion()
hSerial = serial.Serial('COM11', 115200, timeout=1, parity=serial.PARITY_NONE) 
hSerial.write(b'print_on;')
sleep(0.5)
set_point = 26;
hSerial.write(b'set_point=26;')
sleep(0.5)
hSerial.write(b'freq=1;')
sleep(0.5)
hSerial.write(b'select_controller=1;')
sleep(0.5)

timestr = time.strftime("%Y%m%d-%H%M%S")
hFile = open("data_open_loop_object%s.txt" % (timestr), "a")

hSerial.reset_input_buffer()
hSerial.flush()
temperature_samples = [];
t = [];
t_value=0;
while True:
    text = hSerial.readline()
    temperature = 0
    sample = 0
    try:
        sample = json.loads(text)
        temperature = sample["temperature"]
    except ValueError:
        print("Bad JSON")
        print("%s\r\n" % {text})
        hSerial.flush()
        hSerial.reset_input_buffer()
    print(temperature)
    hFile.write("%.2f," % temperature)
    temperature_samples.append(temperature);
    t.append(t_value);
    t_value = t_value + 1
    # Plot results
    plt.clf()
    plt.plot(t,temperature_samples, '.', markersize=5);
    plt.title("BMP280 logger, STM32 (controller sp=%d C). (author: D. Łuczak)" % set_point)
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (C)")
    plt.show()
    plt.pause(0.0001)
    if keyboard.is_pressed("q"):
        break  # finishing the loop
hSerial.close()
hFile.close()
