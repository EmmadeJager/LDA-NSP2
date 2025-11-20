# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lda_vortex_histogram_edit_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(442, 667)
        self.verticalFrame = QFrame(Dialog)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setGeometry(QRect(10, 20, 421, 631))
        self.verticalFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.histogram_data_view_list = QListWidget(self.verticalFrame)
        self.histogram_data_view_list.setObjectName(u"histogram_data_view_list")

        self.verticalLayout.addWidget(self.histogram_data_view_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalFrame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.vortex_hist_x_spinbox = QDoubleSpinBox(self.verticalFrame)
        self.vortex_hist_x_spinbox.setObjectName(u"vortex_hist_x_spinbox")

        self.horizontalLayout.addWidget(self.vortex_hist_x_spinbox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.verticalFrame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.vortex_hist_y_spinbox = QDoubleSpinBox(self.verticalFrame)
        self.vortex_hist_y_spinbox.setObjectName(u"vortex_hist_y_spinbox")

        self.horizontalLayout_3.addWidget(self.vortex_hist_y_spinbox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalFrame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.vortex_hist_z_spinbox = QDoubleSpinBox(self.verticalFrame)
        self.vortex_hist_z_spinbox.setObjectName(u"vortex_hist_z_spinbox")

        self.horizontalLayout_2.addWidget(self.vortex_hist_z_spinbox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.histogram_edit_buttonbox = QDialogButtonBox(self.verticalFrame)
        self.histogram_edit_buttonbox.setObjectName(u"histogram_edit_buttonbox")
        self.histogram_edit_buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.histogram_edit_buttonbox.setCenterButtons(False)

        self.horizontalLayout_4.addWidget(self.histogram_edit_buttonbox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"X Measurement:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Y Measurement:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Z Measurement:", None))
    # retranslateUi

