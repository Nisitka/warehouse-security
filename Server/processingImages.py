import os
import cv2

def processingImage(image):
    # преобразуем изображение к оттенкам серого
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # инициализировать распознаватель лиц (каскад Хаара по умолчанию)
    nameFile = 'frontalface_default.xml'
    dataDir = os.getcwd() + "/neuralNetwork/data"
    face_cascade = cv2.CascadeClassifier(dataDir + '/haarcascades/' + nameFile)

    # обнаружение всех лиц на изображении
    faces = face_cascade.detectMultiScale(image_gray)

    # для всех обнаруженных лиц рисуем синий квадрат
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)

    return image