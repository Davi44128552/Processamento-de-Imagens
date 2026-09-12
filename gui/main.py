# Importing modules
import sys
import os
import ctypes
from qt_core import *
from gui.windows.main_win.ui_main_window import *
from PIL.ImageQt import ImageQt

# Import the algorithms files
directory = os.path.dirname(os.path.abspath(__file__))
directory = os.path.abspath(os.path.join(directory, ".."))
sys.path.append(directory)
from algorithms.intensity_transformations import *
from algorithms.aux_functions import *

# Main window class
class MainWindow(QMainWindow):
    def __init__(self):

        # Creating the class and showing de window
        super().__init__()

        # Adding a title to the application
        self.setWindowTitle("CalopImage")

        # Taking the icon and setting in the application
        directory = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(directory, "images", "calopsita_appimage.png")
        
        # Creating the application icon
        self.setWindowIcon(QIcon(icon_path))

        # Setting the main window
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Toggle button action
        self.ui.toggle_button.clicked.connect(lambda: self.toggle_button(self.ui.left_menu))

        # Calling the function to apply the transformation
        self.ui.toggle2_button.clicked.connect(lambda: self.toggle_button(self.ui.transformation_menu))
        self.ui.button_thresholding.clicked.connect(self.open_thresholding)
        self.ui.button_negative.clicked.connect(self.open_negative)
        self.ui.button_brightness.clicked.connect(self.open_brightness)
        self.ui.button_logarithm_transformation.clicked.connect(self.open_logarithm)
        self.ui.button_power_law.clicked.connect(self.open_power_law)
        self.ui.button_contrast_stretching.clicked.connect(self.open_contrast_stretching)
        self.ui.button_intensity_level_slicing.clicked.connect(self.open_intensity_level_slicing)
        self.ui.button_bit_plane_slicing.clicked.connect(self.open_bit_plane_slicing)
        self.ui.button_steganography_apply.clicked.connect(self.open_steganography_apply)
        self.ui.button_steganography_undo.clicked.connect(self.open_steganography_decode)
        self.ui.transformation_download_button.clicked.connect(self.save_image)
        self.ui.button_transformation_go_back.clicked.connect(self.go_back)

        # Showing the GUI
        self.show()

        # Adding the behavior to the button
        self.ui.toggle_button2.clicked.connect(self.open_image)
        self.ui.toggle_button3.clicked.connect(self.random_image_select)
        self.ui.config_button.clicked.connect(self.help)
        self.ui.select_part_window_ui.pushButton.clicked.connect(self.ui.select_part_window.accept)

        self.button_list = [self.ui.button_thresholding, self.ui.button_negative, self.ui.button_brightness, self.ui.button_logarithm_transformation, self.ui.button_power_law,
                                       self.ui.button_contrast_stretching, self.ui.button_intensity_level_slicing, self.ui.button_bit_plane_slicing,
                                       self.ui.button_steganography_apply, self.ui.button_steganography_undo, self.ui.config_button, self.ui.toggle_button, self.ui.toggle_button2, 
                                       self.ui.toggle_button3]

        # Some config buttons behavior
    def help(self):
        self.ui.toggle_button2.set_active(False)
        self.ui.toggle_button3.set_active(False)
        self.ui.config_button.set_active(True)

    def go_back(self):
        # Removing the transformations menu
        self.ui.main_layout.removeWidget(self.ui.transformation_menu)
        self.ui.transformation_menu.hide()

        # Adding the left menu layout
        self.ui.main_layout.insertWidget(0, self.ui.left_menu)
        self.ui.left_menu.show()

        # Returning to main window
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page1)

    # Adding a action to toggle button
    def toggle_button(self, menu):

        # Configing
        menu_width = menu.width()
        width = 50
        if (menu_width == 50):
            width = 250

        self.animation = QPropertyAnimation(menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    # Adding the button function to open a image
    def open_image(self):

        self.active_button(self.ui.toggle_button2)

        # Opening file selector
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione a imagem", "", "Imagens (*.png *.jpg *.jpeg *.bmp)")
        if (file_path):

            # Reading the image
            load_image = QImage(file_path)

            # Converting to grayscale
            load_image = load_image.convertToFormat(QImage.Format.Format_Grayscale8)
            load_image = QPixmap.fromImage(load_image)

            # Applying scale
            load_image = load_image.scaled(700, 700, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

            # Changing the label and showing the image to the user
            self.ui.ui_pages.label_2.setPixmap(load_image)
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.page2)

            self.select_algorithms(file_path)

    # Adding the button function to take a random image
    def random_image_select(self):

        self.active_button(self.ui.toggle_button3)
                
        # Opening file selector
        directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(directory, "..", "test_images", "calopsita.jpg")
        image_path = os.path.normpath(image_path)
        if (image_path):

            # Reading the image
            random_image = QPixmap(image_path)
            random_image = random_image.scaled(700, 700, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

            # Changing the label and showing the image to the user
            self.ui.ui_pages.label.setPixmap(random_image)
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.page3)

            # Going to transformation function
    # Function to save the images
    def save_image(self):

        # Defining the path
        file_path,_ = QFileDialog.getSaveFileName(self, "Salve a imagem", "", "Imagens (*.png *.bmp)")

        # Verifying path
        if (file_path):
            self.final_image.save(file_path)

    # Function to apply the intensity_transformations
    def transformation(self, img_path):

        # Adding the transformations menu
        self.ui.main_layout.removeWidget(self.ui.left_menu)
        self.ui.left_menu.hide()
        self.ui.main_layout.insertWidget(0, self.ui.transformation_menu)
        self.ui.transformation_menu.show()

        # Reading the image
        self.matrix = conversion_to_matrix(img_path)
        self.final_image = conversion_to_image(self.matrix)

    def active_button(self, selected_button):

        for button in self.button_list:
            if (button == selected_button):
                button.set_active(True)
            else:
                button.set_active(False)

    # Window to choose the algorithms type
    def select_algorithms(self, file_path):

        if (self.ui.select_part_window.exec()):

            # Checking which radiobutton was selected
            if (self.ui.select_part_window_ui.radioButton.isChecked()):

                # Going to intensity transformations "window"
                self.transformation(file_path)

            elif (self.ui.select_part_window_ui.radioButton_2.isChecked()):
                print("2")

            elif (self.ui.select_part_window_ui.radioButton_3.isChecked()):
                print("3")

    # applying the transformations
    # thresholding
    def open_thresholding(self):

        self.active_button(self.ui.button_thresholding)

        # Executing the thresholding dialog
        if (self.ui.thresholding_window.exec()):

            # Taking the value
            T = self.ui.thresholding_window_ui.lineEdit.text()

            try:
                T = int(T)
                converted_matrix = thresholding(self.matrix, T)
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("O valor deve ser inteiro")
                return

    # Negative
    def open_negative(self):

        self.active_button(self.ui.button_negative)

        # Executing the negative dialog
        if (self.ui.negative_window.exec()):

            # Taking the value
            L = self.ui.negative_window_ui.lineEdit.text()
            
            try:
                L = float(L)
                converted_matrix = negative(self.matrix, L)
                self.apply_transformation(converted_matrix)
            except ValueError:
                if (L.strip() != ""):
                    print("O valor deve ser um número")
                    return
                converted_matrix = negative(self.matrix)
                self.apply_transformation(converted_matrix)

    # Brightness
    def open_brightness(self):

        self.active_button(self.ui.button_brightness)

        # Executing the brightness window
        if (self.ui.brightness_window.exec()):

            # Taking the value
            k = self.ui.brightness_window_ui.lineEdit.text()

            try:
                k = float(k)
                converted_matrix = brightness(self.matrix, k)
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("O valor deve ser um número!")
                return 

    # Logarithm
    def open_logarithm(self):

        self.active_button(self.ui.button_logarithm_transformation)

        # Executing the logarith dialog
        if (self.ui.logarithm_transformation_window.exec()):

            # Taking the value
            c = self.ui.logarithm_transformation_window_ui.lineEdit.text()

            try:
                c = float(c)
                converted_matrix = negative(self.matrix, c)
                self.apply_transformation(converted_matrix)
            except ValueError:
                if (c.strip() != ""):
                    print("O valor deve ser um número")
                    return
                converted_matrix = logarithm_transformation(self.matrix)
                self.apply_transformation(converted_matrix)

    # Power law
    def open_power_law(self):

        self.active_button(self.ui.button_power_law)

        # Executing the power law dialog
        if (self.ui.power_law_window.exec()):

            # Taking the value of gamma
            gamma = self.ui.power_law_window_ui.lineEdit.text()

            try:
                gamma = float(gamma)
                converted_matrix = power_law_transformation(self.matrix, gamma)
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("O valor deve ser float")
                return

    # Contrast stretching
    def open_contrast_stretching(self):

        self.active_button(self.ui.button_contrast_stretching)

        # Executing the algorithm
        converted_matrix = contrast_stretching(self.matrix)
        self.apply_transformation(converted_matrix)

    # Intensity level slicing
    def open_intensity_level_slicing(self):

        self.active_button(self.ui.button_intensity_level_slicing)

        if (self.ui.intensity_level_slicing_window.exec()):

            min_value = self.ui.intensity_level_slicing_window_ui.lineEdit.text()
            max_value = self.ui.intensity_level_slicing_window_ui.lineEdit_3.text()
            algorithm = self.ui.intensity_level_slicing_window_ui.lineEdit_2.text().strip().lower()

            try:
                min_value = int(min_value)
                max_value = int(max_value)
                converted_matrix = intensity_level_slicing(self.matrix, min_value, max_value, algorithm)
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("Os valores mínimo e máximo devem ser inteiros!")
                return

    # Bit plane slicing
    def open_bit_plane_slicing(self):

        self.active_button(self.ui.button_bit_plane_slicing)

        # Excecuting the bit plane window
        if (self.ui.bit_plane_slicing_window.exec()):

            bit_reference = self.ui.bit_plane_slicing_window_ui.lineEdit.text()

            try:
                bit_reference = int(bit_reference)
                converted_matrix = bit_plane_slicing(self.matrix, bit_reference)
                self.apply_transformation(converted_matrix)
            except ValueError:
                print("O valor deve ser inteiro")
                return

    # Steganography
    def open_steganography_apply(self):

        self.active_button(self.ui.button_steganography_apply)

        # Executing the steganography window
        if (self.ui.steganopgraphy_apply_window.exec()):
            message = self.ui.steganopgraphy_apply_window_ui.lineEdit.text()
            converted_matrix = steganography_apply(self.matrix, message)
            self.apply_transformation(converted_matrix)

    def open_steganography_decode(self):

        self.active_button(self.ui.button_steganography_undo)

        # Executing the steganography window
        message = steganography_decoder(self.matrix)
        self.ui.steganography_decode_window_ui.retranslateUi(self.ui.steganography_decode_window, message)
        self.ui.steganography_decode_window.exec()

    def apply_transformation(self, converted_matrix: np.ndarray = None):
        self.final_image = conversion_to_image(converted_matrix)
        self.final_image = ImageQt(self.final_image)
        self.final_image = QPixmap.fromImage(self.final_image)
        self.final_image_show = self.final_image.scaled(700, 700, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.ui.ui_pages.label_2.setPixmap(self.final_image_show)
        
# main
def main():
    myappid = 'davi.calopimage.app.1' 
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except Exception as e:
        print(f"{e}")

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()