from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QPixmap
from PyQt5.QtCore import Qt, QRectF, QSizeF
from pyui.design_2 import Ui_MainWindow
from PIL import Image
import sys


class Drawing(QWidget):
    def __init__(self, color: QColor):
        super().__init__()

        self.filled_rectangles = []
        self.current_rectangle = None
        self.color = color
        self.color_to_save = color
        self.brush = QBrush(self.color)
        self.setMouseTracking(True)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.NoPen))
        for rectangle, color in self.filled_rectangles:
            self.brush.setColor(color)
            painter.fillRect(rectangle, self.brush)
            painter.drawRect(rectangle)
        self.brush.setColor(self.color_to_save)
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
                self.filled_rectangles.append([self.current_rectangle, self.brush.color()])
            self.current_rectangle = None
            self.update()

    def change_color(self, color: QColor):
        self.color = color
        self.color_to_save = color
        self.brush.setColor(self.color)

    def save_as_image(self, filename):
        pixmap = self.grab()
        pixmap.save(filename)


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.draw_objects = Drawing(QColor(0, 128, 0))
        self.draw_def = Drawing(QColor(0, 128, 0))
        self.gridLayout_4.addWidget(self.draw_objects)
        self.gridLayout_2.addWidget(self.draw_def)

        # self.pushButton_3.clicked.connect(lambda: self.draw_objects.save_as_image('photo_obj_1.png'))
        self.pushButton.clicked.connect(self.clear_objects)
        self.pushButton_2.clicked.connect(self.clear_defects)
        self.pushButton_30.clicked.connect(self.upload_photo)

        self.colorButton_3.clicked.connect(lambda: self.draw_objects.change_color(QColor(0, 128, 0)))
        self.colorButton_2.clicked.connect(lambda: self.draw_objects.change_color(QColor(0, 0, 255)))
        self.colorButton_1.clicked.connect(lambda: self.draw_objects.change_color(QColor(255, 255, 0)))
        self.colorButton_4.clicked.connect(lambda: self.draw_objects.change_color(QColor(0, 0, 0)))
        self.colorButton_5.clicked.connect(lambda: self.draw_objects.change_color(QColor(0, 255, 255)))
        self.colorButton_6.clicked.connect(lambda: self.draw_def.change_color(QColor(0, 128, 0)))
        self.colorButton_7.clicked.connect(lambda: self.draw_def.change_color(QColor(255, 0, 0)))

    def clear_objects(self):
        while self.gridLayout_4.count():
            child = self.gridLayout_4.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.draw_objects = Drawing(QColor(0, 128, 0))
        self.gridLayout_4.addWidget(self.draw_objects)

    def clear_defects(self):
        while self.gridLayout_2.count():
            child = self.gridLayout_2.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.draw_def = Drawing(QColor(0, 128, 0))
        self.gridLayout_2.addWidget(self.draw_def)

    def upload_photo(self):
        try:
            filename = QFileDialog.getOpenFileNames(self, "Выбрать изображение", "",
                                                    'Изображение (*.jpg *.png);')[0][0]
            image = Image.open(filename).resize((512, 64))
            image.save('image_start.png')
            self.canvas_8.setPixmap(QPixmap('image_start.png'))
        except Exception as E:
            pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
