import cv2
from pyfirmata import Arduino
import time
arduino = Arduino('COM3')
GREEN = 2
RED = 3
face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml") # Tomar como referencia el haarcascade

cap = cv2.VideoCapture(0) # Capturar la camara

while True:
    _, img = cap.read() # Leer la captura de la web cam
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # pasar a escala de grises
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:                                  # Mostrar un rectangulo
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2 ) # en el lugar en el que se detecte el rostro
        arduino.digital[GREEN].write(1)
    cv2.imshow('img', img) # Mostrar en la web cam
    k = cv2.waitKey(27) # detectar teclas
    if k == 27: # 27 es el ascii para esc
        break
cap.release()