import random as rd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# ------------------------------------------------ FIRST PART ------------------------------------------ #
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(478, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.picture_label = QtWidgets.QLabel(self.centralwidget)
        self.picture_label.setGeometry(QtCore.QRect(20, 10, 441, 231))
        self.picture_label.setFrameShape(QtWidgets.QFrame.Box)
        self.picture_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.picture_label.setText("")
        self.picture_label.setPixmap(QtGui.QPixmap("vs code files/trapecia.jpg"))
        self.picture_label.setScaledContents(True)
        self.picture_label.setObjectName("picture_label")
        
        self.answer_label = QtWidgets.QLabel(self.centralwidget)
        self.answer_label.setGeometry(QtCore.QRect(20, 250, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.answer_label.setFont(font)
        self.answer_label.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.answer_label.setFrameShape(QtWidgets.QFrame.Box)
        self.answer_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.answer_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.answer_label.setObjectName("answer_label")
        
        self.calculate_area = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_area.setGeometry(QtCore.QRect(30, 330, 420, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calculate_area.setFont(font)
        self.calculate_area.setStyleSheet("border-color: rgb(186, 186, 186);")
        self.calculate_area.setObjectName("calculate_area")
        
        self.message_box = QtWidgets.QPushButton(self.centralwidget)
        self.message_box.setGeometry(QtCore.QRect(250, 400, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.message_box.setFont(font)
        self.message_box.setStyleSheet("border-color: rgb(186, 186, 186);")
        self.message_box.setObjectName("message_box")
        
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(130, 470, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.close.setFont(font)
        self.close.setStyleSheet("border-color: rgb(186, 186, 186);")
        self.close.setObjectName("close")
        
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(50, 400, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear_button.setFont(font)
        self.clear_button.setStyleSheet("border-color: rgb(186, 186, 186);")
        self.clear_button.setObjectName("clear_button")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 478, 21))
        self.menubar.setObjectName("menubar")
        self.menuChoose_Figure = QtWidgets.QMenu(self.menubar)
        self.menuChoose_Figure.setObjectName("menuChoose_Figure")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.Trapecia = QtWidgets.QAction(MainWindow)
        self.Trapecia.setObjectName("Trapecia")
        self.Martkutxedi = QtWidgets.QAction(MainWindow)
        self.Martkutxedi.setObjectName("Martkutxedi")
        self.Kvadrati = QtWidgets.QAction(MainWindow)
        self.Kvadrati.setObjectName("Kvadrati")
        
        self.menuChoose_Figure.addAction(self.Trapecia)
        self.menuChoose_Figure.addAction(self.Martkutxedi)
        self.menuChoose_Figure.addAction(self.Kvadrati)
        self.menubar.addAction(self.menuChoose_Figure.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.message_box.clicked.connect(self.show_popup)

# --------------------------------------------- LOGIC --------------------------------------------------------------- #
        # call pictures:
        self.Trapecia.triggered.connect(lambda: self.show_trapezoid())
        self.Martkutxedi.triggered.connect(lambda: self.show_rectangle())
        self.Kvadrati.triggered.connect(lambda: self.show_square())

        # call button functions:
        self.calculate_area.clicked.connect(self.Figure_Area)
        self.clear_button.clicked.connect(self.Remove)
        self.close.clicked.connect(MainWindow.close)
        
    # define show_figures function:
    def show_trapezoid(self):
        self.picture_label.setPixmap(QtGui.QPixmap("trapecia.jpg"))
        self.answer_label.setText(f'Area of Trapezoid:')
    def show_rectangle(self):
        self.picture_label.setPixmap(QtGui.QPixmap("martkutxedi.jpg"))
        self.answer_label.setText(f'Area of Rectangle:')
    def show_square(self):
        self.picture_label.setPixmap(QtGui.QPixmap("kvadrati.jpg"))
        self.answer_label.setText(f'Area of Square:')
    
    # choose which figures area should be shown:
    def Figure_Area(self):
        #menu_text = self.menuChoose_Figure
        screen = self.answer_label.text()
        if "Trapezoid" in screen:
            trp_1 = Trapecia(Digit_list[0])
            self.answer_label.setText(f'{screen} {trp_1.t_fartobi()} m\u00b2')
        elif "Rectangle" in screen:
            mrt_1 = Martkutxedi(Digit_list[0])
            self.answer_label.setText(f'{screen} {mrt_1.m_fartobi()} m\u00b2')
        elif "Square" in screen:
            kvt_1 = Kvadrati(Digit_list[0])
            self.answer_label.setText(f'{screen} {kvt_1.k_fartobi()} m\u00b2')
# ------------------------------------------------------------------------------------------------ #
    
    # define function for Clear Button:
    def Remove(self):
        self.answer_label.setText("0")
        self.picture_label.setPixmap(QtGui.QPixmap(""))
    
    # define function for message box button:
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Hello, World")
        msg.setText("Welcome To Main Window!")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
        msg.setDefaultButton(QMessageBox.Retry)
        msg.setInformativeText("Informative Text!")
        msg.setDetailedText("By Order Of The Peacky Blinders!")

        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_()

    def popup_button(self, i):
        print(i.text())
        
# ----------------------------------------------------------------------------------------------------------------- #

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.answer_label.setText(_translate("MainWindow", "0"))
        self.calculate_area.setText(_translate("MainWindow", "Calculate Area"))
        self.message_box.setText(_translate("MainWindow", "Message Box"))
        self.close.setText(_translate("MainWindow", "CLOSE APP"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.menuChoose_Figure.setTitle(_translate("MainWindow", "Choose Figure"))
        self.Trapecia.setText(_translate("MainWindow", "Trapecia"))
        self.Martkutxedi.setText(_translate("MainWindow", "Martkutxedi"))
        self.Kvadrati.setText(_translate("MainWindow", "Kvadrati"))

# ------------------------------------------------ SECOND PART ------------------------------------------ #
Digit_list = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for i in range(10)]

class Trapecia(Ui_MainWindow):
    def __init__(self, digit):
        super().__init__()
        self.fudze1 = digit[0]
        self.fudze2 = digit[1]
        self.simagle = digit[2]
    def __str__(self):
        return str(self.fudze1)+", "+str(self.fudze2)+", "+ str(self.simagle)
    def t_fartobi(self):
        return (self.fudze1 + self.fudze2) / 2 * self.simagle 
    def __le__(self, other):
        return self.fartobi() <= other.fartobi()
    def __eq__(self, other):
        return self.fartobi() == other.fartobi()
           
class Martkutxedi(Trapecia):
    def __init__(self, digit):
        super().__init__(digit)
        self.simagle = None
    def __str__(self):
        return str(self.fudze1)+", "+ str(self.fudze2)
    
    def m_fartobi(self):
        return self.fudze1 * self.fudze2

class Kvadrati(Martkutxedi):
    def __init__(self, digit):
        super().__init__(digit)
        self.fudze2 = None
    def __str__(self):
        return str(self.fudze1)
    
    def k_fartobi(self):
       return self.fudze1**2

# ------------------------------------------------ LAST PART ------------------------------------------ #

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

