from PyQt4 import QtGui
import sys
import form3qt_edit

class Form3(QtGui.QMainWindow, form3qt.Ui_MainWindow):
	def __init__(self,parent =None):
		super(Form3, self).__init__(parent)
		self.setupUi(self)

def main():
	app = QtGui.QApplication(sys.argv)
	form = Form3()
	form.show()
	app.exec_()

if __name__ == '__main__':
    main()
