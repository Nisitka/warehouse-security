import sys  # sys нужен для передачи argv в QApplication

from coreApplication import Core

if __name__ == '__main__':
    # строчка для олдов
    print("Hello, hackathon")

    serverNeronNet = Core(sys.argv)
    serverNeronNet.run()