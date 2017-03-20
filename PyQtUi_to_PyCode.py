# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQtUi_to_PyCode.ui'
#
# Created: Sun Mar 19 13:33:26 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import shutil
import os
import subprocess

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def selectFile(self):
        #self.fileDialog = QtGui.QFileDialog(self)
        #self.fileDialog.show()
        a = QtGui.QFileDialog.getOpenFileName()
        self.TextBoxFilePath.setText(a)
    def RunButtonExec(self):
        print ("Convert Button Clicked")
        #subprocess.call(["systeminfo"])
        #os.system("cd")
        """
        print a

        print b"""


        trimmedtext = self.TextBoxPythonPath.text()
        trimmedtext = str(trimmedtext)
        trimmedtext = trimmedtext.strip()
        File_to_convert = self.TextBoxFilePath.text()
        File_to_convert = str(File_to_convert)
        File_to_convert = File_to_convert.strip()

        srcfile = File_to_convert
        print "##############" + srcfile
        dstroot = trimmedtext
        print "##############" + dstroot
        dstdir = os.path.join(dstroot, os.path.dirname(srcfile))

        os.makedirs(dstdir)  # create all directories, raise an error if it already exists
        shutil.copy(srcfile, dstdir)


        """
        os.chdir(trimmedtext)

        string = trimmedtext + "python.exe pyuic.py " + "PyQtUi_to_PyCode.ui -o Output.py -x"
        os.system(string)"""


        """
        File = open("Data.dat", "w")
        File.writelines(self.TextBoxPythonPath.text())
        File.write("\n")
        File.writelines(self.TextBoxFilePath.text())
        File.close()"""

        #GoToDir = self.TextBoxPythonPath.text()
        #GoToDir = str(GoToDir)
        #print "#############" + GoToDir
        #GoToDir = "cd " + str(GoToDir)
        #print "$$$$$" + GoToDir
        #os.system(GoToDir)
        #Command =

        #os.chdir(GoToDir)
        #os.system("cd")

        #os.system("python.exe pyuic.py PyQtUi_to_PyCode.ui -o Output.py -x")

        #CommandLine = "python" + self.TextBoxPythonPath.text() + "pyuic.py " + self.TextBoxFilePath.text() + " -o Output.py -x"
        #print CommandLine
        #CommandLine = str(CommandLine)
        #os.system(CommandLine)



    def DefaultButtonClick(self):
        """print ("Default Button Clicked")
        direct = "C:\\DefaultButtonData"
        if not os.path.exists(direct):
            os.makedirs(direct)
        DefaultButtonData = open(os.path.join(direct, "RecentFileData.dat"), 'r+b')
        line = DefaultButtonData.readlines()
        LastFilePath = ''.join(line)
        self.TextBoxFilePath.setText(LastFilePath)
        print LastFilePath
        #if (line == Null)

        DefaultButtonData.write(self.TextBoxFilePath.text())
        DefaultButtonData.close()"""
        File = open("Data.dat", "r+b")
        lines = File.readlines()
        print lines[0]
        print lines[1]
        self.TextBoxPythonPath.setText(lines[0])
        self.TextBoxFilePath.setText(lines[1])
        #print File.readline()

        #self.TextBoxPythonPath.setText("C:/Portable_Python_2.7.6.1/App")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 300)
        MainWindow.setMaximumSize(QtCore.QSize(700, 300))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        # button event
        self.PushButton = QtGui.QPushButton(self.centralwidget)
        self.PushButton.setGeometry(QtCore.QRect(360, 160, 75, 23))
        self.PushButton.setObjectName(_fromUtf8("PushButton"))
        self.PushButton.clicked.connect(self.RunButtonExec)
        self.PushButtonDefault = QtGui.QPushButton(self.centralwidget)
        self.PushButtonDefault.setGeometry(QtCore.QRect(180, 160, 125, 23))
        self.PushButtonDefault.setObjectName(_fromUtf8("PushButtonDefault"))
        self.PushButtonDefault.clicked.connect(self.DefaultButtonClick)
        self.PushButtonBrowse = QtGui.QPushButton(self.centralwidget)
        self.PushButtonBrowse.setGeometry(QtCore.QRect(180, 120, 125, 23))
        self.PushButtonBrowse.setObjectName(_fromUtf8("PushButtonBrowse"))
        self.PushButtonBrowse.clicked.connect(self.selectFile)
        ######## Text Box Python Path
        self.TextBoxPythonPath = QtGui.QLineEdit(self.centralwidget)
        self.TextBoxPythonPath.setGeometry(QtCore.QRect(171, 30, 471, 20))
        self.TextBoxPythonPath.setObjectName(_fromUtf8("TextBoxPythonPath"))
        self.LabelPythonPath = QtGui.QLabel(self.centralwidget)
        self.LabelPythonPath.setGeometry(QtCore.QRect(37, 30, 129, 18))
        self.LabelPythonPath.setObjectName(_fromUtf8("LabelPythonPath"))
        self.LabelFilePath = QtGui.QLabel(self.centralwidget)
        self.LabelFilePath.setGeometry(QtCore.QRect(20, 61, 221, 16))
        self.LabelFilePath.setObjectName(_fromUtf8("LabelFilePath"))
        self.TextBoxFilePath = QtGui.QLineEdit(self.centralwidget)
        self.TextBoxFilePath.setGeometry(QtCore.QRect(246, 61, 401, 20))
        self.TextBoxFilePath.setObjectName(_fromUtf8("TextBoxFilePath"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.PushButton.setText(_translate("MainWindow", "Convert", None))
        self.PushButtonDefault.setText(_translate("MainWindow", "Restore with Last Data", None))
        self.PushButtonBrowse.setText(_translate("MainWindow", "Browse File", None))
        self.LabelPythonPath.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Python 2.7 Location</span></p></body></html>", None))
        self.LabelFilePath.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">File to Convert from Qt to Python Code</span></p></body></html>", None))
    def FilePathData(self, MainWindow):
        PythonPath = self.TextBoxPythonPath.text()
        FileToConvert = self.TextBoxFilePath.text()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

