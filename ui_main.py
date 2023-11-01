# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'discad.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSplitter,
    QWidget)
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 404)
        MainWindow.setMinimumSize(QSize(650, 404))
        MainWindow.setMaximumSize(QSize(650, 404))
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(-10, -10, 749, 421))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(749, 421))
        self.frame.setBaseSize(QSize(750, 421))
        self.frame.setAcceptDrops(False)
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"image: url(:/imagens/imb/1.png);")
        self.frame.setInputMethodHints(Qt.ImhPreferUppercase)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.btn_cadastrar = QPushButton(self.frame)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(246, 40, 79, 24))
        icon = QIcon()
        icon.addFile(u"imb/search_book_open_search_locate_6178.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar.setIcon(icon)
        self.btn_cadastrar.setAutoExclusive(False)
        self.List_View = QListWidget(self.frame)
        self.List_View.setObjectName(u"List_View")
        self.List_View.setGeometry(QRect(50, 100, 571, 281))
        self.List_View.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(490, 0, 181, 111))
        self.frame_2.setBaseSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"image: url(:/imagens/imb/1635552453975-removebg-preview.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(580, 390, 81, 20))
        font = QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(60, 44, 183, 22))
        self.splitter.setOrientation(Qt.Vertical)
        self.txt_placa = QLineEdit(self.splitter)
        self.txt_placa.setObjectName(u"txt_placa")
        self.txt_placa.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.txt_placa.setFont(font1)
        self.txt_placa.setLayoutDirection(Qt.LeftToRight)
        self.txt_placa.setInputMethodHints(Qt.ImhUppercaseOnly)
        self.txt_placa.setMaxLength(7)
        self.splitter.addWidget(self.txt_placa)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 390, 521, 23))
        self.progressBar.setValue(0)
        self.txt_equipamento = QLineEdit(self.frame)
        self.txt_equipamento.setObjectName(u"txt_equipamento")
        self.txt_equipamento.setEnabled(True)
        self.txt_equipamento.setGeometry(QRect(60, 70, 183, 22))
        self.txt_equipamento.setFont(font1)
        self.txt_equipamento.setLayoutDirection(Qt.LeftToRight)
        self.txt_equipamento.setInputMethodHints(Qt.ImhUppercaseOnly)
        self.txt_equipamento.setMaxLength(7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cadastro de veiculos", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/imbjpg/download.jpg\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.frame.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.frame.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_cadastrar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_cadastrar.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BruTha CadEquiPla", None))
        self.txt_placa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite a placa", None))
#if QT_CONFIG(accessibility)
        self.progressBar.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.txt_equipamento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o equipamento", None))
    # retranslateUi

