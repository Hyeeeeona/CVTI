import numpy as np
import cv2
import shutil
import os, sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from glob import glob

form_class = uic.loadUiType("videoslicer.ui")[0]
classes = ["normal", "collapse"]

def naming(length, name):
    string = ""
    for i in range(0, length-len(name)):
        string = string + "0"

    return string + name 

def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None

def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)
        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
            print(e)
            return False

def sampling(video_dir, save_dir, slicing_type, slicing_cnt, ext, start_num=1):
#    if not os.path.isdir(save_dir):
#        os.mkdir(save_dir)
    
    videolist = { os.path.splitext(os.path.basename(file)) for file in glob(video_dir + "/*.mp4") }

    #video name directory 생성
    #class unique directory 생성
    #images, annotations 파일 생성
    # make directories

    for index, name, ext in enumerate(videolist):
        try:
            tmp = name.split('_')
            if tmp[0] not in classes:
                  print("video file name error")
                continue
            video_class = tmp[0]
            video_name = tmp[1]
        except:
            print("ff")
    
        if not os.path.isdir(save_dir + "/" + 
        
        cntlen = len(str(start_num))
        
        shutil.copyfile(os.path.join(video_dir, video),"vidioslicer.tmp")
        cap = cv2.VideoCapture("vidioslicer.tmp")
        length = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        frame = -1
        cwd = os.getcwd()
        
        if slicing_type == "fps":
            aaa = int(slicing_cnt)
        else:
            aaa = length / int(slicing_cnt)
    
        fileCount = int(start_num)
        
        objWd = save_dir
        while(cap.isOpened()):
            ret, im = cap.read()
            frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            if not ret:
                break
            if not frame%aaa < 1:
                continue
            
            if not objWd == os.getcwd():
                os.chdir(objWd)
            
            
            if ext == "jpg":
                cv2.imwrite("temp."+ext, im)
                os.rename("temp."+ext, os.path.join(videoname  +"_"+naming(cntlen, str(frame))+"."+ext))
            else:           
                cv2.imwrite("temp."+ext, im,  [cv2.IMWRITE_PNG_COMPRESSION, 1])
                os.rename("temp."+ext, os.path.join(videoname +"_"+naming(cntlen, str(frame))+"."+ext))
                
            fileCount += 1
        cap.release()
        
        os.chdir(cwd)
        os.remove("vidioslicer.tmp")
        
        print("{} ".format(videoname + "_"+str(naming(6, str(index)))+" 완료"))

        break #임시로 디렉터리 안의 하나의 비디오만 처리 후 종료
        
        
    print("end")


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.set_only_int()


    def set_only_int(self):
        self.onlyInt = QIntValidator()
        self.tb_start_num.setValidator(self.onlyInt)
        self.tb_num.setValidator(self.onlyInt)
    
    def initUI(self):
        self.btn_open_video_dir.clicked.connect(self.open_video_dir)
        self.btn_open_save_dir.clicked.connect(self.open_save_dir)
        self.btn_do_convert.clicked.connect(self.do_convert)

    
    def open_video_dir(self):
        global video_dir

        video_dir_tmp = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if video_dir_tmp != None or video_dir_tmp != "":
            video_dir = video_dir_tmp
        self.tb_video_dir.clear()
        self.tb_video_dir.append(video_dir)


    def open_save_dir(self):
        global save_dir
        save_dir_tmp = QFileDialog.getExistingDirectory(self, 'Select Folder')
        #ave_dir_tmp =  QFileDialog(self, windowTitle='Select directory')
        #save_dir_tmp.setDirectory(self.lineEdit.text() or __file__)
        #save_dir_tmp.setFileMode(save_dir_tmp.Directory)
        #save_dir_tmp.setOptions(save_dir_tmp.DontUseNativeDialog)

        if save_dir_tmp != None or save_dir_tmp != "":
            save_dir = save_dir_tmp
        self.tb_save_dir.append(save_dir)
    
    def do_convert(self):
        ext = "jpg" if self.rb_jpg.isChecked() else "png"
    
        slicing_type = "fps" if self.btn_fps.isChecked() else "img_cnt"
        slicing_num = self.tb_num.text()
        start_num = self.tb_start_num.text()
        self.btn_do_convert.setText("변환 중...")
        sampling(video_dir, save_dir, slicing_type, slicing_num, ext, start_num)
        self.btn_do_convert.setText("변환")

    #def checked_file_name(self):
    #def checked_start_number(self):



if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()

