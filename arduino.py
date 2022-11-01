import serial, time
import numpy as np

arduino = serial.Serial("COM10", 9600)




while True:
    val = input("Ingrese una letra")
    if val == "a":
        arduino.write(b'a')
    if val == "b":
        arduino.write(b'b')