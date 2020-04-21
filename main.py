from PyQt5 import uic,  QtWidgets
from PyQt5.QtCore import Qt
from search_file import Search
import sys

# class Base():
#     def error(self,msg=[]):
#         if not len(msg):return
#         for m in msg:




class MainWindow():
    def __init__(self):
        self.ui = uic.loadUi('view.ui')
        self.ci = None
    def setInit(self):
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        self.ui.comboBox.addItem('test1')
        self.ui.comboBox.addItem('test2')


    def signalRegister(self):
        self.ui.comboBox.currentIndexChanged.connect(self.handleCombobox)
        self.ui.toolButton.clicked.connect(lambda : self.handleToolButton('original'))
        self.ui.toolButton_2.clicked.connect(lambda : self.handleToolButton('target'))
        self.ui.toolButton_3.clicked.connect(self.doCustomInput)
        self.ui.pushButton.clicked.connect(self.handlePushButton)


    def handlePushButton(self):
        ori = self.ui.lineEdit.text()
        tar = self.ui.lineEdit_2.text()
        text = self.ui.lineEdit_3.text()
        err = []
        if not len(ori):
            err.append('原地址未选择')
        if not len(tar):
            err.append('目的地址未选择')
        if not text:
            err.append('自定义输入空...')
        if len(err):
            for e in err:
                self.ui.plainTextEdit_3.appendPlainText(e)
            return

        searchWhat = text.split('\n')
        s = Search()
        s.searchNames()



    def doCustomInput(self):
        self.ci = CustomInput(parent=self)
        self.ci.show()
    def handleToolButton(self,type='original'):
        select = {
            'original':self.ui.lineEdit,
            'target':self.ui.lineEdit_2,
            'file':self.ui.lineEdit_3
        }
        if not type in select:
            return
        obj = select[type]
        dir_path=QtWidgets.QFileDialog.getExistingDirectory(None,"choose directory","/")
        obj.setText(dir_path)
        
    def handleCombobox(self,index):
        page_count = self.ui.stackedWidget.count()
        if index>=page_count:
            print('index error')
            return
        self.ui.stackedWidget.setCurrentIndex(index)
        

    def show(self):
        self.setInit()
        self.signalRegister()
        self.ui.show()



class CustomInput(MainWindow):
    def __init__(self,parent=None):
        # super(CustomInput,self).__init__()
        self.parent = parent.ui
        self.ci = uic.loadUi('custom_input.ui')
        self.ci.setWindowModality(Qt.ApplicationModal)



    def setInit(self):
        text = self.parent.lineEdit_3.text()
        if text and len(text):
            self.ci.plainTextEdit.setPlainText(text)
    def signalRegister(self):
        self.ci.pushButton.clicked.connect(self.closeit)



    def closeit(self):
        text = self.ci.plainTextEdit.toPlainText()
        if not text:
            self.parent.plainTextEdit_3.appendPlainText('输入为空，什么都没发生...')
            self.ci.close()
            return
        print(text)
        self.parent.lineEdit_3.setText(text)
        self.ci.close()
    
    def show(self):
        self.setInit()
        self.signalRegister()
        self.ci.show()
        
app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())