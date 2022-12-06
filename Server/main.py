import sys  # sys нужен для передачи argv в QApplication

from Server.coreApplication import Core

if __name__ == '__main__':
    # строчка для олдов
    print("Hello, hackathon")

    warenouseSecurity = Core(sys.argv)
    warenouseSecurity.run()