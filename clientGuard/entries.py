# class Entries(): # сделай наследование 
    

class Barrier():
    def __init__(self):
        self.open = False
        
    def isOpen(self):
        return self.open
    
    def Open(self):
        self.open = True
        
    def Close(self):
        self.open = False
        
class Gate():
    def __init__(self):
        self.open = False
        
    def isOpen(self):
        return self.open
    
    def Open(self):
        self.open = True
        
    def Close(self):
        self.open = False
