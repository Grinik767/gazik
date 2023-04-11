from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QRectF, QSizeF
from pyui.design_2 import Ui_MainWindow
import sys


class Drawing(QWidget):
    def __init__(self, color):
        super().__init__()

        self.filled_rectangles = []
        self.current_rectangle = None
        self.color = color
        self.brush = QBrush(Qt.green)
        self.setMouseTracking(True)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.NoPen))

        for rectangle in self.filled_rectangles:
            painter.fillRect(rectangle, self.brush)
            painter.drawRect(rectangle)

        if self.current_rectangle is not None:
            painter.fillRect(self.current_rectangle, self.brush)
            painter.drawRect(self.current_rectangle)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.current_rectangle = QRectF(event.pos(), QSizeF())
            self.update()

    def mouseMoveEvent(self, event):
        if self.current_rectangle is not None:
            s = event.pos() - self.current_rectangle.topLeft()
            size = QSizeF(s.x(), s.y())
            self.current_rectangle.setSize(size)
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if abs(self.current_rectangle.width()) > 0 and abs(self.current_rectangle.height()) > 0:
                self.filled_rectangles.append(self.current_rectangle)
            self.current_rectangle = None
            self.update()

    def save_as_image(self, filename):
        pixmap = self.grab()
        pixmap.save(filename)


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.draw_objects = Drawing('1')
        self.draw_def = Drawing('1')
        self.gridLayout_4.addWidget(self.draw_objects)
        self.gridLayout_2.addWidget(self.draw_def)

        self.pushButton_3.clicked.connect(lambda: self.draw_objects.save_as_image('photo.png'))
        self.pushButton.clicked.connect(self.clear_objects)

    def clear_objects(self):
        while self.gridLayout_4.count():
            child = self.gridLayout_4.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.draw_objects = Drawing('1')
        self.gridLayout_4.addWidget(self.draw_objects)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
