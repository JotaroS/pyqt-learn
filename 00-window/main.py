import sys
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton


class App (QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Empty Window")
        self.setGeometry(100,100,200,200)
        button = QPushButton("a button", self)
        button.setGeometry(25,25,100,20)
        button.clicked.connect(self.buttonEvent)

    def buttonEvent(self):
        print('button is pressed')


qApp = QApplication(sys.argv)
app = App()
app.show();
qApp.exec()