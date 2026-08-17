# Importing modules
import sys
import os
import ctypes
from qt_core import *
from gui.windows.main_win.ui_main_window import *

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
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # Showing the GUI
        self.show()

        # Adding the behavior to the button
        self.ui.toggle_button.clicked.connect(self.toggle)
        self.ui.toggle_button2.clicked.connect(self.select_image)
        self.ui.toggle_button3.clicked.connect(self.random_image)
        self.ui.config_button.clicked.connect(self.help)

    # Button behavior
    def toggle(self):
        self.ui.toggle_button.set_active(True)
        self.ui.toggle_button2.set_active(False)
        self.ui.toggle_button3.set_active(False)
        self.ui.config_button.set_active(False)

    def select_image(self):
        self.ui.toggle_button.set_active(False)
        self.ui.toggle_button2.set_active(True)
        self.ui.toggle_button3.set_active(False)
        self.ui.config_button.set_active(False)

    def random_image(self):
        self.ui.toggle_button2.set_active(False)
        self.ui.toggle_button3.set_active(True)
        self.ui.config_button.set_active(False)

    def help(self):
        self.ui.toggle_button2.set_active(False)
        self.ui.toggle_button3.set_active(False)
        self.ui.config_button.set_active(True)

    # Adding a action to toggle button
    def toggle_button(self):

        # Configing
        menu_width = self.ui.left_menu.width()
        width = 50
        if (menu_width == 50):
            width = 250

        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()
        

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