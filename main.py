import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from camera import *

# QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

class CWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.camera = camera(self, QSize(self.frm.width(), self.frm.height()))

    def initUI(self):
        size = QSize(600, 500)
        vbox = QVBoxLayout()

        # cam on, off button
        self.btn = QPushButton('start cam', self)
        self.btn.setCheckable(True)
        self.btn.clicked.connect(self.turnCam)
        vbox.addWidget(self.btn)

        """
        # kind of detection
        txt = ['full body', 'upper body', 'lower body', 'face', 'eye', 'eye glass', 'smile']
        self.grp = QButtonGroup(self)
        self.grp = QButtonGroup(self)
        for i in range(len(txt)):
            btn = QCheckBox(txt[i], self)
            self.grp.addButton(btn, i)
            vbox.addWidget(btn)
        vbox.addStretch(1)
        self.grp.setExclusive(False)
        self.grp.buttonClicked[int].connect(self.detectOption)
        self.bDetect = [False for i in range(len(txt))]
        """

        # video area
        self.frm = QLabel(self)
        self.frm.setFrameShape(QFrame.Panel)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addWidget(self.frm, 1)
        self.setLayout(hbox)

        self.setFixedSize(size)
        self.move(100, 100)
        self.setWindowTitle('OpenCV + PyQt5')
        self.show()

    def turnCam(self, e):
        if self.btn.isChecked():
            self.btn.setText('stop')
            self.camera.startCam()
        else:
            self.btn.setText('start')
            self.camera.stopCam()


    def recvImage(self, img):
        self.frm.setPixmap(QPixmap.fromImage(img))

    def closeEvent(self, e):
        self.camera.stopCam()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    sys.exit(app.exec_())