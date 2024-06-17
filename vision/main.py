# Importamos las librerías
import cv2
import numpy as np
import face_recognition as fr
import os
import random
from datetime import datetime

# Accedemos a la carpeta
path = 'Personal'
images = []
clases = []
lista = os.listdir(path)

# Variables
comp1 = 100

# Leemos los rostros de la base de datos
for lis in lista:
    imgdb = cv2.imread(f'{path}/{lis}')
    images.append(imgdb)
    clases.append(os.path.splitext(lis)[0])

print(clases)

# Función para codificar los rostros
def codrostros(images):
    listacod = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cod = fr.face_encodings(img)[0]
        listacod.append(cod)

    return listacod

# Hora de ingreso
def horario(nombre):
    with open('Horario.txt', 'a') as h:  # Cambié 'r+' a 'a' para simplificar la escritura
        info = datetime.now()
        fecha = info.strftime('%Y:%m:%d')
        hora = info.strftime('%H:%M:%S')
        h.writelines(f'{nombre},{fecha},{hora}\n')
        print(info)

# Llamamos a la función para codificar los rostros
rostroscod = codrostros(images)

# Realizamos VidepCaptura (0 para la cámara de la laptop)
cap = cv2.VideoCapture(0)

# Empezamos
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al acceder a la cámara.")
        break

    # Reducimos las imágenes para mejor procesamiento
    frame2 = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    rgb = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

    # Buscamos los rostros
    faces = fr.face_locations(rgb)
    facescod = fr.face_encodings(rgb, faces)

    for facecod, faceloc in zip(facescod, faces):
        comparacion = fr.compare_faces(rostroscod, facecod)
        simi = fr.face_distance(rostroscod, facecod)
        min_index = np.argmin(simi)

        if comparacion[min_index]:
            nombre = clases[min_index].upper()
            print(nombre)
            yi, xf, yf, xi = faceloc
            yi, xf, yf, xi = yi*4, xf*4, yf*4, xi*4

            if comp1 != min_index:
                r = random.randrange(0, 255, 50)
                g = random.randrange(0, 255, 50)
                b = random.randrange(0, 255, 50)
                comp1 = min_index

            if comp1 == min_index:
                cv2.rectangle(frame, (xi, yi), (xf, yf), (r, g, b), 3)
                cv2.rectangle(frame, (xi, yf-35), (xf, yf), (r, g, b), cv2.FILLED)
                cv2.putText(frame, nombre, (xi+6, yf-6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                horario(nombre)

    # Mostramos los frames
    cv2.imshow("Reconocimiento Facial", frame)

    # Leemos el teclado
    t = cv2.waitKey(5)
    if t == 27:  # Esc key para salir
        break

cap.release()
cv2.destroyAllWindows()
