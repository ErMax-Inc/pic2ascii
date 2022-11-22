from PyQt6.QtCore import QStandardPaths
from PyQt6 import QtCore
from PyQt6.QtGui import QFontDatabase
from PyQt6.QtWidgets import QApplication
import sys, os

def getFontPaths():
    font_paths = QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.StandardLocation.FontsLocation)

    accounted = []
    unloadable = []
    family_to_path = {}

    db = QFontDatabase()
    for fpath in font_paths:  # go through all font paths
        for filename in os.listdir(fpath):  # go through all files at each path
            path = os.path.join(fpath, filename)

            idx = db.addApplicationFont(path)  # add font path
            
            if idx < 0: unloadable.append(path)  # font wasn't loaded if idx is -1
            else:
                names = db.applicationFontFamilies(idx)  # load back font family name

                for n in names:
                    if n in family_to_path:
                        accounted.append((n, path))
                    else:
                        family_to_path[n] = path
                # this isn't a 1:1 mapping, for example
                # 'C:/Windows/Fonts/HTOWERT.TTF' (regular) and
                # 'C:/Windows/Fonts/HTOWERTI.TTF' (italic) are different
                # but applicationFontFamilies will return 'High Tower Text' for both
    return unloadable, family_to_path, accounted
#input(QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.StandardLocation.FontsLocation))
input(QtCore.QStandardPaths.locate(QtCore.QStandardPaths.StandardLocation.FontsLocation, 'Comic Sans MS'))

https://stackoverflow.com/questions/19098440/how-to-get-the-font-file-path-with-qfont-in-qt#:~:text=What%20you%20can%20do%20is%20first%20get%20the,you%20then%20feed%20to%20the%20database%27s%20applicationFontFamilies%20function.
