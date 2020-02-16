from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from time import sleep

class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow,self).__init__()
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("Ash Tech Blogs")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first app")
        self.label.move(200,200)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("pressed the application button for long time    ")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = myWindow()
    # win.setGeometry(0,100,300,300)   #x,y,w,h
    # win.setWindowTitle("AshTechBlogs")
    # label = QtWidgets.QLabel(win)
    # label.setText("my first app")
    # label.move(50,50)
    win.show()
    sys.exit(app.exec_())

window()