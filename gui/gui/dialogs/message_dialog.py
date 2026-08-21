from qt_core import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(726, 300)
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 10, 711, 281))
        self.textEdit.setStyleSheet(u"background-color: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Shadow.Sunken)
        self.textEdit.setReadOnly(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog, message = ""):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", message))
        self.textEdit.setPlainText(message)
    # retranslateUi

