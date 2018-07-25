from PyQt5 import QtWidgets
from demo import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

    def loadSingle(self):
        file_name, ok = QFileDialog.getOpenFileName(self, '读取', './')

    def loadAll(self):
        file_name, ok = QFileDialog.getOpenFileName(self, '读取', './')

    def loadROI(self):
        file_name, ok = QFileDialog.getOpenFileName(self, '读取', './')

    def loadCSV(self):
        file_name, ok = QFileDialog.getOpenFileName(self, '读取', './')

    def save(self):
        file_name, ok = QFileDialog.getSaveFileName(self, '读取', '/home')
        if ok:
            _f = open(file_name, 'w')
            _f.write(str(self.plainTextEdit.toPlainText()))

    def segment(self):
        return 0

    def calculate(self):
        return 0



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())