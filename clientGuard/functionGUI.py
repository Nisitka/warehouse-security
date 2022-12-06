from PyQt5 import QtGui, QtWidgets

def setStyleButton(QButton, rgb, text):
    QButton.setText(str(text))
    
    if (sum(rgb) < 255*0.9):
        v = 255
    else:
        v = 0
    QButton.setStyleSheet('''
                          QPushButton {
                              background-color: rgb(''' + str(rgb[0]) + ''','''
                                                        + str(rgb[1]) + ''',''' 
                                                        + str(rgb[2]) + '''); 
                             color: rgb(''' + str(v) + ''','''
                                            + str(v) + ''',''' 
                                            + str(v) + ''');
                                                
                              border-style: outset;
                              border-radius: 5px;
                              border-width: 1px;
                              border-color: rgb(0,0,0);
                              }
                          QPushButton:hover {
                              background-color: rgb(''' + str(n(rgb[0]+20)) + ''','''
                                                        + str(n(rgb[1]+20)) + ''',''' 
                                                        + str(n(rgb[2]+20)) + ''');
                              color: rgb(''' + str(v) + ''','''
                                             + str(v) + ''',''' 
                                             + str(v) + ''');
                              border-color: rgb(0,0,0);
                              }
                          ''')
    

def n(value):
    if (value > 255):
        return 255
    else:
        return value