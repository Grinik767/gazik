from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QPixmap
from PyQt5.QtCore import Qt, QRectF, QSizeF
from pyui.test_4 import Ui_MainWindow
from PIL import Image
import sys
import os


class Drawing(QWidget):
    def __init__(self, color: QColor):
        super().__init__()

        self.current_rectangle = None

        self.color = color
        self.color_to_save = color
        self.brush = QBrush(self.color)
        self.filled_rectangles = [
            [QRectF(self.pos(), QSizeF(self.x() + 1025, self.y() + 65)), self.brush.color()]]
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

        self.have_photo = None

        self.draw_objects = Drawing(QColor(0, 128, 0))
        self.draw_def = Drawing(QColor(0, 128, 0))

        self.pushButton_3.clicked.connect(self.save_images)
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
        if self.have_photo:
            while self.gridLayout_4.count():
                child = self.gridLayout_4.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.draw_objects = Drawing(QColor(0, 128, 0))
            self.gridLayout_4.addWidget(self.draw_objects)

    def clear_defects(self):
        if self.have_photo:
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
            image = Image.open(filename).resize((1024, 64))
            image.save('image_start.png')
            self.have_photo = True
            self.gridLayout_4.addWidget(self.draw_objects)
            self.gridLayout_2.addWidget(self.draw_def)
            self.canvas_8.setPixmap(QPixmap('image_start.png'))
        except Exception as E:
            pass

    def save_images(self):
        if self.have_photo:
            try:
                filename = \
                    QFileDialog.getSaveFileName(self, "Сохранить изображения", '',
                                                'Изображение (*.png);;Изображение (*.jpg);')[
                        0]
                type_of_f = filename.split('/')[-1].split('.')[-1]
                self.draw_objects.save_as_image(f'objects_1.{type_of_f}')
                self.draw_def.save_as_image(f'defects_1.{type_of_f}')
                image_obj = Image.open(f'objects_1.{type_of_f}')
                image_def = Image.open(f'defects_1.{type_of_f}')
                image_start = Image.open(f'image_start.png')
                image_object_size = image_obj.size
                new_image = Image.new('RGB', (image_object_size[0], 3 * image_object_size[1] + 3), (255, 255, 255))
                new_image.paste(image_start, (0, 0))
                new_image.paste(image_obj, (0, image_object_size[1] + 1))
                new_image.paste(image_def, (0, 2 * image_object_size[1] + 2))
                new_image.save(filename)
                new_image.show()
                os.remove(f'objects_1.{type_of_f}')
                os.remove(f'defects_1.{type_of_f}')
                os.remove('image_start.png')
            except Exception as e:
                pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
