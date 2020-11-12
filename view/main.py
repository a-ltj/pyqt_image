# _*_ coding:utf-8 _*_
"""
 主界面逻辑函数
"""
import os
import exifread
import requests



from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QFileDialog

from ui.main_window import Ui_Form



class MainWindow(Ui_Form, QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('用户识别')
        # self.init_ui()
        self.init_slot()

    def init_slot(self):
        self.pushButton.clicked.connect(self.openfile)
        self.lastpushButton.clicked.connect(self.NextImBntClicked)
        self.prepushButton.clicked.connect(self.PreImBntClicked)
    #打开文件
    def openfile(self):
        #图片路径
        self.download_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        if not self.download_path[0].strip():
            pass
        else:
            self.lineEdit.setText(self.download_path)
            #图片集合
            self.ImNameSet = os.listdir(self.download_path)
            self.ImNameSet.sort()
            self.ImPath = self.download_path+'/'+self.ImNameSet[0]
            pix = QPixmap(self.ImPath)
            # 处理图片
            # 规定大小
            scarePixmap = pix.scaled(QSize(271, 261), aspectRatioMode=Qt.KeepAspectRatio)
            self.label_3.setPixmap(scarePixmap)
            #当前图片id
            self.CurImId = 0
            #查看当前图片属性
            self.get_photo_info

    #显示下一张
    def NextImBntClicked(self):
        # download_path = download_path
        # ImNameSet = self.ImNameSet
        # CurImId = self.CurImId
        #图片个数
        self.ImNum = len(self.ImNameSet)
        if self.CurImId<self.ImNum-1:#不可循环看图
            self.ImPath = os.path.join(self.download_path, self.ImNameSet[self.CurImId+1])
            pix = QPixmap(self.ImPath)
            scarePixmap = pix.scaled(QSize(271, 261), aspectRatioMode=Qt.KeepAspectRatio)
            self.label_3.setPixmap(scarePixmap)
            self.CurImId = self.CurImId+1
            self.get_photo_info

    #显示上一张
    def PreImBntClicked(self):
        # ImNameSet = self.ImNameSet
        # CurImId = self.CurImId
        # ImNum = len(ImNameSet)
        if self.CurImId > 0:  # 第一张图片没有前一张
            self.ImPath = os.path.join(self.download_path, self.ImNameSet[self.CurImId - 1])
            pix = QPixmap(self.ImPath)
            scarePixmap = pix.scaled(QSize(271, 261), aspectRatioMode=Qt.KeepAspectRatio)
            self.label_3.setPixmap(scarePixmap)
            self.CurImId = self.CurImId - 1
            # 显示图片属性
            self.get_photo_info

    # 显示图片属性的基本信息
    @property
    def get_photo_info(self):
        f = open(self.ImPath, 'rb')
        tags = exifread.process_file(f)
        # 打印照片信息
        # try:
        print('拍摄时间：', tags['EXIF DateTimeOriginal'])
        print('照片尺寸：', tags['EXIF ExifImageWidth'], tags['EXIF ExifImageLength'])

            # 纬度
        #     lat_ref = tags["GPS GPSLatitudeRef"].printable
        #     lat = tags["GPS GPSLatitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
        #     lat = float(lat[0]) + float(lat[1]) / 60 + float(lat[2]) / float(lat[3]) / 3600
        #     if lat_ref != "N":
        #         lat = lat * (-1)
        #     # 经度
        #     lon_ref = tags["GPS GPSLongitudeRef"].printable
        #     lon = tags["GPS GPSLongitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
        #     lon = float(lon[0]) + float(lon[1]) / 60 + float(lon[2]) / float(lon[3]) / 3600
        #     if lon_ref != "E":
        #         lon = lon * (-1)
        # except KeyError:
        #     return "ERROR:请确保照片包含经纬度等EXIF信息。"
        # else:
        #     print("经纬度：", lat, lon)
        #     return lat, lon
    # 显示图片位置信息
    # def get_photo_location(self):
    #     self.ak = 'nYPs4LQ9a4VhVxj55AD69K6zgsRy9o4z' #替换为自己申请的密钥
    #     self.location = self.get_photo_info()
    #     url = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak={}&output=json' \
    #           '&coordtype=wgs84ll&location={},{}'.format(self.ak, *self.location)
    #     response = requests.get(url).json()
    #     status = response['status']
    #     if status == 0:
    #         address = response['result']['formatted_address']
    #         print('详细地址：', address)
    #     else:
    #         print('baidu_map error')



