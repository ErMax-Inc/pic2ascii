from PyQt6 import QtGui, QtWidgets, QtCore
import os
#import matplotlib.font_manager as font_manager
from matplotlib import font_manager
from fontTools import ttLib

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontComboBox.setGeometry(QtCore.QRect(210, 220, 338, 32))
        self.fontComboBox.setObjectName("fontComboBox")
        self.text = QtWidgets.QLineEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(300, 310, 398, 48))
        self.text.setObjectName("yourmom")
        self.text.setText("uuouo")
        self.text.setFont(QtGui.QFont(font_manager.findfont(ui.fontComboBox.currentFont().family())))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    
    
        self.fontComboBox.currentFontChanged.connect(lambda:your())
def your():
    if ui.fontComboBox.currentFont().family().find("-") == -1:
        print(ui.fontComboBox.currentFont().family())
        w = font_manager.findfont(ui.fontComboBox.currentFont().family())
        print(w)
        font = ttLib.TTFont(w)
        print(font["name"].getDebugName(4))
        print(font["name"].getDebugName(1))
        x = QtGui.QFont(font["name"].getDebugName(1))
        ui.fontComboBox.setFont(x)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    your()
    sys.exit(app.exec())
