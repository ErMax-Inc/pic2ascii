# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2 and modified by ErMax.Inc
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys, PIL
from PyQt5 import QtCore, QtGui, QtWidgets
from platform import system 
from PIL import ImageDraw, ImageFont
from tqdm import tqdm
import math
from tkinter.filedialog import askopenfilenames
from tkinter import *
from time import sleep
from multiprocessing import Process
from subprocess import call

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        print(self)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(985, 462)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(985, 462))
        MainWindow.setMaximumSize(QtCore.QSize(985, 462))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks)
        self.widgetMain = QtWidgets.QWidget(MainWindow)
        self.widgetMain.setObjectName("widgetMain")
        self.tabWidget = QtWidgets.QTabWidget(self.widgetMain)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 987, 423))
        self.tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.setStatusTip("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabHome = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabHome.setFont(font)
        self.tabHome.setAutoFillBackground(True)
        self.tabHome.setObjectName("tabHome")
        self.label = QtWidgets.QLabel(self.tabHome)
        self.label.setGeometry(QtCore.QRect(0, 0, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tabHome)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tabHome)
        self.label_3.setGeometry(QtCore.QRect(140, 80, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tabHome, "")
        self.tabSetup = QtWidgets.QWidget()
        self.tabSetup.setAutoFillBackground(False)
        self.tabSetup.setObjectName("tabSetup")
        self.labelinDesk = QtWidgets.QLabel(self.tabSetup)
        self.labelinDesk.setGeometry(QtCore.QRect(10, 40, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.labelinDesk.setFont(font)
        self.labelinDesk.setObjectName("labelinDesk")
        self.lineEditInDir = QtWidgets.QLineEdit(self.tabSetup)
        self.lineEditInDir.setEnabled(True)
        self.lineEditInDir.setGeometry(QtCore.QRect(260, 40, 511, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lineEditInDir.setFont(font)
        self.lineEditInDir.setMouseTracking(False)
        self.lineEditInDir.setFrame(True)
        self.lineEditInDir.setReadOnly(True)
        self.lineEditInDir.setClearButtonEnabled(False)
        self.lineEditInDir.setObjectName("lineEditInDir")
        self.pushButtonImageIn = QtWidgets.QPushButton(self.tabSetup)
        self.pushButtonImageIn.setGeometry(QtCore.QRect(790, 40, 171, 23))
        self.pushButtonImageIn.setObjectName("pushButtonImageIn")
        self.labelOutDesk = QtWidgets.QLabel(self.tabSetup)
        self.labelOutDesk.setGeometry(QtCore.QRect(10, 80, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.labelOutDesk.setFont(font)
        self.labelOutDesk.setObjectName("labelOutDesk")
        self.lineEditOutDir = QtWidgets.QLineEdit(self.tabSetup)
        self.lineEditOutDir.setGeometry(QtCore.QRect(260, 80, 511, 20))
        self.lineEditOutDir.setReadOnly(True)
        self.lineEditOutDir.setObjectName("lineEditOutDir")
        self.pushButtonFolderOut = QtWidgets.QPushButton(self.tabSetup)
        self.pushButtonFolderOut.setGeometry(QtCore.QRect(790, 80, 171, 23))
        self.pushButtonFolderOut.setObjectName("pushButtonFolderOut")
        self.labelFormatOut = QtWidgets.QLabel(self.tabSetup)
        self.labelFormatOut.setGeometry(QtCore.QRect(60, 260, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.labelFormatOut.setFont(font)
        self.labelFormatOut.setObjectName("labelFormatOut")
        self.comboBoxFormatOut = QtWidgets.QComboBox(self.tabSetup)
        self.comboBoxFormatOut.setGeometry(QtCore.QRect(280, 260, 91, 22))
        self.comboBoxFormatOut.setObjectName("comboBoxFormatOut")
        self.comboBoxFormatOut.addItem("")
        self.comboBoxFormatOut.addItem("")
        self.tabWidget.addTab(self.tabSetup, "")
        self.tabJobs = QtWidgets.QWidget()
        self.tabJobs.setStatusTip("")
        self.tabJobs.setObjectName("tabJobs")
        self.progressBar = QtWidgets.QProgressBar(self.tabJobs)
        self.progressBar.setGeometry(QtCore.QRect(5, 370, 971, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.progressBar.setFont(font)
        self.progressBar.setToolTipDuration(0)
        self.progressBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(True)
        self.progressBar.setObjectName("progressBar")
        self.pushButtonStart = QtWidgets.QPushButton(self.tabJobs)
        self.pushButtonStart.setGeometry(QtCore.QRect(860, 330, 81, 31))
        self.pushButtonStart.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButtonStart.setMouseTracking(False)
        self.pushButtonStart.setToolTipDuration(0)
        self.pushButtonStart.setCheckable(False)
        self.pushButtonStart.setObjectName("pushButtonStart")
        #click
        self.pushButtonStart.clicked.connect(lambda:ui.jobstart(MainWindow))
        
        self.pushButtonStop = QtWidgets.QPushButton(self.tabJobs)
        self.pushButtonStop.setGeometry(QtCore.QRect(770, 330, 81, 31))
        self.pushButtonStop.setMouseTracking(False)
        self.pushButtonStop.setToolTipDuration(0)
        self.pushButtonStop.setWhatsThis("")
        self.pushButtonStop.setAccessibleDescription("")
        self.pushButtonStop.setObjectName("pushButtonStop")
        #click
        self.pushButtonStop.clicked.connect(lambda:ui.Stop(MainWindow))
        
        self.comboBoxFinnishOpts = QtWidgets.QComboBox(self.tabJobs)
        self.comboBoxFinnishOpts.setGeometry(QtCore.QRect(770, 300, 171, 21))
        self.comboBoxFinnishOpts.setToolTipDuration(0)
        self.comboBoxFinnishOpts.setEditable(False)
        self.comboBoxFinnishOpts.setPlaceholderText("")
        self.comboBoxFinnishOpts.setDuplicatesEnabled(False)
        self.comboBoxFinnishOpts.setObjectName("comboBoxFinnishOpts")
        self.comboBoxFinnishOpts.addItem("")
        self.comboBoxFinnishOpts.addItem("")
        self.comboBoxFinnishOpts.addItem("")
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.addTab(self.tabJobs, "")
        MainWindow.setCentralWidget(self.widgetMain)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_Pic2Ascii = QtWidgets.QAction(MainWindow)
        self.actionAbout_Pic2Ascii.setObjectName("actionAbout_Pic2Ascii")
        self.actionContact = QtWidgets.QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionContact)
        self.menuAbout.addAction(self.actionAbout_Pic2Ascii)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.jobstart(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ErMax.Inc-Pic2Ascii"))
        self.label.setText(_translate("MainWindow", "Welcome!"))
        self.label_2.setText(_translate("MainWindow", "Chose a Tab to begin,"))
        self.label_3.setText(_translate("MainWindow", "or select Help! for help."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHome), _translate("MainWindow", "Home"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabHome), _translate("MainWindow", "This is the Home Tab"))
        self.labelinDesk.setText(_translate("MainWindow", "Input Image/Image Sequance:"))
        self.pushButtonImageIn.setText(_translate("MainWindow", "Browse (Image/Image Sequance)"))
        self.labelOutDesk.setText(_translate("MainWindow", "Output Folder Image/Image Sequance:"))
        self.pushButtonFolderOut.setText(_translate("MainWindow", "Browse (Folder)"))
        self.labelFormatOut.setText(_translate("MainWindow", "Output Image Formats (Supported):"))
        self.comboBoxFormatOut.setItemText(0, _translate("MainWindow", "PNG (Default)"))
        self.comboBoxFormatOut.setItemText(1, _translate("MainWindow", "JPG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSetup), _translate("MainWindow", "Setup"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabSetup), _translate("MainWindow", "This is where you setup the source and ouput"))
        self.progressBar.setToolTip(_translate("MainWindow", "Status bar"))
        self.progressBar.setStatusTip(_translate("MainWindow", "Status bar"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.pushButtonStart.setToolTip(_translate("MainWindow", "This Starts the operation (Job)"))
        self.pushButtonStart.setStatusTip(_translate("MainWindow", "This Starts the operation (Job)"))
        self.pushButtonStart.setText(_translate("MainWindow", "Start Job"))
        self.pushButtonStop.setToolTip(_translate("MainWindow", "This Stops the operaton (Job)"))
        self.pushButtonStop.setStatusTip(_translate("MainWindow", "This Stops the operaton (Job)"))
        self.pushButtonStop.setText(_translate("MainWindow", "Stop Job"))
        self.comboBoxFinnishOpts.setToolTip(_translate("MainWindow", "Choose what to do when done"))
        self.comboBoxFinnishOpts.setStatusTip(_translate("MainWindow", "Choose what to do when done"))
        self.comboBoxFinnishOpts.setItemText(0, _translate("MainWindow", "Do nothing when done"))
        self.comboBoxFinnishOpts.setItemText(1, _translate("MainWindow", "Shutdown when done (Windows only)"))
        self.comboBoxFinnishOpts.setItemText(2, _translate("MainWindow", "Exit Pic2Ascii when done"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabJobs), _translate("MainWindow", "Jobs"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabJobs), _translate("MainWindow", "This is where you start the prosses"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help!"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "This exits the program"))
        self.actionAbout_Pic2Ascii.setText(_translate("MainWindow", "About Pic2Ascii/Licence"))
        self.actionContact.setText(_translate("MainWindow", "Contact"))
    
    def jobstart(self, MainWindow):
        global stopJob
        stopJob = False
        self.pushButtonStart.setEnabled(False)
        self.pushButtonStop.setEnabled(False)
        print('Compiling Variables...\nPlease Wait.')
        self.comboBoxFormatOutFunc(MainWindow)
    
    def comboBoxFormatOutFunc(self, MainWindow):
        global outPutFormat
        if self.comboBoxFormatOut.currentText() == 'PNG (Default)':
            outPutFormat = '.png'
        elif self.comboBoxFormatOut.currentText() == 'JPG':
            outPutFormat = '.jpg'
        self.comboBoxFinnishOptsFunc(MainWindow)
    
    def comboBoxFinnishOptsFunc(self, MainWindow):
        global exitWhenDone
        global shutWhenDone
        if self.comboBoxFinnishOpts.currentText() == 'Exit Pic2Ascii when done':
            if ['linux'] in str(system()):
                exitWhenDone = True
                shutWhenDone = False
            else:
                shutWhenDone = False
                exitWhenDone = False
        elif self.comboBoxFinnishOpts.currentText() == 'Shutdown when done (Windows only)':
            shutWhenDone = True
            exitWhenDone = False
        else:
            shutWhenDone = False
            exitWhenDone = False
        self.pushButtonStop.setEnabled(True)
        print('done\n\n')
        the().main()

    def Stop(self, MainWindow):
        global stopJob
        stopJob = True
        print('stopping...')
        self.pushButtonStart.setEnabled(True)

class the:
    chars = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''[::-1]
    charArray = list(chars)
    charLength = len(charArray)
    interval = charLength/256

    oneCharWidth = 10
    oneCharHeight = 18


    def getChar(self, inputInt):
        return charArray[math.floor(inputInt*interval)]

    def main(self):
        scaleFactor = input('Hello Enter Scale Factor')
        try:
            int(scaleFactor)
        except:
            print('making default')
            sleep(.2)
            scaleFactor = 0.4
        print('select image or image sequance.')
        sleep(.3)
        print('opening window')
        sleep(.2)
        
        #grabs fileman from com()
        fileman = Tk()
        fileman.wm_state('iconic')
        file_path_list = askopenfilenames(filetypes=(("JPEG/JPG files","*.jpeg *.jpg"), ("Any file", "*")), initialdir="/", title='Select pictures.')
        file_path_list = list(file_path_list)
        
        x = 0
        for file in file_path_list:
                
            im = PIL.Image.open(file_path_list[x])
                

            fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

            width, height = im.size
            im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), PIL.Image.NEAREST)
            width, height = im.size
            pix = im.load()

            outputImage = PIL.Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (64, 64, 64))
            #outputImage = im
            d = ImageDraw.Draw(outputImage)

            for i in tqdm(range(height)):
                for j in range(width):
                    r, g, b = pix[j, i]
                    h = int(r/3 + g/3 + b/3)
                    pix[j, i] = (h, h, h)
                    d.text((j*oneCharWidth, i*oneCharHeight), self.getChar(h), font = fnt, fill = (r, g, b))
                    
                
            r = file_path_list[x].replace('/', '\\')
            x += 1
            outputImage.save(r.replace('.jpg', outPutFormat))
            if stopJob == True:
                print('stopped Job')
                break
        if shutWhenDone == True:
            call(shutdown.exe)
        elif exitWhenDone == True:
            print('exiting...')
            sleep(.5)
            exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
