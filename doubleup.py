from io import BytesIO
import doubleagent
import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import time
import requests
import re
import random
import math
import os
from PIL import Image, ImageOps, ImageFile, ImageDraw, ImageFont
import numpy as np
import cv2 as cv
from rembg.bg import remove

import io
import tkinter
from tkinter import filedialog
import webbrowser
from callee import *
import traceback


class MainWindow(QMainWindow):
    def __init__(self):

        self.thread = {}
        super(MainWindow, self).__init__()
        self.centralwidget = QWidget(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        # 센터 위젯 가장 상위 위젯으로 셀프를 넣는다
        self.centralwidgetLayout = QVBoxLayout(self.centralwidget)
        #  centralwidgetLayout 을 센터 위젯에 편입신다 이것은 v박스 형태로 레이아웃을 설정한다
        self.scrollArea = QScrollArea(self.centralwidget)
        #  스크롤 가능 에어리어를 설정한다
        self.modi = False
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        # self.scrollAreaWidget.setGeometry(QRect(100, 100, 500, 500))
        self.scrollAreaWidgetLayout = QVBoxLayout(
            self.scrollAreaWidget)
        self.scrollAreaWidgetLayout.addItem(QSpacerItem(
            20, 40, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding))
        # 알파이자 오메가
        self.scrollArea.setWidget(self.scrollAreaWidget)
        #  키포인트는 어덯게 레이아웃이 위젯을 통과 시키는지 확인하는 것이다
        self.buttonWidget = QWidget(self.centralwidget)
        self.buttonAddGroupBox = QPushButton(
            'Add', self.buttonWidget)
        self.buttonDeleteLaterGroupBox = QPushButton(
            'Del', self.buttonWidget)
## # # # # # # # # # # # # # # # # # # # # # # # # # # #
        self.buttonWidget2 = QWidget()
        self.buttonAddGroupBox2 = QPushButton(
            'Add', self.buttonWidget2)
        self.buttonDeleteLaterGroupBox2 = QPushButton(
            'Del', self.buttonWidget2)
        self.buttonLayout2 = QGridLayout(self.buttonWidget2)
        self.buttonLayout2.addWidget(
            self.buttonAddGroupBox2,          0, 0, 1, 1)
        self.buttonLayout2.addWidget(
            self.buttonDeleteLaterGroupBox2,  0, 1, 1, 1)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        self.buttonLayout = QGridLayout(self.buttonWidget)
        self.buttonLayout.addWidget(
            self.buttonAddGroupBox,          0, 0, 1, 1)
        self.buttonLayout.addWidget(
            self.buttonDeleteLaterGroupBox,  0, 1, 1, 1)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        self.scrollArea2 = QScrollArea(self.centralwidget)
        #  스크롤 가능 에어리어를 설정한다
        self.scrollArea2.setWidgetResizable(True)
        self.scrollAreaWidget2 = QWidget()
        # self.scrollAreaWidget.setGeometry(QRect(100, 100, 500, 500))
        self.scrollAreaWidgetLayout2 = QVBoxLayout(
            self.scrollAreaWidget2)
        self.scrollAreaWidgetLayout2.addItem(QSpacerItem(
            20, 40, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding))
        # 알파이자 오메가
        self.scrollArea2.setWidget(self.scrollAreaWidget2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# lastbutton
        self.finish = QWidget()
        self.suffle = QComboBox(self.finish)

        self.suffle.addItem(
            'BIG', 'FLAT')  # index 0
        self.suffle.addItem(
            'COLORCHANGE', ['Chicago', 'Springfield', 'Evanston', 'Skokie', 'Lincolnwood'])  # index 1
        self.suffle.currentIndexChanged.connect(self.dependent)

        # self.suffle = QPushButton(
        #     'logo1', self.finish)
        # self.buttonDeleteLaterGroupBox2 = QPushButton(
        #     'Del', self.finish)
        self.finishlayout = QGridLayout(self.finish)
        self.finishlayout.addWidget(
            self.suffle,          0, 0)
        # self.buttonLayout2.addWidget(
        #     self.buttonAddGroupBox2,  0, 1)

        # 버튼 레이아웃은 그리드 형태로 만든다
        # 이 방식의 핵심은 그리드 방식과 박스레이아웃의 컴플렉스이다
#
        self.first = QWidget()
        self.firstlabel = QLabel(
            'Item No', self.first)
        self.firstline = QLineEdit(self.first)
        self.firstLayout = QGridLayout(self.first)
        self.firstLayout.addWidget(
            self.firstlabel,          0, 0)
        self.firstLayout.addWidget(
            self.firstline,  0, 1)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        self.finalattack = QPushButton('GO')
        self.modifinalattack = QPushButton('SELECTGO')
        self.removbutton = QPushButton('REMOVE')
        self.picbalance = QComboBox()
        self.linkbutton = QPushButton('LINK')
        # self.removebutton = QPushButton('REMOVE')
        self.linkbutton.setMinimumWidth(315)

        self.picbalance.addItems(['topdown', 'center'])  # index 0
        self.centralwidgetLayout.addWidget(self.first)
        self.centralwidgetLayout.addWidget(
            self.linkbutton, alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralwidgetLayout.addWidget(self.buttonWidget)
        self.centralwidgetLayout.addWidget(self.scrollArea)
        self.centralwidgetLayout.addWidget(self.buttonWidget2)
        self.centralwidgetLayout.addWidget(self.scrollArea2)
        self.centralwidgetLayout.addWidget(self.finish)
        self.centralwidgetLayout.addWidget(self.picbalance)
        self.finalattack.setMinimumHeight(60)
        self.finalattack.clicked.connect(self.listLayoutChildWidgets)
        self.centralwidgetLayout.addWidget(self.finalattack)
        self.centralwidgetLayout.addWidget(self.modifinalattack)

        self.modifinalattack.clicked.connect(self.moditer)
        self.modifinalattack.clicked.connect(self.listLayoutChildWidgets)
        self.centralwidgetLayout.addWidget(self.removbutton)
        self.removbutton.clicked.connect(self.ruserious)
        self.setCentralWidget(self.centralwidget)

        self.buttonAddGroupBox.clicked.connect(self.addGroupBox)
        self.buttonDeleteLaterGroupBox.clicked.connect(
            self.deleteLaterGroupBox)

        self.buttonAddGroupBox2.clicked.connect(self.addGroupBox2)
        self.linkbutton.clicked.connect(self.linkgo)
        self.buttonDeleteLaterGroupBox2.clicked.connect(
            self.deleteLaterGroupBox2)
        self.setGeometry(500, 200, 350, 700)
        self.dependent(self.suffle.currentIndex())

    def moditer(self):
        print('ok')
        self.modi = True
        self.modiimg = QFileDialog.getOpenFileName(
            None, 'OpenFile', filter='*.png *.jpg')[0]

    def ruserious(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to remove?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.No:
            pass
        else:
            reply = QMessageBox.question(self, 'Message', 'Are you really sure to remove?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                try:

                    if self.thread[3].is_running == True:
                        self.thread[3].terminate()
                        self.thread[3].wait()

                except:

                    pass

                self.thread[3] = remover()

                self.thread[3].start()

            else:
                pass

    @pyqtSlot()
    def signal1_emitted(self):
        self.finalattack.setStyleSheet('background: red;')

    @pyqtSlot()
    def signal2_emitted(self):
        self.finalattack.setStyleSheet('background: green;')

    def linkgo(self):
        num = self.firstline.text()

        try:

            if self.thread[2].is_running == True:
                self.thread[2].terminate()
                self.thread[2].wait()

        except:

            pass

        self.thread[2] = urlworker(index=num)

        self.thread[2].start()

    def listLayoutChildWidgets(self):
        # 0 ==number 1=scrol1 2=scrol2 3=comboboxlayout

        number = self.firstline.text()
        scroll1_list = []
        scroll2_list = []
        comb_list = []
        scroll1 = self.centralwidgetLayout.itemAt(3).widget()
        scroll2 = self.centralwidgetLayout.itemAt(5).widget()
        comb = self.centralwidgetLayout.itemAt(6).widget()
        slines1 = scroll1.findChildren(QLineEdit)
        scroll1text_list = []
        for li in slines1:
            scroll1text_list.append(li.text())
        scroll1_list.append(scroll1text_list)
        slines1 = scroll1.findChildren(QComboBox)
        comb1text_list = []
        for li in slines1:
            comb1text_list.append(li.currentText())
        scroll1_list.append(comb1text_list)
        slines2 = scroll2.findChildren(QLineEdit)
        scroll2text_list = []
        for li in slines2:
            
            scroll2text_list.append(li.text())
            li.setText(str(''))
        scroll2_list.append(scroll2text_list)
        slines2 = scroll2.findChildren(QComboBox)
        comb2text_list = []
        for li in slines2:
            comb2text_list.append(li.currentText())
        scroll2_list.append(comb2text_list)

        comb = comb.findChildren(QComboBox)

        ficomb = self.picbalance.currentText()
        for li in comb:
            comb_list.append(li.currentText())
        finalagent = [number, scroll1_list, scroll2_list, comb_list, ficomb]

        if self.modi == True:
            finalagent.insert(len(finalagent), self.modiimg)
    
        if finalagent[3][1] == 'userselect':
            img = QFileDialog.getOpenFileName(
                None, 'OpenFile', filter='*.png *.jpg')[0]
            finalagent[3][1] = img

        if finalagent[3][2] == 'userselect':
            img = QFileDialog.getOpenFileName(
                None, 'OpenFile', filter='*.png *.jpg')[0]
            finalagent[3][2] = img

        try:

            if self.thread[1].is_running == True:
                self.thread[1].terminate()
                self.thread[1].wait()

        except:

            pass

        self.thread[1] = pixworker(index=finalagent)
        pixworkerman = self.thread[1]

        pixworkerman.signal1.connect(self.signal1_emitted)
        pixworkerman.signal2.connect(self.signal2_emitted)
        self.thread[1].start()
        self.modi = False

    def dependent(self, index):
     # index 0
        if index == 0:
            self.suffle1 = QComboBox()

            self.suffle1.addItems(
                ['america',  'canada',  'haccp', 'healthmark', 'void', 'userselect'])  # index 0
            self.suffle2 = QComboBox()

            self.suffle2.addItems(
                ['america',  'canada',  'haccp', 'healthmark', 'void', 'userselect'])
            self.finishlayout.addWidget(
                self.suffle1, 0, 1)
            self.finishlayout.addWidget(
                self.suffle2, 0, 2)
        else:
            self.suffle1.deleteLater()
            self.suffle2.deleteLater()

    def addGroupBox(self):
        count = self.scrollAreaWidgetLayout.count() - 1

        t = QTextEdit()
        groupBox = QGroupBox(self.scrollAreaWidget)
        #  이걸 잘 봐야한다 그룹박스를 선정하고 두번째 인자에 어떤녀석에게 넣을건지 표시한다
        #  파이큐티는 참 좆같이 만들었는데 박스에 넣을거 그냥 상위 개체에 넣게 표시하면 안되나? 왜 좆같이 하위개체가 상위계체를 선택하는지 모르겠다
        self.scrollAreaWidgetLayout.insertWidget(count, groupBox)

        comboBox = QComboBox(groupBox)
        comboBox.addItems(['sky', 'orange', 'yellow'])
        comboBox2 = QComboBox(groupBox)
        comboBox2.addItems(['1', '2'])

        gridLayout = QGridLayout(groupBox)
        gridLayout.addWidget(QLineEdit(groupBox), 0, 0)

        gridLayout.addWidget(comboBox, 0, 3)

        gridLayout.addWidget(comboBox2, 0, 4)

    def addGroupBox2(self):
        count = self.scrollAreaWidgetLayout2.count() - 1

        t = QTextEdit()
        groupBox = QGroupBox(self.scrollAreaWidget2)
        #  이걸 잘 봐야한다 그룹박스를 선정하고 두번째 인자에 어떤녀석에게 넣을건지 표시한다
        #  파이큐티는 참 좆같이 만들었는데 박스에 넣을거 그냥 상위 개체에 넣게 표시하면 안되나? 왜 좆같이 하위개체가 상위계체를 선택하는지 모르겠다
        self.scrollAreaWidgetLayout2.insertWidget(count, groupBox)

        comboBox = QComboBox(groupBox)
        comboBox.addItems(['sky', 'orange', 'yellow'])
        comboBox2 = QComboBox(groupBox)
        comboBox2.addItems(['1', '2'])

        gridLayout = QGridLayout(groupBox)
        gridLayout.addWidget(QLineEdit(groupBox), 0, 0)

        gridLayout.addWidget(comboBox, 0, 3)
        gridLayout.addWidget(comboBox2, 0, 4)

    def erasebutton(self):
        self.labelButton.deleteLater()
        self.buttonErase.deleteLater()

    def deleteLaterGroupBox(self):
        count = self.scrollAreaWidgetLayout.count()
        if count == 1:
            return
        item = self.scrollAreaWidgetLayout.itemAt(count - 2)
        widget = item.widget()
        widget.deleteLater()

    def deleteLaterGroupBox2(self):
        count = self.scrollAreaWidgetLayout2.count()
        if count == 1:
            return
        item = self.scrollAreaWidgetLayout2.itemAt(count - 2)
        widget = item.widget()
        widget.deleteLater()

    def removeItemGroupBox(self):
        count = self.scrollAreaWidgetLayout.count()
        if count == 1:
            return
        item = self.scrollAreaWidgetLayout.itemAt(count - 2)
        self.scrollAreaWidgetLayout.removeItem(item)

    def removeWidgetGroupBox(self):
        count = self.scrollAreaWidgetLayout.count()
        if count == 1:
            return
        item = self.scrollAreaWidgetLayout.itemAt(count - 2)
        widget = item.widget()
        self.scrollAreaWidgetLayout.removeWidget(widget)


class urlworker(QThread):

    def __init__(self,  index=0):
        super(urlworker, self).__init__()
        self.index = index

        self.is_running = True

    def run(self):

        num = self.index
        if 'b' in num:
            num =num[1:]
        try:
            t = requests.get(
                'http://www.msgood4u.com/html/search/search.php?skey=all&directsearch=y&searchTerm=&sword='+str(num)+'').text
            t = t.split('line_4')[1:]
            for li in t:
                lnum = li.split('상품코드 <span>')[1:][0]
                lnum = lnum.split('</span>')[0]
                if num == lnum:
                    target = li
                    break
            img = target.split("<img src='")[1:][0].split(' ')[0]
            if not "http" in img:
                img = 'http://www.msgood4u.com/'+img
            link = target.split("<a href='")[1:][0].split("'")[0]
            webbrowser.open(link)
        except:
            pass

class remover(QThread):

    def __init__(self,):
        super(remover, self).__init__()

        self.is_running = True

    def run(self):

        for file in os.scandir('big'):
            os.remove(file.path)
        for file in os.scandir('small'):
            os.remove(file.path)


class pixworker(QThread):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal()

    def __init__(self,  index=0):
        super(pixworker, self).__init__()
        self.index = index

        self.is_running = True

    def run(self):
        self.signal1.emit()

        num = self.index[0]
        try:

            if len(self.index) == 6:
                img = self.index[-1]
                img = Image.open(img)
                self.index = self.index[:-1]

            else:
                print('g')
                img = self.urlparser(num)
            print(len(self.index))
            xsize,ysize=img.size
            if not xsize == 1000:
                img = img.resize((1000,1000))

            image_list = self.splitim(img)
            if self.index[-2][0] == 'BIG':
                backgroundtext_list = self.textmaker(self.index[1:3],'BIG')
            if self.index[-2][0] == 'FLAT':
                backgroundtext_list = self.textmaker(self.index[1:3],'FLAT')
            final_list = self.logoplay(
                image_list, backgroundtext_list, self.index[-2])

            self.save(num, final_list)
            self.signal2.emit()
        except Exception as e:
            print(traceback.format_exc())
            self.signal2.emit()

    def imgselect(self, num):
        img = QFileDialog.getOpenFileName(
            None, 'OpenFile', filter='*.png *.jpg')[0]
        img = Image.open(img)
        return img

    def save(self, num, final_list):
        if num.isdigit():

            li = doubleagent.whiterbg(final_list[0])
            randomi = random.randrange(60, 100)
            li.save('small//a'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[1])
            # randomi = random.randrange(60, 100)
            # li.save('small//b'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[2])
            randomi = random.randrange(60, 100)
            li.save('small//a'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[3])
            # randomi = random.randrange(60, 100)
            # li.save('small//b'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[4])
            randomi = random.randrange(60, 100)
            li.save('small//a'+str(num)+'-3.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[5])
            # randomi = random.randrange(60, 100)
            # li.save('small//b'+str(num)+'-3.jpg', 'JPEG', quality=randomi)

            li = doubleagent.whiterbg(final_list[0])
            randomi = random.randrange(60, 100)
            li.save('big//a'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[1])
            # randomi = random.randrange(60, 100)
            # li.save('big//b'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[2])
            randomi = random.randrange(60, 100)
            li.save('big//a'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[3])
            # randomi = random.randrange(60, 100)
            # li.save('big//b'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[4])
            randomi = random.randrange(60, 100)
            li.save('big//a'+str(num)+'-3.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[5])
            # randomi = random.randrange(60, 100)
            # li.save('big//b'+str(num)+'-3.jpg', 'JPEG', quality=randomi)

        if 'b' in num:
            num =num[1:]
            li = doubleagent.whiterbg(final_list[0])
            randomi = random.randrange(60, 100)
            li.save('small//b'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[1])
            # randomi = random.randrange(60, 100)
            # li.save('small//b'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[2])
            randomi = random.randrange(60, 100)
            li.save('small//b'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[3])
            # randomi = random.randrange(60, 100)
            # li.save('small//b'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[4])
            randomi = random.randrange(60, 100)
            li.save('small//b'+str(num)+'-3.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[5])
            # randomi = random.randrange(60, 100)
            # li.save('small//b'+str(num)+'-3.jpg', 'JPEG', quality=randomi)

            li = doubleagent.whiterbg(final_list[0])
            randomi = random.randrange(60, 100)
            li.save('big//b'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[1])
            # randomi = random.randrange(60, 100)
            # li.save('big//b'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[2])
            randomi = random.randrange(60, 100)
            li.save('big//b'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[3])
            # randomi = random.randrange(60, 100)
            # li.save('big//b'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[4])
            randomi = random.randrange(60, 100)
            li.save('big//b'+str(num)+'-3.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[5])
            # randomi = random.randrange(60, 100)
            # li.save('big//b'+str(num)+'-3.jpg', 'JPEG', quality=randomi)
        if 'c' in num:
            num =num[1:]
            li = doubleagent.whiterbg(final_list[0])
            randomi = random.randrange(60, 100)
            li.save('small//c'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[1])
            # randomi = random.randrange(60, 100)
            # li.save('small//b'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[2])
            randomi = random.randrange(60, 100)
            li.save('small//c'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[3])
            # randomi = random.randrange(60, 100)
            # li.save('small//b'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[4])
            randomi = random.randrange(60, 100)
            li.save('small//c'+str(num)+'-3.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[5])
            # randomi = random.randrange(60, 100)
            # li.save('small//b'+str(num)+'-3.jpg', 'JPEG', quality=randomi)

            li = doubleagent.whiterbg(final_list[0])
            randomi = random.randrange(60, 100)
            li.save('big//c'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[1])
            # randomi = random.randrange(60, 100)
            # li.save('big//b'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[2])
            randomi = random.randrange(60, 100)
            li.save('big//c'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[3])
            # randomi = random.randrange(60, 100)
            # li.save('big//b'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[4])
            randomi = random.randrange(60, 100)
            li.save('big//c'+str(num)+'-3.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[5])
            # randomi = random.randrange(60, 100)
            # li.save('big//b'+str(num)+'-3.jpg', 'JPEG', quality=randomi)
        if 'd' in num:
            num =num[1:]
            li = doubleagent.whiterbg(final_list[0])
            randomi = random.randrange(60, 100)
            li.save('small//d'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[1])
            # randomi = random.randrange(60, 100)
            # li.save('small//b'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[2])
            randomi = random.randrange(60, 100)
            li.save('small//d'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[3])
            # randomi = random.randrange(60, 100)
            # li.save('small//b'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[4])
            randomi = random.randrange(60, 100)
            li.save('small//d'+str(num)+'-3.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[5])
            # randomi = random.randrange(60, 100)
            # li.save('small//b'+str(num)+'-3.jpg', 'JPEG', quality=randomi)

            li = doubleagent.whiterbg(final_list[0])
            randomi = random.randrange(60, 100)
            li.save('big//d'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[1])
            # randomi = random.randrange(60, 100)
            # li.save('big//b'+str(num)+'.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[2])
            randomi = random.randrange(60, 100)
            li.save('big//d'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[3])
            # randomi = random.randrange(60, 100)
            # li.save('big//b'+str(num)+'-2.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[4])
            randomi = random.randrange(60, 100)
            li.save('big//d'+str(num)+'-3.jpg', 'JPEG', quality=randomi)
            li = doubleagent.whiterbg(final_list[5])
            # randomi = random.randrange(60, 100)
            # li.save('big//b'+str(num)+'-3.jpg', 'JPEG', quality=randomi)


    def logoplay(self, image_list, backgroundtext_list, triger):
        fusion_list = []
        for image, backgroundtext in zip(image_list, backgroundtext_list):

            fusion = doubleagent.alpacomposite(backgroundtext, image, (0, 0))

            fusion_list.append(fusion)

        if 'america' == triger[1]:
            target1 = Image.open('logos//america.png')
        elif 'canada' == triger[1]:
            target1 = Image.open('logos//canada.png')
        elif 'france' == triger[1]:
            target1 = Image.open('logos//france.png')
        elif 'haccp' == triger[1]:
            target1 = Image.open('logos//haccp.png')
        elif 'healthmark' == triger[1]:
            target1 = Image.open('logos//healthmark.png')
        elif 'void' == triger[1]:
            target1 = Image.open('logos//void.png')
        else:
            target1 = Image.open(triger[1]).resize((290, 290))

        if 'america' == triger[2]:
            target2 = Image.open('logos//america.png')
        elif 'canada' == triger[2]:
            target2 = Image.open('logos//canada.png')
        elif 'france' == triger[2]:
            target2 = Image.open('logos//france.png')
        elif 'haccp' == triger[2]:
            target2 = Image.open('logos//haccp.png')
        elif 'healthmark' == triger[2]:
            target2 = Image.open('logos//healthmark.png')
        elif 'void' == triger[2]:
            target2 = Image.open('logos//void.png')
        else:
            target2 = Image.open(triger[2]).resize((290, 290))
        final_list = []
        for li in fusion_list:

            final1 = doubleagent.alpacomposite(li, target1, (700, 270))

            final1 = doubleagent.alpacomposite(final1, target2, (700, 590))
            final_list.append(final1)
            final2 = doubleagent.alpacomposite(li, target2, (700, 250))

            final2 = doubleagent.alpacomposite(final2, target1, (700, 600))
            final_list.append(final2)
        return final_list

    def urlparser(self, num):
        if 'b' in num:
            num = num[1:]
        if 'c' in num:
            num = num[1:]
        if 'd' in num:
            num = num[1:]
        if 'e' in num:
            num = num[1:]
        try:
            t = requests.get(
                'http://www.msgood4u.com/html/search/search.php?skey=all&directsearch=y&searchTerm=&sword='+str(num)+'').text
            t = t.split('line_4')[1:]


            for li in t:
                lnum = li.split('상품코드 <span>')[1:][0]
                lnum = lnum.split('</span>')[0]
                if num == lnum:
                    target = li
                    break
            img = target.split("<img src='")[1:][0].split(' ')[0]
            img = img.replace("'",'')
            if not "http" in img:
                img = 'http://www.msgood4u.com/'+img

            print(img)
            mem = requests.get(img).content

            b = BytesIO(mem)

            img1 = Image.open(b)
            deserialized_bytes = np.frombuffer(mem, dtype=np.int8)
            ImageFile.LOAD_TRUNCATED_IMAGES = True

            result = remove(img1)
            # pil_image=Image.fromarray(result)
            # pil_image.show()
            img = result.convert("RGBA")

            x, y = img.size

            px = img.load()

            for i in range(0, x):
                for j in range(0, y):
                    count = False
                    t = list(px[i, j])
                    if t[3] > 0:
                        t[3] = 256
                        count = True
                    if count == True and (t[0] + t[1] + t[2]) < 25:

                        t[3] = 0
                    if t[3] > 0:
                        t = [256, 256, 256, 256]
                    px[i, j] = tuple(t)
            filterd = img.convert('L')

            numpy_image = np.array(filterd)

            # convert to a openCV2 image and convert from RGB to BGR format
            img = cv.cvtColor(numpy_image, cv.COLOR_RGB2BGR)

            image_contours = np.zeros((img.shape[0], img.shape[1], 1), np.uint8)

            image_binary = np.zeros((img.shape[0], img.shape[1], 1), np.uint8)

            for channel in range(img.shape[2]):
                ret, image_thresh = cv.threshold(
                    img[:, :, channel], 127, 255, cv.THRESH_BINARY)
                contours = cv.findContours(image_thresh, 1, 1)[0]
                cv.drawContours(image_contours, contours, -
                                1, (255, 255, 255), -100)

            contours = cv.findContours(image_contours, cv.RETR_LIST,
                                    cv.CHAIN_APPROX_SIMPLE)[0]

            cv.drawContours(image_binary, [max(contours, key=cv.contourArea)],
                            -1, (255, 255, 255), -100)

            color_coverted = cv.cvtColor(image_binary, cv.COLOR_BGR2RGB)

            # convert from openCV2 to PIL
            pil_image = Image.fromarray(color_coverted).resize((986, 986))

            back = Image.new('RGB', (1000, 1000), (0, 0, 0))
            
            back.paste(pil_image, ((7, 7)))
            # Convert to grayscale
            mask = back.convert('L')

            # Threshold and invert the colors (white will be transparent)
            mask = mask.point(lambda x: x > 100 and 255)
            img1.putalpha(256)
            # The size of the images must match before apply the mask
            img = ImageOps.fit(img1, mask.size)

            img.putalpha(mask)  # Modifies the original image without return

            return img
        except:
            pass
    def textmaker(self, arg,texttype):
        itemcounter = arg[1][0]

        backgroundtext_list = []
        textint_list = []
        for li in itemcounter:
            counter = 0
            intstartcounter = None
            for q in li:

                if q.isdigit() == True and intstartcounter == None:
                    intstart = counter
                    intstartcounter = True

                if intstartcounter == True and q.isdigit() == True:
                    intend = counter
                counter = counter + 1
            textint = li[intstart:intend+1]
            textint_list.append(textint)
        # version1

        var1_list = []
        ontriger = True
        for li1, li2 in zip(itemcounter, textint_list):
            if ontriger == True:
                li = li1.replace(li2, str(int(li2)))
                var1_list.append(li)
                ontriger = False
                continue
            li = li1.replace(li2, str(int(li2)*2))
            var1_list.append(li)

        var1_list.insert(1, 'x2통 ')
        var2_list = []
        ontriger = True
        for li1, li2 in zip(itemcounter, textint_list):
            if ontriger == True:
                li = li1.replace(li2, str(int(li2)))
                var2_list.append(li)
                ontriger = False
                continue
            li = li1.replace(li2, str(int(li2)*4))
            var2_list.append(li)

        var2_list.insert(1, 'x4통 ')
        var3_list = []
        ontriger = True
        for li1, li2 in zip(itemcounter, textint_list):
            if ontriger == True:
                li = li1.replace(li2, str(int(li2)))
                var3_list.append(li)
                ontriger = False
                continue
            li = li1.replace(li2, str(int(li2)*6))
            var3_list.append(li)
        var3_list.insert(1, 'x6통 ')

        testttt = arg[1][1][:]
        testttt.insert(2, 'orange')
        testttt.insert(3, '1')
        var1_list[0] = var1_list[0]+' '
        underpreinput_list_list = [var1_list, var2_list, var3_list]
        underprecolor_list_list = [['yellow', 'orange', 'yellow'], [
            'yellow', 'orange', 'yellow'], ['yellow', 'orange', 'yellow']]
        underprerow_list_list = [['1', '1','1'], ['1', '1', '1'], ['1', '1', '1']]
        for underpreinput_list, underprecolor_list, underprerow_list in zip(underpreinput_list_list, underprecolor_list_list, underprerow_list_list):
            preinput_list = arg[0][0]

            prerow_list = arg[0][1][1::2]
            precolor_list = arg[0][1][0::2]

            sentence_list = []
            whool_list = []
            for input, color, row in zip(preinput_list, precolor_list, prerow_list):

                pre = []
                pre.append(input)
                pre.append(color)
                pre.append(row)
                sentence_list.append(pre)
            row1_list = []
            row2_list = []
            for li in sentence_list:
                if int(li[2]) == 1:
                    li = li[:-1]
                    row1_list.append(li)
                else:
                    li = li[:-1]
                    row2_list.append(li)

            dir = os.path.dirname(os.path.realpath(__file__))
            MAX_W, MAX_H = 1000, 1000
        
            im = Image.new('RGB', (MAX_W, MAX_H), (255, 255, 255))
            
            

            
            
            im.putalpha(1)
            blackpanel = Image.new('RGBA', (1000, 260), (0, 0, 0,256))
            im = doubleagent.alpacomposite(im,blackpanel,(0,0))
            draw = ImageDraw.Draw(im)
            if texttype == 'BIG':
                textsize = 100
                font = ImageFont.truetype(
                    dir+'/Jalnan.ttf', textsize)

                # row1

                xw_list = []
                for letter_list in row1_list:

                    xw, yh = draw.textsize(letter_list[0], font=font)

                    xw_list.append(xw)
                textrow1width = sum(xw_list)
                xw_list = []
                for letter_list in row1_list:

                    sentence = letter_list[0]
                    color = letter_list[1]
                    if color == 'orange':

                        xw, yh = draw.textsize(sentence, font=font)


                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 20),
                                sentence, '#FF0000', font=font, stroke_fill='#000000', stroke_width=5)
                        xw_list.append(xw)
                    if color == 'yellow':

                        xw, yh = draw.textsize(sentence, font=font)
   
 
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 20),
                                sentence, '#FFFF00', font=font, stroke_fill='#000000', stroke_width=5)
                        xw_list.append(xw)
                    if color == 'sky':
                        xw, yh = draw.textsize(sentence, font=font)


                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 20),
                                sentence, '#FFFFFF', font=font, stroke_fill='#000000', stroke_width=5)
                        xw_list.append(xw)
                xw_list = []
                font = ImageFont.truetype(
                    dir+'/Jalnan.ttf', 100)
                for letter_list in row2_list:

                    xw, yh = draw.textsize(letter_list[0], font=font)

                    xw_list.append(xw)
                textrow1width = sum(xw_list)
                xw_list = []
                


                for letter_list in row2_list:

                    sentence = letter_list[0]
                    color = letter_list[1]
                    if color == 'orange':

                        xw, yh = draw.textsize(sentence, font=font)


                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 140),
                                sentence, '#FF0000', font=font, stroke_fill='#000000', stroke_width=4)
                        xw_list.append(xw)
                    if color == 'yellow':
                        xw, yh = draw.textsize(sentence, font=font)


                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 140),
                                sentence, '#FFFF00', font=font, stroke_fill='#000000', stroke_width=4)
                        xw_list.append(xw)
                    if color == 'sky':
                        xw, yh = draw.textsize(sentence, font=font)


                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 140),
                                sentence, '#FFFFFF', font=font, stroke_fill='#000000', stroke_width=4)
                        xw_list.append(xw)
                # im.show()
                # underlinestart

                sentence_list = []
                whool_list = []
                for input, color, row in zip(underpreinput_list, underprecolor_list, underprerow_list):

                    pre = []
                    pre.append(input)
                    pre.append(color)
                    pre.append(row)
                    sentence_list.append(pre)
                row1_list = []
                row2_list = []
                for li in sentence_list:
                    if int(li[2]) == 1:
                        li = li[:-1]
                        row1_list.append(li)
                    else:
                        li = li[:-1]
                        row2_list.append(li)

                font = ImageFont.truetype(
                    dir+'/Jalnan.ttf', 100)

                # row1

                xw_list = []
                for letter_list in row1_list:

                    xw, yh = draw.textsize(letter_list[0], font=font)

                    xw_list.append(xw)
                textrow1width = sum(xw_list)
                xw_list = []
                for letter_list in row1_list:

                    sentence = letter_list[0]
                    color = letter_list[1]
                    if color == 'orange':

                        xw, yh = draw.textsize(sentence, font=font)


                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 895),
                                sentence, '#FFAC95', font=font, stroke_fill='#000000', stroke_width=6)
                        xw_list.append(xw)
                    if color == 'yellow':
                        xw, yh = draw.textsize(sentence, font=font)


                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 895),
                                sentence, '#FFFF00', font=font, stroke_fill='#000000', stroke_width=6)
                        xw_list.append(xw)
                    if color == 'sky':
                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 895),
                                sentence, '#B9E9FF', font=font, stroke_fill='#000000', stroke_width=6)
                        xw_list.append(xw)
                xw_list = []

                for letter_list in row2_list:

                    xw, yh = draw.textsize(letter_list[0], font=font)

                    xw_list.append(xw)
                textrow1width = sum(xw_list)
                xw_list = []
                for letter_list in row2_list:

                    sentence = letter_list[0]
                    color = letter_list[1]
                    if color == 'orange':

                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list)+6, 900+6),
                                sentence, '#3D1C1C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 900),
                                sentence, '#F0502D', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        xw_list.append(xw)
                    if color == 'yellow':
                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list)+6, 900+6),
                                sentence, '#3D1C1C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 900),
                                sentence, '#FFE38C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        xw_list.append(xw)
                    if color == 'sky':
                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list)+6, 900+6),
                                sentence, '#3D1C1C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 900),
                                sentence, '#9CC7FA', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        xw_list.append(xw)

                backgroundtext_list.append(im)     
            # big 타입 아닐경우
            else:
                textsize = 95
                font = ImageFont.truetype(
                    dir+'/Jalnan.ttf', textsize)

                # row1

                xw_list = []
                for letter_list in row1_list:

                    xw, yh = draw.textsize(letter_list[0], font=font)

                    xw_list.append(xw)
                textrow1width = sum(xw_list)
                xw_list = []
                for letter_list in row1_list:

                    sentence = letter_list[0]
                    color = letter_list[1]
                    if color == 'orange':

                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 20+6),
                                sentence, '#000000', font=font, stroke_fill='#000000', stroke_width=5)
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 20),
                                sentence, '#FFAC95', font=font, stroke_fill='#3D1C1C', stroke_width=5)
                        xw_list.append(xw)
                    if color == 'yellow':
                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 20+6),
                                sentence, '#000000', font=font, stroke_fill='#000000', stroke_width=5)
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 20),
                                sentence, '#FFFF00', font=font, stroke_fill='#000000', stroke_width=5)
                        xw_list.append(xw)
                    if color == 'sky':
                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list)+6, 20+6),
                                sentence, '#3D1C1C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 20),
                                sentence, '#9CC7FA', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        xw_list.append(xw)
                xw_list = []

                for letter_list in row2_list:

                    xw, yh = draw.textsize(letter_list[0], font=font)

                    xw_list.append(xw)
                textrow1width = sum(xw_list)
                xw_list = []
                
                font = ImageFont.truetype(
                    dir+'/Jalnan.ttf', 100)

                for letter_list in row2_list:

                    sentence = letter_list[0]
                    color = letter_list[1]
                    if color == 'orange':

                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list)+6, 115+7),
                                sentence, '#3D1C1C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 115),
                                sentence, '#EC292D', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        xw_list.append(xw)
                    if color == 'yellow':
                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list)+6, 115+7),
                                sentence, '#3D1C1C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 115),
                                sentence, '#FFE38C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        xw_list.append(xw)
                    if color == 'sky':
                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list)+6, 115+7),
                                sentence, '#3D1C1C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 115),
                                sentence, '#9CC7FA', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        xw_list.append(xw)
                # im.show()
                # underlinestart

                sentence_list = []
                whool_list = []
                for input, color, row in zip(underpreinput_list, underprecolor_list, underprerow_list):

                    pre = []
                    pre.append(input)
                    pre.append(color)
                    pre.append(row)
                    sentence_list.append(pre)
                row1_list = []
                row2_list = []
                for li in sentence_list:
                    if int(li[2]) == 1:
                        li = li[:-1]
                        row1_list.append(li)
                    else:
                        li = li[:-1]
                        row2_list.append(li)

                font = ImageFont.truetype(
                    dir+'/Jalnan.ttf', 100)

                # row1

                xw_list = []
                for letter_list in row1_list:

                    xw, yh = draw.textsize(letter_list[0], font=font)

                    xw_list.append(xw)
                textrow1width = sum(xw_list)
                xw_list = []
                for letter_list in row1_list:

                    sentence = letter_list[0]
                    color = letter_list[1]
                    if color == 'orange':

                        xw, yh = draw.textsize(sentence, font=font)


                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 900),
                                sentence, '#EC292D', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        xw_list.append(xw)
                    if color == 'yellow':
                        xw, yh = draw.textsize(sentence, font=font)


                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 900),
                                sentence, '#FFE38C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        xw_list.append(xw)
                    if color == 'sky':
                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list)+6, 900+6),
                                sentence, '#3D1C1C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 900),
                                sentence, '#9CC7FA', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        xw_list.append(xw)
                xw_list = []

                for letter_list in row2_list:

                    xw, yh = draw.textsize(letter_list[0], font=font)

                    xw_list.append(xw)
                textrow1width = sum(xw_list)
                xw_list = []
                for letter_list in row2_list:

                    sentence = letter_list[0]
                    color = letter_list[1]
                    if color == 'orange':

                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list)+6, 900+6),
                                sentence, '#3D1C1C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 900),
                                sentence, '#F0502D', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        xw_list.append(xw)
                    if color == 'yellow':
                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list)+6, 900+6),
                                sentence, '#3D1C1C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 900),
                                sentence, '#FFE38C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        xw_list.append(xw)
                    if color == 'sky':
                        xw, yh = draw.textsize(sentence, font=font)

                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list)+6, 900+6),
                                sentence, '#3D1C1C', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        draw.text(((MAX_W - textrow1width) / 2+sum(xw_list), 900),
                                sentence, '#9CC7FA', font=font, stroke_fill='#3D1C1C', stroke_width=3)
                        xw_list.append(xw)

                backgroundtext_list.append(im)

        return backgroundtext_list

    def splitim(self, solo):
        backgound = solo

        imgArray = np.array(backgound)
        nomal = imgArray.tolist()
        count = 0
        for y, li1 in enumerate(nomal):

            if count == 1:
                break
            for x, li2 in enumerate(li1):
                if count == 1:
                    break

                if not li2[3] == 0:
                    y1 = y

                    count = 1

        lotate90 = backgound.transpose(Image.ROTATE_270)
        lotate90 = np.array(lotate90)
        lotate90 = lotate90.tolist()
        count = 0
        for y, li1 in enumerate(lotate90):

            if count == 1:
                break
            for x, li2 in enumerate(li1):
                if count == 1:
                    break

                if not li2[3] == 0:
                    x1 = y

                    count = 1

        lotate180 = backgound.transpose(Image.ROTATE_180)
        lotate180 = np.array(lotate180)
        lotate180 = lotate180.tolist()
        count = 0
        for y, li1 in enumerate(lotate180):

            if count == 1:
                break
            for x, li2 in enumerate(li1):
                if count == 1:
                    break

                if not li2[3] == 0:
                    y2 = y

                    count = 1

        lotate90 = backgound.transpose(Image.ROTATE_90)
        lotate90 = np.array(lotate90)
        lotate90 = lotate90.tolist()
        count = 0
        for y, li1 in enumerate(lotate90):

            if count == 1:
                break
            for x, li2 in enumerate(li1):
                if count == 1:
                    break

                if not li2[3] == 0:
                    x2 = y

                    count = 1
        f = backgound.crop((x1, y1, 1000-x2, 1000-y2))

        x, y = f.size
        if y > x:
            print('y')
            ratio = 630/y
            f1 = f.resize((round(x*ratio), round(y*ratio)))
            prebackground = Image.new('RGBA', (630, 630), (255, 255, 255, 0))
            result1 = doubleagent.alpacomposite(
                prebackground, f1, ((round((650-round(x*ratio))/2)), round(((650-round(y*ratio))/2))))
            background = Image.new('RGBA', (1000, 1000), (255, 255, 255, 0))
            result1 = doubleagent.alpacomposite(
                background, result1, (10, 260))

            ratio = 540/y
            f1 = f.resize((round(x*ratio), round(y*ratio)))
            prebackground = Image.new('RGBA', (630, 630), (255, 255, 255, 0))
            result2 = doubleagent.alpacomposite(
                prebackground, f1, (0, 0))
            result2 = doubleagent.alpacomposite(result2, f1, (80, 80))
            background = Image.new('RGBA', (1000, 1000), (255, 255, 255, 0))
            lx, ly, llx, lly = doubleagent.rectangularcroplocation(result2)
            result2 = doubleagent.alpacomposite(background, result2, ((
                round(10+(650-(llx-lx))/2), round(260+(650-(lly-ly))/2))))

            ratio = 520/y
            f2 = f.resize((round(x*ratio), round(y*ratio)))
            prebackground = Image.new('RGBA', (630, 630), (255, 255, 255, 0))
            result3 = doubleagent.alpacomposite(
                prebackground, f2, (0, 0))
            result3 = doubleagent.alpacomposite(result3, f2, (50, 50))
            result3 = doubleagent.alpacomposite(result3, f2, (100, 100))
            lx, ly, llx, lly = doubleagent.rectangularcroplocation(result2)
            result3 = doubleagent.alpacomposite(background, result3, ((
                round(10+(650-(llx-lx))/2), round(260+(650-(lly-ly))/2))))
            image_list = [result1, result2, result3]

        else:
            print('x')
            ratio = 620/x
            f1 = f.resize((round(x*ratio), round(y*ratio)))
            prebackground = Image.new('RGBA', (630, 630), (255, 255, 255, 0))
            result1 = doubleagent.alpacomposite(
                prebackground, f1, ((round((630-round(x*ratio))/2)), round(((630-round(y*ratio))/2))))
            background = Image.new('RGBA', (1000, 1000), (255, 255, 255, 0))
            result1 = doubleagent.alpacomposite(
                background, result1, (30, 255))

            ratio = 550/x
            f1 = f.resize((round(x*ratio), round(y*ratio)))
            prebackground = Image.new('RGBA', (630, 630), (255, 255, 255, 0))
            result2 = doubleagent.alpacomposite(
                prebackground, f1, (0, 0))
            result2 = doubleagent.alpacomposite(result2, f1, (70, 70))
            background = Image.new('RGBA', (1000, 1000), (255, 255, 255, 0))
            lx, ly, llx, lly = doubleagent.rectangularcroplocation(result2)
            result2 = doubleagent.alpacomposite(background, result2, ((
                round(35+(630-(llx-lx))/2), round(255+(620-(lly-ly))/2))))

            ratio = 530/x
            f2 = f.resize((round(x*ratio), round(y*ratio)))
            prebackground = Image.new('RGBA', (630, 630), (255, 255, 255, 0))
            result3 = doubleagent.alpacomposite(
                prebackground, f2, (0, 0))
            result3 = doubleagent.alpacomposite(result3, f2, (50, 50))
            result3 = doubleagent.alpacomposite(result3, f2, (100, 100))
            lx, ly, llx, lly = doubleagent.rectangularcroplocation(result2)
            result3 = doubleagent.alpacomposite(background, result3, ((
                round(35+(630-(llx-lx))/2), round(255+(620-(lly-ly))/2))))
            image_list = [result1, result2, result3]
            
        return image_list


def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    app.exec()


if __name__ == '__main__':
    main()
