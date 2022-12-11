import numpy as np
import cv2

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    # cap = cv2.VideoCapture('http://192.168.3.9:8080/')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        #print(type(frame))
        cv2.imshow("image", frame)
        '''
        frames = frames + 1
        print(frames)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quit")
            break
        '''

    cap.release()