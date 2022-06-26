from asyncio.windows_events import NULL
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("videoslicer.ui")[0]

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.set_only_int()


    def set_only_int(self):
        self.onlyInt = QIntValidator()
        self.lineEdit_4.setValidator(self.onlyInt)
        self.lineEdit.setValidator(self.onlyInt)
    
    def initUI(self):
        self.pushButton.clicked.connect(self.video_folder_open)
        self.pushButton_2.clicked.connect(self.save_folder_open)
        self.pushButton_3.clicked.connect(self.do_convert)

    
    def video_folder_open(self):
        global video_folder
        video_folder_tmp = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if video_folder_tmp != NULL or video_folder_tmp != "":
            video_folder = video_folder_tmp
        self.textBrowser_2.clear()
        self.textBrowser_2.append(video_folder)


    def save_folder_open(self):
        global save_folder
        save_folder_tmp = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if save_folder_tmp != NULL or save_folder_tmp != "":
            save_folder = save_folder_tmp
        self.textBrowser.append(save_folder)
    
    def do_convert(self):
        self.pushButton_3.setText("변환 중...")

    #def checked_file_name(self):
    #def checked_start_number(self):



if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()