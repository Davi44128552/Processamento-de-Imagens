# Importing os
import os

# Importing modules
from qt_core import *

# Importing pages
from gui.pages.ui_pages import Ui_StackedWidget

# Importing widgets
from gui.widgets.py_push_button import PyPushButton

# Importing dialogs
import gui.dialogs.dialog_one_input as one_input
import gui.dialogs.message_dialog as response
import gui.dialogs.dialog_three_input as three_input
import gui.dialogs.message_dialog as message_dialog
import gui.dialogs.dialog_method_select as dialog_method_select

# Path to select images
app_path = os.path.abspath(os.getcwd())
folder = "gui/images/"
path = os.path.join(app_path, folder)

# Main window
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # Setting the initial parameters
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        # Creating central widget
        self.central_frame = QFrame()

        # Creating and cofiguring the main layout
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Creating and cofiguring the extra frames
        # Left menu
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # Left menu layout
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # Top Frame menu
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(40)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")

        # Top frame layout
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        # Top bottoms
        self.toggle_button = PyPushButton(text = "Menu", icon_path = "icon_menu.svg")
        self.toggle_button2 = PyPushButton(text = "Abrir Imagem", icon_path = "folder.svg")
        self.toggle_button3 = PyPushButton(text = "Pegar Imagem Aleatória", icon_path = "random.svg")

        # Add buttons
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.toggle_button2)
        self.left_menu_top_layout.addWidget(self.toggle_button3)

        # Menu spacer
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Bottom frame menu
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(40)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")

        # Bottom frame layout
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        # bottom button
        self.config_button = PyPushButton(text = "Ajuda", icon_path = "qmark.svg")

        # Add buttons
        self.left_menu_bottom_layout.addWidget(self.config_button)

        # Label version
        self.left_menu_version = QLabel("v1.1.0")
        self.left_menu_version.setAlignment(Qt.AlignCenter)
        self.left_menu_version.setMaximumHeight(30)
        self.left_menu_version.setMinimumHeight(30)
        self.left_menu_version.setStyleSheet("color: #c3ccdf")

        # Add to layout
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_version)

        # Adding the histogram equalization frame
        self.equalization_hist_menu = QFrame()
        self.equalization_hist_menu.setStyleSheet("background-color: #44475a")
        self.equalization_hist_menu.setMaximumWidth(50)
        self.equalization_hist_menu.setMinimumWidth(50)

        # Left menu layout
        self.equalization_hist_menu_layout = QVBoxLayout(self.equalization_hist_menu)
        self.equalization_hist_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.equalization_hist_menu_layout.setSpacing(0)

        # Adding the transformations frame
        self.transformation_menu = QFrame()
        self.transformation_menu.setStyleSheet("background-color: #44475a")
        self.transformation_menu.setMaximumWidth(50)
        self.transformation_menu.setMinimumWidth(50)

        # Left menu layout
        self.transformation_menu_layout = QVBoxLayout(self.transformation_menu)
        self.transformation_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.transformation_menu_layout.setSpacing(0)

        # Configuring the buttons
        self.toggle2_button = PyPushButton(text = "Menu", icon_path = "icon_menu.svg")
        self.toggle_histogram_button = PyPushButton(text = "Menu", icon_path = "icon_menu.svg")
        self.button_thresholding = PyPushButton(text = "Linearização", icon_path = "icon1.svg")
        self.button_negative = PyPushButton(text = "Negativa", icon_path = "icon2.svg")
        self.button_brightness = PyPushButton(text = "Brilho", icon_path = "icon10.svg")
        self.button_logarithm_transformation = PyPushButton(text = "Transformação Logarítmica", icon_path = "icon3.svg")
        self.button_power_law = PyPushButton(text = "Transformação gamma", icon_path = "icon4.svg")
        self.button_contrast_stretching = PyPushButton(text = "Alongamento de contraste", icon_path = "icon5.svg")
        self.button_intensity_level_slicing = PyPushButton(text = "Fatiamento por intensidade", icon_path = "icon7.svg")
        self.button_bit_plane_slicing = PyPushButton(text = "Fatiamento por planos de bits", icon_path = "icon6.svg")
        self.button_steganography_apply = PyPushButton(text = "Aplicar Esteganografia", icon_path = "icon8.svg")
        self.button_steganography_undo = PyPushButton(text = "Decodificar Esteganografia", icon_path = "icon9.svg")
        self.transformation_download_button = PyPushButton(text = "Baixar Imagem", icon_path = "download.svg")        
        self.histogram_download_button = PyPushButton(text = "Baixar Imagem", icon_path = "download.svg")        
        self.button_transformation_go_back = PyPushButton(text = "Voltar", icon_path = "arrow.svg")
        self.button_histogram_go_back = PyPushButton(text = "Voltar", icon_path = "arrow.svg")

        # Adding the buttons to layout
        self.equalization_hist_menu_layout.addWidget(self.toggle_histogram_button)
        self.hist_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.equalization_hist_menu_layout.addItem(self.hist_spacer)
        self.equalization_hist_menu_layout.addWidget(self.histogram_download_button)
        self.equalization_hist_menu_layout.addWidget(self.button_histogram_go_back)
        self.equalization_hist_menu.hide()

        self.transformation_menu_layout.addWidget(self.toggle2_button)
        self.transformation_menu_layout.addWidget(self.button_thresholding)
        self.transformation_menu_layout.addWidget(self.button_negative)
        self.transformation_menu_layout.addWidget(self.button_brightness)
        self.transformation_menu_layout.addWidget(self.button_logarithm_transformation)
        self.transformation_menu_layout.addWidget(self.button_power_law)
        self.transformation_menu_layout.addWidget(self.button_contrast_stretching)
        self.transformation_menu_layout.addWidget(self.button_intensity_level_slicing)
        self.transformation_menu_layout.addWidget(self.button_bit_plane_slicing)
        self.transformation_menu_layout.addWidget(self.button_steganography_apply)
        self.transformation_menu_layout.addWidget(self.button_steganography_undo)
        self.transformation_menu_layout.addWidget(self.transformation_download_button)
        self.transformation_menu_layout.addWidget(self.button_transformation_go_back)

        self.transformation_menu.hide()

        # Content
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # Content Layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # Top bar
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)

        # Left label to top bar
        self.top_label_left = QLabel("Aplicação para processamento de imagens")

        # Top spacer
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Right label to top bar
        self.top_label_right = QLabel("CALOPIMAGE")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # Add to layout
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # Bottom bar
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

        # Left label to bottom bar
        self.bottom_label_left = QLabel("Criado por: Davi I. L. Souza")

        # bottom spacer
        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Right label to bottom bar
        self.bottom_label_right = QLabel("© 2026")

        # Add to layout
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)

        # Application pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.ui_pages = Ui_StackedWidget()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page1)

        # Adding content to the page
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # Add widgets to app
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # Configuring the chapter dialog box
        self.select_part_window = QDialog()
        self.select_part_window_ui = dialog_method_select.Ui_Dialog()
        self.select_part_window_ui.setupUi(self.select_part_window)
        self.select_part_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.select_part_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "calopsita_appimage.png"))))
        self.select_part_window.setWindowTitle("Seleção de algoritmos")

        # Configuring the dialog box
        self.thresholding_window = QDialog()
        self.thresholding_window_ui = one_input.Ui_Dialog()
        self.thresholding_window_ui.setupUi(self.thresholding_window)
        self.thresholding_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.thresholding_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon1.svg"))))
        self.thresholding_window.setWindowTitle("Limiarização")

        self.brightness_window = QDialog()
        self.brightness_window_ui = one_input.Ui_Dialog()
        self.brightness_window_ui.setupUi(self.brightness_window)
        self.brightness_window_ui.retranslateUi(self.brightness_window, "Escreva um valor para ajustar o brilho", "1")
        self.brightness_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.brightness_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon10.svg"))))
        self.brightness_window.setWindowTitle("Brilho")

        self.negative_window = QDialog()
        self.negative_window_ui = one_input.Ui_Dialog()
        self.negative_window_ui.setupUi(self.negative_window)
        self.negative_window_ui.retranslateUi(self.negative_window, "Escreva um valor para L", "")
        self.negative_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.negative_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon2.svg"))))
        self.negative_window.setWindowTitle("Negativa")

        self.logarithm_transformation_window = QDialog()
        self.logarithm_transformation_window_ui = one_input.Ui_Dialog()
        self.logarithm_transformation_window_ui.setupUi(self.logarithm_transformation_window)
        self.logarithm_transformation_window_ui.retranslateUi(self.logarithm_transformation_window, "Escreva um valor para c", "")
        self.logarithm_transformation_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.logarithm_transformation_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon3.svg"))))
        self.logarithm_transformation_window.setWindowTitle("Transformação logarítmica")

        self.power_law_window = QDialog()
        self.power_law_window_ui = one_input.Ui_Dialog()
        self.power_law_window_ui.setupUi(self.power_law_window)
        self.power_law_window_ui.retranslateUi(self.power_law_window, "Escreva um valor para gamma", "1")
        self.power_law_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.power_law_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon4.svg"))))
        self.power_law_window.setWindowTitle("Transformação Gamma")

        self.intensity_level_slicing_window = QDialog()
        self.intensity_level_slicing_window_ui = three_input.Ui_Dialog()
        self.intensity_level_slicing_window_ui.setupUi(self.intensity_level_slicing_window)
        self.intensity_level_slicing_window.setStyleSheet("background-color: #44475a; font: 700 10pt 'Segoe UI'; color: white")
        self.intensity_level_slicing_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon7.svg"))))
        self.intensity_level_slicing_window.setWindowTitle("Transformação por nível de intensidade")

        self.bit_plane_slicing_window = QDialog()
        self.bit_plane_slicing_window_ui = one_input.Ui_Dialog()
        self.bit_plane_slicing_window_ui.setupUi(self.bit_plane_slicing_window)
        self.bit_plane_slicing_window_ui.retranslateUi(self.bit_plane_slicing_window, "Escreva um plano de bit de referência (entre 0 e 7)", "")
        self.bit_plane_slicing_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.bit_plane_slicing_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon6.svg"))))
        self.bit_plane_slicing_window.setWindowTitle("Transformação por planos de bits")

        self.steganopgraphy_apply_window = QDialog()
        self.steganopgraphy_apply_window_ui = one_input.Ui_Dialog()
        self.steganopgraphy_apply_window_ui.setupUi(self.steganopgraphy_apply_window)
        self.steganopgraphy_apply_window_ui.retranslateUi(self.steganopgraphy_apply_window, "Escreva uma mensagem qualquer", "")
        self.steganopgraphy_apply_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.steganopgraphy_apply_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon8.svg"))))
        self.steganopgraphy_apply_window.setWindowTitle("Aplicar Esteganografia")

        self.steganography_decode_window = QDialog()
        self.steganography_decode_window_ui = response.Ui_Dialog()
        self.steganography_decode_window_ui.setupUi(self.steganography_decode_window)
        self.steganography_decode_window.setStyleSheet("background-color: #44475a; font: 700 11pt 'Segoe UI'; color: white")
        self.steganography_decode_window.setWindowIcon(QPixmap(os.path.normpath(os.path.join(path, "icon9.svg"))))
        self.steganography_decode_window.setWindowTitle("Esteganografia decodificada")
        parent.setCentralWidget(self.central_frame)