import numpy as np
import time
import json
import threading
import csv

import keyboard
import matplotlib.pyplot as plt
import serial.tools.list_ports


def terminalInput(terminal: serial.Serial):
    while True:
        temperature = input()
        terminal.write(str(temperature).encode())


def dataPlot(temperature, control, desired, time):
    temperature = np.array(temperature)
    control = np.array(control)
    desired = np.array(desired)
    time = np.array(time)
    plt.clf()
    plt.subplot(311)
    plt.title("Temperature: ")
    plt.grid()
    plt.plot(time, temperature)
    plt.plot(time, desired)
    plt.xlabel("Time [s]")
    plt.ylabel("Temperature [c]")
    plt.subplot(312)
    plt.title("PWM DUTY:")
    plt.grid()
    plt.plot(time, control)
    plt.xlabel("Time [s]")
    plt.ylabel("DUTY [%]")
    plt.subplot(313)
    plt.title("Error: ")
    plt.grid()
    plt.plot(time, np.subtract(desired, temperature))
    plt.xlabel("Time [s]")
    plt.ylabel("Error [c]")
    plt.show()
    plt.pause(0.001)


#check which port is in use:
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

hSerial = serial.Serial('COM4', 115200, timeout=1, parity=serial.PARITY_NONE)


thread = threading.Thread(target=terminalInput, args=(hSerial, ))
thread.start()


time_str = time.strftime("%Y%m%d-%H%M%S")
hFile = open("PIDLogging%s.csv" % time_str, "a", newline='')

writer = csv.DictWriter(hFile, fieldnames=["temperature", "desired", "control"])
writer.writeheader()


hSerial.reset_input_buffer()
hSerial.flush()
temperature_samples = []
control_samples = []
desired_samples = []
t = []
t_value=time.time()


firstRound = True
plt.ion()
while True:
    text = hSerial.readline()
    temperature = 0
    control = 0
    desired = 0
    sample = 0
    try:
        sample = json.loads(text)
        temperature = sample["temperature"]
        control = sample["control"]
        desired = sample["desired"]
    except ValueError:
        print("Bad JSON")
        print("%s\r\n" % {text})
        hSerial.flush()
        hSerial.reset_input_buffer()
    hFile.write("%.2f," % temperature)
    temperature_samples.append(temperature);
    control_samples.append(control)
    desired_samples.append(desired)
    if firstRound == True:
        t.append(0)
        firstRound = False
    else:
        t_value = time.time() - t_value
        t.append(round(t_value, 1))
    # Plot results
    dataPlot(temperature_samples, control_samples, desired_samples, t)
    writer.writerow([temperature, desired, control])
    if keyboard.is_pressed("q"):
        break  # finishing the loop
hSerial.close()
hFile.close()
