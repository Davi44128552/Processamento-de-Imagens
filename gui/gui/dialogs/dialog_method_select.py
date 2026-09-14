from qt_core import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(321, 195)
        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 20, 371, 41))
        self.radioButton.setChecked(True)
        self.radioButton_2 = QRadioButton(Dialog)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(20, 70, 250, 20))
        self.radioButton_3 = QRadioButton(Dialog)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(20, 110, 171, 20))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 150, 91, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Transforma\u00e7\u00f5es de intensidade", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Equaliza\u00e7\u00e3o de Histograma", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Filtragem espacial", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Selecionar", None))
    # retranslateUi

