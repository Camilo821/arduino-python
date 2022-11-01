import serial, time

arduino = serial.Serial("COM12", 9600)

while True:
    val = input("Ingrese una letra")
    if val == "a":
        arduino.write(b'a')
    if val == "b":
        arduino.write(b'b')