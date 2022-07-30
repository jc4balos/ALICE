import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon


class Home(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):



        self.setFixedWidth(720)
        self.setFixedHeight(576)
        self.center()

        self.setWindowTitle('ALICE: Autonomous Light Integrated Commandable Entity')
        self.setWindowIcon(QIcon('./assets/icons/alice.ico'))
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():

    app = QApplication(sys.argv)
    ex = Home()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()