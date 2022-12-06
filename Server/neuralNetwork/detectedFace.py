# поиск лиц на изображении

import os
import cv2

dataDir = os.getcwd() + "/data"

nameFile = "test2.jpg"
path = dataDir + "/Images/" + nameFile

# Загрузка изображения
image = cv2.imread(path) # как N-мерный массив numpy.

# преобразуем изображение к оттенкам серого
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# инициализировать распознаватель лиц (каскад Хаара по умолчанию)
nameFile = 'frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(dataDir + '/haarcascades/' + nameFile)

# обнаружение всех лиц на изображении
faces = face_cascade.detectMultiScale(image_gray)
# печатать количество найденных лиц
print(f"{len(faces)} лиц обнаружено на изображении.")

# для всех обнаруженных лиц рисуем синий квадрат
i = 1
for x, y, width, height in faces:
    crop_img = image[y:y + height, x:x + width]
    # сохраним изображение с обнаруженными лицами
    cv2.imwrite("faceDetectedTest" + str(i) + ".jpg", crop_img)
    i += 1