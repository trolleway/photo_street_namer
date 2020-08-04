# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets, QtGui
import os

import mainform

import photo_geo_processor

class Photogeocaption(QtWidgets.QMainWindow, mainform.Ui_MainWindow):
    ck = 0
    images_paths = list()
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.btnBrowse.clicked.connect(self.browse_folder)

        self.pushButton_1.clicked.connect(self.process_choise_1)
        self.pushButton_2.clicked.connect(self.process_choise_2)
        self.pushButton_3.clicked.connect(self.process_choise_3)
        self.pushButton_4.clicked.connect(self.process_choise_4)
        self.pushButton_5.clicked.connect(self.process_choise_5)
        self.pushButton_6.clicked.connect(self.process_choise_6)

        self.processor = photo_geo_processor.Photo_geo_processor()
        self.__current_image_key = 0
        self.images_count = 0
        self.images_paths = list()

        self.ck = 0

    #def set_current_image_key(self,value):
    #    self.__current_image_key = value
    #def get_current_image_key(self):
    #    return self.__current_image_key

    #current_img_key = property(get_current_image_key, set_current_image_key)

    def browse_folder(self):
        self.label.clear()  # На случай, если в списке уже есть элементы
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории
        self.images_paths = self.read_dir(directory)

        print(self.images_paths)

        self.read_image(0)

    def go_image(self, inc):
        self.read_image(self.ck + inc)

    def go_next_image(self):
        self.go_image(1)

    def process_choise_1(self):
        self.update_image(self.ck, 1)

    def process_choise_2(self):
        self.update_image(self.ck, 2)

    def process_choise_3(self):
        self.update_image(self.ck, 3)

    def process_choise_4(self):
        self.update_image(self.ck, 4)

    def process_choise_5(self):
        self.update_image(self.ck, 5)

    def process_choise_6(self):
        self.update_image(self.ck, 6)


    def update_image(self,ck,choise):
        filepath = self.images_paths[ck]
        to = self.texts[int(choise)]
        print('update image'+filepath+' with choise '+to)

        self.processor.rename_file(filepath, to)
        self.go_next_image()

    def read_image(self,key):
        print('key='+str(key)+' len='+str(len(self.images_paths)))
        if key >= len(self.images_paths):
            quit()
            return None

        self.label_imageview.setText(self.images_paths[key])
        self.ck = (key)

        filepath = self.images_paths[key]
        texts = self.processor.get_variants_list(filepath)
        print(texts)
        self.texts = texts

        self.pushButton_1.setText(texts[1])
        self.pushButton_2.setText(texts[2])
        self.pushButton_3.setText(texts[3])
        self.pushButton_4.setText(texts[4])
        self.pushButton_5.setText(texts[5])
        self.pushButton_6.setText(texts[6])

    def read_dir(self,directory):
        self.label_imageview.setScaledContents(True);

        images_paths = list()
        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            self.label.setText('<h2>'+directory+'</h2>')

            for root, sub_folders, files in os.walk(directory):
                images_paths += [os.path.join(root, filename) for filename in files if filename.lower().endswith(".jpg")]
            return images_paths



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Photogeocaption()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
        main()  # то запускаем функцию main()
