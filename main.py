from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
from random import randint


class Prog(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.diams = []
        self.colors = []
        self.is_draw = False
        self.button_after_clicking_on_which_random_diameter_circles_of_yellow_color_shold_be_appear_on_the_form.\
            clicked.connect(self.appear)

    def paintEvent(self, event):
        if self.is_draw:
            draw = QPainter()
            draw.begin(self)
            for i in range(2):
                for j in range(2):
                    draw.setBrush(self.colors[i * 2 + j])
                    draw.drawEllipse(110 + i * 200 - self.diams[i * 2 + j] // 2, 150 + j * 200 -
                                     self.diams[i * 2 + j] // 2, self.diams[i * 2 + j], self.diams[i * 2 + j])
            draw.end()

    def appear(self):
        self.diams.clear()
        self.diams = [randint(1, 200), randint(1, 200), randint(1, 200), randint(1, 200)]
        self.colors = [QColor(randint(0, 255), randint(0, 255), randint(0, 255)),
                       QColor(randint(0, 255), randint(0, 255), randint(0, 255)),
                       QColor(randint(0, 255), randint(0, 255), randint(0, 255)),
                       QColor(randint(0, 255), randint(0, 255), randint(0, 255))]
        self.is_draw = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Prog()
    prog.show()
    sys.exit(app.exec_())
