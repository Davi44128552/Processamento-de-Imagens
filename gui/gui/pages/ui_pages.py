# This Python file was made with Qt Widgets Designer
from qt_core import *
import os

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(489, 615)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout = QVBoxLayout(self.page1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.page1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Loading the image
        directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(directory, "..", "..", "images", "calopsita.png")
        image_path = os.path.normpath(image_path)

        # Loading cockatiel icon
        cockatiel_icon = QPixmap(image_path)
        cockatiel_icon = cockatiel_icon.scaled(275, 275, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.label_3.setPixmap(cockatiel_icon)

        self.verticalLayout.addWidget(self.label_3)

        StackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_2 = QVBoxLayout(self.page2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        StackedWidget.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.verticalLayout_3 = QVBoxLayout(self.page3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        StackedWidget.addWidget(self.page3)

        self.retranslateUi(StackedWidget)

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"pagina2", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"pagina 3", None))
    # retranslateUi

