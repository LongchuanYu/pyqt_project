from PyQt5 import uic,  QtWidgets
import sys

class MainWindow():
    def __init__(self):
        self.ui = uic.loadUi('view.ui')
        self.widgets = []
    def setInit(self):
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        self.ui.comboBox.addItem('test1')
        self.ui.comboBox.addItem('test2')
        # 在这里按照顺序添加页面objname
        self.widgets = [
            self.ui.widget,
            self.ui.widget_2
        ]
        self.handleCombobox(0)

    def signalRegister(self):
        self.ui.comboBox.currentIndexChanged.connect(self.handleCombobox)
        self.ui.toolButton.clicked.connect(lambda : self.handleToolButton('original'))
        self.ui.toolButton_2.clicked.connect(lambda : self.handleToolButton('target'))
        self.ui.toolButton_3.clicked.connect(lambda : self.handleToolButton('file'))


    def handleToolButton(self,type='original'):
        select = {
            'original':self.ui.plainTextEdit,
            'target':self.ui.plainTextEdit_2,
            'file':self.ui.plainTextEdit_4
        }
        if not type in select:
            return
        obj = select[type]
        dir_path=QtWidgets.QFileDialog.getExistingDirectory(None,"choose directory","/")
        obj.setPlainText(dir_path)
        
    def handleCombobox(self,index):
        if not self.widgets:
            return
        for i,w in enumerate(self.widgets):
            w.show() if i==index else w.hide()

    def show(self):
        self.setInit()
        self.signalRegister()
        self.ui.show()

app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())