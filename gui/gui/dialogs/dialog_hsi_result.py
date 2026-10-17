from qt_core import *
from PIL.ImageQt import ImageQt
from algorithms.aux_functions import conversion_to_image

class HSIDialog(QDialog):

    def __init__(self, images_data, parent = None):
        QDialog.__init__(self, parent)
        self.setWindowTitle("Resultado da Conversão")
        self.setStyleSheet("background-color: #44475a; color: white; font: 10pt 'Segoe UI';")
        self.images = []

        layout = QHBoxLayout(self)

        for matrix, name in images_data:
            vbox = QVBoxLayout()

            # Title
            label_title = QLabel(name)
            label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label_title.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 10px;")
            vbox.addWidget(label_title)

            # Converting matrix to image
            pillow_image = conversion_to_image(matrix)
            qt_image = ImageQt(pillow_image)
            self.images.append(qt_image)

            # Image label
            label_image = QLabel()
            pixmap = QPixmap.fromImage(qt_image).scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            label_image.setPixmap(pixmap)
            label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
            vbox.addWidget(label_image)

            # Saving option
            save_button = QPushButton(f"Salvar image {name}")
            save_button.setCursor(Qt.CursorShape.PointingHandCursor)
            save_button.setStyleSheet("background-color: #6272a4; padding: 8px; border-radius: 5px;")

            save_button.clicked.connect(lambda checked = False, img = pillow_image, n = name: self.save_specific_image(img, n))
            vbox.addWidget(save_button)

            layout.addLayout(vbox)

    def save_specific_image(self, pillow_image, name):
        file_path, _ = QFileDialog.getSaveFileName(self, f"Salvar imagem {name}", f"{name}.png", "Imagens (*.png *.bmp *.jpg)")

        if (file_path):
            pillow_image.save(file_path)
            print(f"{name} Salva com sucesso!")