import sys
from PySide2.QtWidgets import *
from ui.ui_mainwindow import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(parent=None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication()
    # Create and show the form
    window = MainWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
