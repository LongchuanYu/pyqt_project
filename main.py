from PyQt5 import uic,QtCore, QtGui, QtWidgets
import sys

class MainWindow():
    def __init__(self):
        self.ui = uic.loadUi('view.ui')
        self.widgets = []
    def setInit(self):
        self.ui.comboBox.addItem('test1')
        self.ui.comboBox.addItem('test2')
        # 在这里按照顺序添加页面objname
        self.widgets = [
            self.ui.widget,
            self.ui.widget_2
        ]
        self.handleCombobox(0)

    def modelsRegister(self):
        self.ui.comboBox.currentIndexChanged.connect(self.handleCombobox)
        self.ui.toolButton.clicked.connect(self.handleToolButton)


    def handleToolButton(self):
        dir_path=QtWidgets.QFileDialog.getExistingDirectory(None,"choose directory","/")
        self.ui.plainTextEdit.setPlainText(dir_path)
        
    def handleCombobox(self,index):
        if not self.widgets:
            return
        for i,w in enumerate(self.widgets):
            w.show() if i==index else w.hide()

    def show(self):
        self.setInit()
        self.modelsRegister()
        self.ui.show()

app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())