# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.bat = 0
        self.bow = 0
        self.ar = 0
        self.wk = 0
        self.used = 0
        self.avail = 0
        self.name = ""

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 649)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        MainWindow.setPalette(palette)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(600, 600, 300, 200))
        self.openGLWidget.setObjectName("openGLWidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 30, 1011, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(198, 195, 195);\n"
                                        "border: 3px black;\n"
                                        " margin-top: 0ex;\n"
                                        "\n"
                                        "")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 30, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(250, 30, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(500, 30, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(740, 30, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.bat_count = QtWidgets.QLineEdit(self.groupBox_2)
        self.bat_count.setGeometry(QtCore.QRect(170, 30, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bat_count.setFont(font)
        self.bat_count.setStyleSheet("background-color: white;\n"
                                        "color:green;")
        
        self.bat_count.setAlignment(QtCore.Qt.AlignCenter)
        self.bat_count.setObjectName("bat_count")
        self.bowl_count = QtWidgets.QLineEdit(self.groupBox_2)
        self.bowl_count.setGeometry(QtCore.QRect(400, 30, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bowl_count.setFont(font)
        self.bowl_count.setStyleSheet("background-color: white;\n"
                                      "color:green;")
        
        self.bowl_count.setAlignment(QtCore.Qt.AlignCenter)
        self.bowl_count.setObjectName("bowl_count")
        self.ar_count = QtWidgets.QLineEdit(self.groupBox_2)
        self.ar_count.setGeometry(QtCore.QRect(660, 30, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ar_count.setFont(font)
        self.ar_count.setStyleSheet("background-color: white;\n"
                                    "color:green;")
        
        self.ar_count.setAlignment(QtCore.Qt.AlignCenter)
        self.ar_count.setObjectName("ar_count")
        self.wk_count = QtWidgets.QLineEdit(self.groupBox_2)
        self.wk_count.setGeometry(QtCore.QRect(950, 30, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wk_count.setFont(font)
        self.wk_count.setStyleSheet("background-color: white;\n"
                                    "color:green;")
        
        self.wk_count.setAlignment(QtCore.Qt.AlignCenter)
        self.wk_count.setObjectName("wk_count")
        self.bat_count.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.bowl_count.raise_()
        self.ar_count.raise_()
        self.wk_count.raise_()
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.points_avail = QtWidgets.QLineEdit(self.centralwidget)
        self.points_avail.setGeometry(QtCore.QRect(240, 130, 81, 31))
        self.points_avail.setStyleSheet("color:green;")
        
        self.points_avail.setObjectName("points_avail")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(80, 170, 380, 420))
        self.groupBox.setStyleSheet("background-color: white;\n"
                                    "border-style: solid;\n"
                                    "border-width: 2px;\n"
                                    "border-color: black;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.check_bat = QtWidgets.QRadioButton(self.groupBox)
        self.check_bat.setGeometry(QtCore.QRect(28, 10, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.check_bat.setFont(font)
        self.check_bat.setObjectName("check_bat")
        self.check_bowl = QtWidgets.QRadioButton(self.groupBox)
        self.check_bowl.setGeometry(QtCore.QRect(116, 10, 62, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.check_bowl.setFont(font)
        self.check_bowl.setObjectName("check_bowl")
        self.check_ar = QtWidgets.QRadioButton(self.groupBox)
        self.check_ar.setGeometry(QtCore.QRect(204, 10, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.check_ar.setFont(font)
        self.check_ar.setObjectName("check_ar")
        self.check_wk = QtWidgets.QRadioButton(self.groupBox)
        self.check_wk.setGeometry(QtCore.QRect(292, 10, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.check_wk.setFont(font)
        self.check_wk.setObjectName("check_wk")
        self.add_player = QtWidgets.QListWidget(self.groupBox)
        self.add_player.setGeometry(QtCore.QRect(65, 70, 250, 331))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_player.setFont(font)
        self.add_player.setStyleSheet("border-style: solid;\n"
                                        "border-width: 0px;\n"
                                        "border-color: white;\n"
                                        "color:rgb(0, 255, 255);")
        self.add_player.setObjectName("add_player")
        self.points_used = QtWidgets.QLineEdit(self.centralwidget)
        self.points_used.setGeometry(QtCore.QRect(790, 130, 81, 31))
        self.points_used.setStyleSheet("color:green;")
        
        self.points_used.setObjectName("points_used")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(670, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(670, 170, 380, 420))
        self.groupBox_3.setStyleSheet("background-color: white;\n"
                                        "border-style: solid;\n"
                                        "border-width: 2px;\n"
                                        "border-color: black;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 5, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-style: solid;\n"
                                "border-width: 0px;\n"
                                "border-color: white;")
        self.label_7.setObjectName("label_7")
        self.team_name = QtWidgets.QLineEdit(self.groupBox_3)
        self.team_name.setGeometry(QtCore.QRect(130, 5, 211, 31))
        self.team_name.setStyleSheet("border-color: white;\n"
                                        "color:green;")
        self.team_name.setText("####")
        self.team_name.setObjectName("team_name")
        self.check_player = QtWidgets.QListWidget(self.groupBox_3)
        self.check_player.setGeometry(QtCore.QRect(65, 70, 250, 331))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.check_player.setFont(font)
        self.check_player.setStyleSheet("border-style: solid;\n"
                                        "border-width: 0px;\n"
                                        "border-color: white;\n"
                                        "color:rgb(0, 255, 255);")
        self.check_player.setObjectName("check_player")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(540, 320, 31, 31))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/image/right.png"))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 26))
        self.menubar.setObjectName("menubar")
        self.manage = QtWidgets.QMenu(self.menubar)
        self.manage.setObjectName("manage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.bat_count.setText("##")
        self.bowl_count.setText("##")
        self.ar_count.setText("##")
        self.wk_count.setText("##")
        self.points_avail.setText("####")
        self.points_used.setText("####")

        
        self.New = QtWidgets.QAction(MainWindow)
        self.New.setObjectName("New")
        
        self.open = QtWidgets.QAction(MainWindow)
        self.open.setObjectName("open")
        
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        
        self.evaluate = QtWidgets.QAction(MainWindow)
        self.evaluate.setObjectName("evaluate")
        
        
        self.manage.addAction(self.New)
        self.manage.addAction(self.open)
        self.manage.addAction(self.save)
        self.manage.addAction(self.evaluate)
        self.menubar.addAction(self.manage.menuAction())

        self.New.triggered.connect(lambda: self.clicked("New"))
        self.open.triggered.connect(lambda: self.clicked("open"))
        self.save.triggered.connect(lambda: self.clicked("save"))
        self.evaluate.triggered.connect(lambda: self.clicked("evaluate"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Your Selection"))
        self.label.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.label_2.setText(_translate("MainWindow", "Bowler(BOW)"))
        self.label_3.setText(_translate("MainWindow", "Allrounder(AR)"))
        self.label_4.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.label_5.setText(_translate("MainWindow", "Points Available:"))
        self.check_bat.setText(_translate("MainWindow", "BAT"))
        self.check_bowl.setText(_translate("MainWindow", "BOW"))
        self.check_ar.setText(_translate("MainWindow", "AR"))
        self.check_wk.setText(_translate("MainWindow", "WK"))
        self.label_6.setText(_translate("MainWindow", "Points Used:"))
        self.label_7.setText(_translate("MainWindow", "Team Name:"))
        self.manage.setTitle(_translate("MainWindow", "Manage Teams"))
        self.New.setText(_translate("MainWindow", "New Team"))
        self.New.setStatusTip(_translate("MainWindow", "Create Your Team"))
        self.New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.open.setText(_translate("MainWindow", "Open Team"))
        self.open.setStatusTip(_translate("MainWindow", "Open previously created team"))
        self.open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.save.setText(_translate("MainWindow", "Save Team"))
        self.save.setStatusTip(_translate("MainWindow", "Save created team"))
        self.save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.evaluate.setText(_translate("MainWindow", "Evaluate Score"))
        self.evaluate.setStatusTip(_translate("MainWindow", "Evaluate the score of selected team"))
        self.evaluate.setShortcut(_translate("MainWindow", "Ctrl+E"))
    
    def setFields(self):
        self.bat_count.setText(str(self.bat))
        self.bowl_count.setText(str(self.bow))
        self.ar_count.setText(str(self.ar))
        self.wk_count.setText(str(self.wk))
        self.points_avail.setText(str(self.avail))
        self.points_used.setText(str(self.used))
        self.team_name.setText(str(self.name))
    
    def clicked(self,text):
        if text == "New":
            name, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team Name", "Enter name of team:")
            if ok:
                if name !="":
                    self.name = name
                    self.avail = 1000
                    self.setFields()
                else:
                    while ok and name == "":
                        name, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team Name", "Enter name of team:")



        elif text == "open":
            print(text)
        elif text == "save":
            print(text)

        elif text == "evaluate":
            from dialog import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()
        
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
