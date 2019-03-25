# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kon-boot\Desktop\untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

#import qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidget
#import doc
from docxtpl import *
from pandas import *
import os

class general():
    db_file = {}
    templates = ''
    doc = ''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 677)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 681, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_2.addWidget(self.toolButton_2, 3, 2, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout_2.addWidget(self.toolButton_3, 5, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 5, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 260, 681, 371))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.tableWidget.setRowCount(2000)
        self.tableWidget.setColumnCount(2000)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()

        for x in range(0,2000):
            self.tableWidget.setItem(0, x, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(1, x, item)
            item = QtWidgets.QTableWidgetItem()


        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()


        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 640, 201, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #connection
        self.toolButton.clicked.connect(self.toolbutton_1Clicked)
        self.toolButton_2.clicked.connect(self.toolbutton_2Clicked)
        self.toolButton_3.clicked.connect(self.toolbutton_3Clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2Clicked)
        #close connection

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("genDoc", "genDoc"))
        self.label_3.setText(_translate("MainWindow", "Выберите папку для сохранения созданных файлов"))
        self.label_2.setText(_translate("MainWindow", "Выберите папку с шаблонами"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Выберите файл базы данных"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("MainWindow", "Генерировать"))


    def readyorno(self):
        if len(general.doc)>= 1 and len(general.templates)>= 1 and len(general.db_file)>= 1:
            self.pushButton_2.setStyleSheet('color: green')
        else:
            self.pushButton_2.setStyleSheet('color: red')
 
#выбор файла базы данных
    def toolbutton_1Clicked(self):
        try:
            _translate = QtCore.QCoreApplication.translate
            file_name = QFileDialog.getOpenFileName(None,'OpenFile','',"(*.xls;*.xlsx)")
            self.lineEdit.setText(_translate("MainWindow", str(file_name[0])))
            if len(file_name[0]) >= 1:
                self.label.setStyleSheet('color: green')
            else:
                self.label.setStyleSheet('color: red')
            #подключаемся к базе и формируем словарь
            xls = ExcelFile(str(file_name[0]))
            df = xls.parse(xls.sheet_names[0])
            #конвертация в словарь
            b = df.to_dict()
            canvas = {}
            for x,y in b.items():
                canvas[x] = y[0]
            general.db_file = canvas
            #print(general.db_file)
            self.readyorno()
                
            row = 0
            for x, y in canvas.items():
                if x is None:
                    x,y = 'yb'
                else:
                    try:
                        item = self.tableWidget.item(0, row)
                        #print(str('*') + x)
                        item.setText(_translate("MainWindow", x))


                        item = self.tableWidget.item(1, row)
                        #print(str('*') + y)
                        item.setText(_translate("MainWindow", y))
                        
                        row+=1
                    except Exception as e:
                        print(e)               

        except Exception as e:
            print(e)

#выбор папки с шаблонами
    def toolbutton_2Clicked(self):
        try:
            _translate = QtCore.QCoreApplication.translate
            file_name = QFileDialog.getExistingDirectory()
            self.lineEdit_2.setText(_translate("MainWindow", str(file_name)))
            general.templates = file_name

            if len(file_name[0]) >= 1:
                self.label_2.setStyleSheet('color: green')
            else:
                self.label_2.setStyleSheet('color: red')
            self.readyorno()
        except Exception as e:
            print(e)

#выбор папки для сохранения генеририемого контента
    def toolbutton_3Clicked(self):
        try:
            _translate = QtCore.QCoreApplication.translate
            file_name = QFileDialog.getExistingDirectory()
            self.lineEdit_3.setText(_translate("MainWindow", str(file_name)))
            general.doc = file_name

            if len(file_name[0]) >= 1:
                self.label_3.setStyleSheet('color: green')
            else:
                self.label_3.setStyleSheet('color: red')
            self.readyorno()

        except Exception as e:
            print(e)
            
    def pushButton_2Clicked(self):
        #получаем все директории в папке шаблона
        tree = os.listdir(general.templates)
        
        for branch in tree:
            #проверяем существует ли директория
            if not os.path.exists(general.doc+'/'+branch):
                os.makedirs(general.doc+'/'+branch)

            files = os.listdir(general.templates+'/'+branch)
            
            work = 0
            dont_work = 0
            
            for f in files:
                print(f)
                try:
                    tpl = DocxTemplate(general.templates+"/"+str(branch)+"/"+str(f))
                    tpl.render(general.db_file)
                    tpl.save(general.doc+"/"+str(branch)+"/"+str(f))
                    work+=1
                except:
                    print('Не сработало с:' + str(f))
                    dont_work+=1
            print("сработало с - "+ str(work))
            print("не сработало с - "+ str(dont_work))


       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


