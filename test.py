from PyQt5 import uic,  QtWidgets
import sys




class Test():
    def __init__(self):
        self.ui = uic.loadUi('test.ui')
    def signalRegister(self):
        self.ui.pushButton.clicked.connect(self.handleClick)

    def handleClick(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def show(self):
        self.signalRegister()
        self.ui.show()
    





# app = QtWidgets.QApplication(sys.argv)
# main = Test()
# main.show()

# sys.exit(app.exec_())