import sys  # sys нужен для передачи argv в QApplication

from coreApplication import Core

if __name__ == '__main__':
    # создание и запуск приложения
    cameraClient = Core(sys.argv)
    cameraClient.run()