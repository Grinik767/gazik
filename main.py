from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QPixmap
from PyQt5.QtCore import Qt, QRectF, QSizeF, QEvent
from pyui.test_5 import Ui_MainWindow
from pyui.neuro_1 import Ui_MainWindow_n
from pyui.levels import Ui_MainWindow_l
from PIL import Image
from Unet import *
from Pspnet import *
from funcs import *
import sys
import os


class Drawing(QWidget):
    def __init__(self, color: QColor):
        super().__init__()

        self.current_rectangle = None
        self.have_copy = None

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
        if self.have_copy:
            self.filled_rectangles.append([self.have_copy, self.brush.color()])
            self.have_copy = None
        for rectangle, color in self.filled_rectangles:
            self.brush.setColor(color)
            if rectangle.__class__.__name__ == 'QPixmap':
                painter.drawPixmap(0, 0, rectangle)
            else:
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

    def paste_image(self, filename):
        self.have_copy = QPixmap(filename)


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.have_photo = None
        self.have_pr = None
        self.type_of_f = ''

        self.draw_objects = Drawing(QColor(0, 128, 0))
        self.draw_def = Drawing(QColor(0, 128, 0))
        self.draw_objects_pr = Drawing(QColor(0, 128, 0))
        self.draw_def_pr = Drawing(QColor(0, 128, 0))

        self.pushButton_3.clicked.connect(self.save_images)
        self.pushButton.clicked.connect(self.clear_objects)
        self.pushButton_2.clicked.connect(self.clear_defects)
        self.pushButton_8.clicked.connect(self.clear_objects_pr)
        self.pushButton_9.clicked.connect(self.clear_defects_pr)
        self.pushButton_30.clicked.connect(self.upload_photo)
        self.pushButton_31.clicked.connect(self.choose_task)
        self.pushButton_4.clicked.connect(self.get_from_neuro)
        self.pushButton_11.clicked.connect(self.get_from_neuro_pr)

        self.colorButton_3.clicked.connect(lambda: self.draw_objects.change_color(QColor(0, 128, 0)))
        self.colorButton_2.clicked.connect(lambda: self.draw_objects.change_color(QColor(0, 0, 255)))
        self.colorButton_1.clicked.connect(lambda: self.draw_objects.change_color(QColor(255, 255, 0)))
        self.colorButton_4.clicked.connect(lambda: self.draw_objects.change_color(QColor(0, 0, 0)))
        self.colorButton_5.clicked.connect(lambda: self.draw_objects.change_color(QColor(0, 255, 255)))
        self.colorButton_6.clicked.connect(lambda: self.draw_def.change_color(QColor(0, 128, 0)))
        self.colorButton_7.clicked.connect(lambda: self.draw_def.change_color(QColor(255, 0, 0)))
        self.colorButton_8.clicked.connect(lambda: self.draw_objects_pr.change_color(QColor(0, 128, 0)))
        self.colorButton_9.clicked.connect(lambda: self.draw_objects_pr.change_color(QColor(0, 0, 255)))
        self.colorButton_10.clicked.connect(lambda: self.draw_objects_pr.change_color(QColor(255, 255, 0)))
        self.colorButton_11.clicked.connect(lambda: self.draw_objects_pr.change_color(QColor(0, 0, 0)))
        self.colorButton_12.clicked.connect(lambda: self.draw_objects_pr.change_color(QColor(0, 255, 255)))
        self.colorButton_13.clicked.connect(lambda: self.draw_def_pr.change_color(QColor(0, 128, 0)))
        self.colorButton_14.clicked.connect(lambda: self.draw_def_pr.change_color(QColor(255, 0, 0)))

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

    def clear_objects_pr(self):
        if self.have_pr:
            while self.gridLayout_8.count():
                child = self.gridLayout_8.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.draw_objects_pr = Drawing(QColor(0, 128, 0))
            self.gridLayout_8.addWidget(self.draw_objects_pr)

    def clear_defects_pr(self):
        if self.have_pr:
            while self.gridLayout_3.count():
                child = self.gridLayout_3.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.draw_def_pr = Drawing(QColor(0, 128, 0))
            self.gridLayout_3.addWidget(self.draw_def_pr)

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

    def choose_task(self):
        self.levels = Levels()
        self.levels.show()

    def apply_task(self, level: int):
        try:
            image = Image.open(f'tasks/{level}/photo.jpg').resize((1024, 64))
            image.save('image_start_pr.png')
            self.have_pr = level
            self.gridLayout_8.addWidget(self.draw_objects_pr)
            self.gridLayout_3.addWidget(self.draw_def_pr)
            self.canvas_6.setPixmap(QPixmap('image_start_pr.png'))
        except Exception as E:
            pass

    def save_images(self):
        if self.have_photo:
            try:
                filename = \
                    QFileDialog.getSaveFileName(self, "Сохранить изображения", '',
                                                'Изображение (*.png);;Изображение (*.jpg);')[
                        0]
                self.type_of_f = filename.split('/')[-1].split('.')[-1]
                self.draw_objects.save_as_image(f'objects_1.{self.type_of_f}')
                self.draw_def.save_as_image(f'defects_1.{self.type_of_f}')
                image_obj = Image.open(f'objects_1.{self.type_of_f}')
                image_def = Image.open(f'defects_1.{self.type_of_f}')
                image_start = Image.open(f'image_start.png')
                image_object_size = image_obj.size
                new_image = Image.new('RGB', (image_object_size[0], 3 * image_object_size[1] + 3), (255, 255, 255))
                new_image.paste(image_start, (0, 0))
                new_image.paste(image_obj, (0, image_object_size[1] + 1))
                new_image.paste(image_def, (0, 2 * image_object_size[1] + 2))
                new_image.save(filename)
                new_image.show()
            except Exception as e:
                pass

    def get_from_neuro(self):
        if self.have_photo:
            img = image.load_img('image_start.png', target_size=(img_height // 8, img_width // 8))
            self.adm = Neuro(img)
            self.adm.show()

    def get_from_neuro_pr(self):
        if self.have_pr:
            img = image.load_img('image_start_pr.png', target_size=(img_height // 8, img_width // 8))
            self.adm = Neuro(img, pr=True)
            self.adm.show()

    def paste_objects(self, pr: bool):
        if pr:
            self.draw_objects_pr.paste_image('image_neuro_obj_pr.png')
        else:
            self.draw_objects.paste_image('image_neuro_obj.png')

    def paste_defects(self, pr: bool):
        if pr:
            self.draw_def_pr.paste_image('image_neuro_def_pr.png')
        else:
            self.draw_def.paste_image('image_neuro_def.png')

    def closeEvent(self, event):
        if self.have_photo:
            os.remove('image_start.png')
        if self.have_pr:
            os.remove('image_start_pr.png')
        if self.type_of_f:
            os.remove(f'objects_1.{self.type_of_f}')
            os.remove(f'defects_1.{self.type_of_f}')


class Neuro(QMainWindow, Ui_MainWindow_n):
    def __init__(self, img, pr=False):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(self.copy_objects)
        self.pushButton_5.clicked.connect(self.copy_defects)

        self.pr = pr
        self.img = img
        self.get_result()

    def get_result(self, to_view=True):
        modelUnet = unet(num_classes, (img_height // 8, img_width // 8, 3))
        modelUnet.load_weights('Model_UNET_elem.h5')
        modelPsPnet = pspnet(num_classes_def, (img_height // 8, img_width // 8, 3))
        modelPsPnet.load_weights('Model_PSPNET_def.h5')

        x = image.img_to_array(self.img)

        predict_obj = np.array(modelUnet.predict(x.reshape(1, img_height // 8, img_width // 8, 3)))[0].reshape(-1,
                                                                                                               num_classes)
        predict_def = np.array(modelPsPnet.predict(x.reshape(1, img_height // 8, img_width // 8, 3)))[0].reshape(-1,
                                                                                                                 num_classes_def)
        if to_view:
            pr1 = []
            pr2 = []
            for k in range(len(predict_obj)):
                pr1.append(index2color(predict_obj[k]))
                pr2.append(index2color_def(predict_def[k]))
            self.view_result(pr1, objects=True)
            self.view_result(pr2, objects=False)
        else:
            return predict_obj, predict_def

    def view_result(self, result: list, objects: bool):
        result = np.array(result).reshape(img_height // 8, img_width // 8, 3)
        res = Image.fromarray(result.astype('uint8')).resize((1024, 64))
        if objects:
            if self.pr:
                res.save('image_neuro_obj_pr.png')
                self.canvas_7.setPixmap(QPixmap('image_neuro_obj_pr.png'))
            else:
                res.save('image_neuro_obj.png')
                self.canvas_7.setPixmap(QPixmap('image_neuro_obj.png'))
        else:
            if self.pr:
                res.save('image_neuro_def_pr.png')
                self.canvas_8.setPixmap(QPixmap('image_neuro_def_pr.png'))
            else:
                res.save('image_neuro_def.png')
                self.canvas_8.setPixmap(QPixmap('image_neuro_def.png'))

    def copy_objects(self):
        ex.paste_objects(self.pr)

    def copy_defects(self):
        ex.paste_defects(self.pr)

    def count_overlap(self):
        '''objects, defects = self.get_result(to_view=False)
        objects1 = []
        defects1 = []
        for k in range(len(objects)):
            objects1.append(np.argmax(objects[k]))
            defects1.append(np.argmax(defects[k]))
        objects, defects = np.array(objects1).reshape(img_height // 8, img_width // 8), np.array(defects1).reshape(
            img_height // 8, img_width // 8)
        ex.draw_objects.save_as_image('objects_1.png')
        img_obj = yt_prep([Image.open('objects_1.png').convert('RGB').resize((1024, 64))], num_classes).reshape(-1,
                                                                                                                num_classes)
        res1_1 = []
        res2_1 = []
        for i in range(len(img_obj)):
            res1_1.append(np.argmax(img_obj[i]))
        res1_1 = np.array(res1_1)
        res1_1 = res1_1.reshape(img_height // 2, img_width // 4)
        res1 = []
        res2 = []
        for i in range(img_width // 8):
            res1 += ([np.argmax(np.bincount(objects[:, i]))] * 8)
            res2 += ([np.argmax(np.bincount(defects[:, i]))] * 8)
        res1_2 = []
        for i in range(img_width // 4):
            res1_2 += ([np.argmax(np.bincount(res1_1[:, i]))] * 4)
        k_def = 0
        for i in range(img_width):
            if res1[i] == res1_2[i]:
                k_def += 1
        print(k_def / 4096 * 100)'''

    def event(self, event):
        if event.type() == QEvent.WindowActivate:
            pass
        elif event.type() == QEvent.Close:
            if self.pr:
                os.remove('image_neuro_obj_pr.png')
                os.remove('image_neuro_def_pr.png')
            else:
                os.remove('image_neuro_obj.png')
                os.remove('image_neuro_def.png')
        return QMainWindow.event(self, event)


class Levels(QMainWindow, Ui_MainWindow_l):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: self.choose_level(1))
        self.pushButton_2.clicked.connect(lambda: self.choose_level(2))
        self.pushButton_3.clicked.connect(lambda: self.choose_level(3))
        self.pushButton_4.clicked.connect(lambda: self.choose_level(4))
        self.pushButton_5.clicked.connect(lambda: self.choose_level(5))

    def choose_level(self, level: int):
        ex.apply_task(level)
        self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
