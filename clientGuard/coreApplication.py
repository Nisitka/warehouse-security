from GUI import gui

class Core():
    def __init__(self):
        self.guiApp = gui()
        
    def run(self):
        self.guiApp.openMainWin()
        
    def openGate(self):
        print("Ворота открыты")
        
    def openBarrier(self):
        print("Турникет открыт")