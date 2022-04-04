# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 750)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/zoom-in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("*{\n"
"   border:none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:rgb(54, 34, 86);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.side_menu_container = QtWidgets.QFrame(self.centralwidget)
        self.side_menu_container.setEnabled(True)
        self.side_menu_container.setMaximumSize(QtCore.QSize(0, 16777215))
        self.side_menu_container.setStyleSheet("background-color:rgb(09,15,33);\n"
"color:#FFF\n"
"")
        self.side_menu_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_container.setObjectName("side_menu_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.slide_menu = QtWidgets.QFrame(self.side_menu_container)
        self.slide_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.slide_menu.setStyleSheet("QPushButton{\n"
"    border-left: 2px solid transparent;\n"
"    border-bottom: 2px solid transparent;\n"
"}\n"
"QPushButton::clicked\n"
"{\n"
"background-color : red;\n"
"}")
        self.slide_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_menu.setObjectName("slide_menu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.slide_menu)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.slide_menu)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#FFF")
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.frame_7 = QtWidgets.QFrame(self.slide_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_7.setFont(font)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.toolBox = QtWidgets.QToolBox(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("QToolBox{\n"
"  background-color:rgb(24,24,66);\n"
"  text-align:left;\n"
"}    \n"
"QToolBox::tab{\n"
"  border-radius:1px;\n"
"background-color:rgb(09,15,33);\n"
"  text-align:left;\n"
"}\n"
"")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 163, 121))
        self.page.setObjectName("page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_9 = QtWidgets.QFrame(self.page)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame_9.setFont(font)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setContentsMargins(5, 5, 0, 5)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.profileBtn = QtWidgets.QPushButton(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.profileBtn.setFont(font)
        self.profileBtn.setStyleSheet("QPushButton:hover{\n"
"background-color:rgb(50,110,255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconLogos/icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profileBtn.setIcon(icon1)
        self.profileBtn.setIconSize(QtCore.QSize(35, 35))
        self.profileBtn.setObjectName("profileBtn")
        self.verticalLayout_8.addWidget(self.profileBtn, 0, QtCore.Qt.AlignLeft)
        self.settingsBtn = QtWidgets.QPushButton(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.settingsBtn.setFont(font)
        self.settingsBtn.setStyleSheet("QPushButton:hover{\n"
"background-color:rgb(50,110,255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconLogos/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsBtn.setIcon(icon2)
        self.settingsBtn.setIconSize(QtCore.QSize(35, 35))
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_8.addWidget(self.settingsBtn, 0, QtCore.Qt.AlignLeft)
        self.feedbackBtn = QtWidgets.QPushButton(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.feedbackBtn.setFont(font)
        self.feedbackBtn.setStyleSheet("QPushButton:hover{\n"
"background-color:rgb(50,110,255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconLogos/icons/mail.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.feedbackBtn.setIcon(icon3)
        self.feedbackBtn.setIconSize(QtCore.QSize(35, 35))
        self.feedbackBtn.setObjectName("feedbackBtn")
        self.verticalLayout_8.addWidget(self.feedbackBtn, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_7.addWidget(self.frame_9, 0, QtCore.Qt.AlignTop)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 195, 84))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_10 = QtWidgets.QFrame(self.page_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setContentsMargins(5, 5, 0, 5)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.appVersionBtn = QtWidgets.QPushButton(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.appVersionBtn.setFont(font)
        self.appVersionBtn.setStyleSheet("QPushButton:hover{\n"
"background-color:rgb(50,110,255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/iconLogos/icons/smartphone.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.appVersionBtn.setIcon(icon4)
        self.appVersionBtn.setIconSize(QtCore.QSize(35, 35))
        self.appVersionBtn.setObjectName("appVersionBtn")
        self.verticalLayout_10.addWidget(self.appVersionBtn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.aboutBtn = QtWidgets.QPushButton(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.aboutBtn.setFont(font)
        self.aboutBtn.setStyleSheet("QPushButton:hover{\n"
"background-color:rgb(50,110,255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/iconLogos/icons/alert-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutBtn.setIcon(icon5)
        self.aboutBtn.setIconSize(QtCore.QSize(35, 35))
        self.aboutBtn.setObjectName("aboutBtn")
        self.verticalLayout_10.addWidget(self.aboutBtn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout_9.addWidget(self.frame_10, 0, QtCore.Qt.AlignTop)
        self.toolBox.addItem(self.page_2, "")
        self.verticalLayout_6.addWidget(self.toolBox, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.slide_menu)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.exit_button = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("QPushButton:hover{\n"
"background-color:rgb(50,110,255);\n"
"border-radius: 10px;\n"
"color:#FFF\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/iconLogos/icons/external-link.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(icon6)
        self.exit_button.setIconSize(QtCore.QSize(35, 35))
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_5.addWidget(self.exit_button, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.verticalLayout_4.addWidget(self.frame_8, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.slide_menu)
        self.gridLayout.addWidget(self.side_menu_container, 0, 0, 1, 1)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_body)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header_frame = QtWidgets.QFrame(self.main_body)
        self.Header_frame.setStyleSheet("background-color:rgb(09,15,33);\n"
"")
        self.Header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header_frame.setObjectName("Header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Header_frame)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.Header_frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.open_close_sidebar_button = QtWidgets.QPushButton(self.frame_3)
        self.open_close_sidebar_button.setStyleSheet("QPushButton:hover{\n"
"background-color:rgb(50,110,255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"\n"
"")
        self.open_close_sidebar_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/iconLogos/icons/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_close_sidebar_button.setIcon(icon7)
        self.open_close_sidebar_button.setIconSize(QtCore.QSize(35, 35))
        self.open_close_sidebar_button.setObjectName("open_close_sidebar_button")
        self.verticalLayout_33.addWidget(self.open_close_sidebar_button)
        self.horizontalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignLeft)
        self.frame_21 = QtWidgets.QFrame(self.Header_frame)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.backBtn = QtWidgets.QPushButton(self.frame_21)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.backBtn.setFont(font)
        self.backBtn.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(50,110,255);\n"
"border-radius: 10px;\n"
"color:#fff;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/iconLogos/icons/chevron-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backBtn.setIcon(icon8)
        self.backBtn.setIconSize(QtCore.QSize(35, 35))
        self.backBtn.setObjectName("backBtn")
        self.verticalLayout_29.addWidget(self.backBtn)
        self.horizontalLayout.addWidget(self.frame_21, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.frame_2 = QtWidgets.QFrame(self.Header_frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.LogOut = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LogOut.setFont(font)
        self.LogOut.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(50,110,255);\n"
"border-radius: 10px;\n"
"color:#FFF\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/iconLogos/icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LogOut.setIcon(icon9)
        self.LogOut.setIconSize(QtCore.QSize(35, 35))
        self.LogOut.setObjectName("LogOut")
        self.verticalLayout_26.addWidget(self.LogOut)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.Header_frame)
        self.frame.setStyleSheet("QPushButton:hover{\n"
"background-color:rgb(50,110,255);\n"
"border-radius: 10px;\n"
"color:#FFF\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minimize_window_button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minimize_window_button.setFont(font)
        self.minimize_window_button.setStyleSheet("color:#fff;\n"
"margin-right: 10px;")
        self.minimize_window_button.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/iconLogos/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_window_button.setIcon(icon10)
        self.minimize_window_button.setIconSize(QtCore.QSize(35, 35))
        self.minimize_window_button.setObjectName("minimize_window_button")
        self.horizontalLayout_3.addWidget(self.minimize_window_button)
        self.restore_window_button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.restore_window_button.setFont(font)
        self.restore_window_button.setStyleSheet("color:#fff;\n"
"margin-right: 10px;")
        self.restore_window_button.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/iconLogos/icons/maximize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restore_window_button.setIcon(icon11)
        self.restore_window_button.setIconSize(QtCore.QSize(35, 35))
        self.restore_window_button.setObjectName("restore_window_button")
        self.horizontalLayout_3.addWidget(self.restore_window_button)
        self.close_window_button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.close_window_button.setFont(font)
        self.close_window_button.setStyleSheet("color:#fff;\n"
"margin-right: 10px;")
        self.close_window_button.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/iconLogos/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_window_button.setIcon(icon12)
        self.close_window_button.setIconSize(QtCore.QSize(35, 35))
        self.close_window_button.setObjectName("close_window_button")
        self.horizontalLayout_3.addWidget(self.close_window_button)
        self.horizontalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.Header_frame)
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_body)
        self.stackedWidget.setObjectName("stackedWidget")
        self.MainPage = QtWidgets.QWidget()
        self.MainPage.setObjectName("MainPage")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.MainPage)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.main_body_contains = QtWidgets.QFrame(self.MainPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_contains.sizePolicy().hasHeightForWidth())
        self.main_body_contains.setSizePolicy(sizePolicy)
        self.main_body_contains.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body_contains.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_contains.setObjectName("main_body_contains")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.main_body_contains)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_11 = QtWidgets.QFrame(self.main_body_contains)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setStyleSheet("color:#FFF")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_4 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_12.addWidget(self.label_4)
        self.Name = QtWidgets.QLineEdit(self.frame_11)
        self.Name.setMinimumSize(QtCore.QSize(400, 60))
        self.Name.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Name.setFont(font)
        self.Name.setStyleSheet("QLineEdit{\n"
" border:1px solid white;\n"
" border-radius:10px;\n"
" Padding:5px;\n"
"}")
        self.Name.setObjectName("Name")
        self.verticalLayout_12.addWidget(self.Name, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Email = QtWidgets.QLineEdit(self.frame_11)
        self.Email.setMinimumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Email.setFont(font)
        self.Email.setStyleSheet("QLineEdit{\n"
" border:1px solid white;\n"
" border-radius:10px;\n"
" Padding:5px;\n"
"}")
        self.Email.setObjectName("Email")
        self.verticalLayout_12.addWidget(self.Email, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_3 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_12.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_11)
        self.dateEdit.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("color:#FFF;\n"
"")
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_12.addWidget(self.dateEdit, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_11.addWidget(self.frame_11)
        self.proceedBtn = QtWidgets.QPushButton(self.main_body_contains)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.proceedBtn.setFont(font)
        self.proceedBtn.setStyleSheet("QPushButton{\n"
"  background-color:black;\n"
"  text-align:centre;\n"
"  border-radius:15px;\n"
"  border:1px solid white;\n"
"  color:#FFF;\n"
"  padding:20px;\n"
"}    ")
        self.proceedBtn.setObjectName("proceedBtn")
        self.verticalLayout_11.addWidget(self.proceedBtn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_13.addWidget(self.main_body_contains)
        self.stackedWidget.addWidget(self.MainPage)
        self.greetPage = QtWidgets.QWidget()
        self.greetPage.setObjectName("greetPage")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.greetPage)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_22 = QtWidgets.QFrame(self.greetPage)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.frame_23 = QtWidgets.QFrame(self.frame_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_24 = QtWidgets.QFrame(self.frame_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_24)
        self.scrollArea.setStyleSheet("QScrollBar:vertical{\n"
"border:none;\n"
"background-color: rgb(39, 25, 63);\n"
"width:20px;\n"
"margin:15px 0 15px 0;\n"
"border-radius:0px;\n"
"}\n"
"/* Handle bar*/\n"
"QScrollBar::handle:vertical{\n"
"background-color: rgb(93, 59, 149);\n"
"min-height:30px;\n"
"border-radius:7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"background-color: rgb(255, 85, 255);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"background-color: rgb(93, 59, 149);\n"
"}\n"
"/* Button Top - Scrollbar*/\n"
"QScrollBar::sub-line:vertical{\n"
"border:none;\n"
"background-color: rgb(49, 35, 73);\n"
"height:15px;\n"
"border-top-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(255, 85, 255);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"background-color: rgb(36, 23, 58);\n"
"}\n"
"\n"
"/* Button Bottom - Scrollbar*/\n"
"QScrollBar::add-line:vertical{\n"
"border:none;\n"
"background-color: rgb(49, 35, 73);\n"
"height:15px;\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"QScrollBar::add-line:vertical:hover{\n"
"background-color: rgb(255, 85, 255);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"background-color: rgb(36, 23, 58);\n"
"}\n"
"\n"
"/* Reset Arrow*/\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down:vertical{\n"
"background:none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"background:none;\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 78, 40))
        self.scrollAreaWidgetContents_3.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.chat = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat.sizePolicy().hasHeightForWidth())
        self.chat.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chat.setFont(font)
        self.chat.setStyleSheet("color:#fff;")
        self.chat.setText("")
        self.chat.setTextFormat(QtCore.Qt.RichText)
        self.chat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.chat.setWordWrap(True)
        self.chat.setObjectName("chat")
        self.verticalLayout_45.addWidget(self.chat)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_44.addWidget(self.scrollArea)
        self.verticalLayout_3.addWidget(self.frame_24)
        self.frame_5 = QtWidgets.QFrame(self.frame_23)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_5.setStyleSheet("margin-top:5px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_6.setStyleSheet("margin-bottom:2px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.sendTextField = QtWidgets.QLineEdit(self.frame_6)
        self.sendTextField.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sendTextField.setFont(font)
        self.sendTextField.setStyleSheet("QLineEdit{\n"
" border:1px solid white;\n"
" border-radius:10px;\n"
" Padding:5px;\n"
"color:#fff;\n"
"}")
        self.sendTextField.setObjectName("sendTextField")
        self.verticalLayout_32.addWidget(self.sendTextField)
        self.horizontalLayout_6.addWidget(self.frame_6)
        self.frame_25 = QtWidgets.QFrame(self.frame_5)
        self.frame_25.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_25.setMaximumSize(QtCore.QSize(55, 52))
        self.frame_25.setStyleSheet("margin-left:4px;\n"
"margin-right:4px;\n"
"border-radius:12px;")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.MicBtn = QtWidgets.QPushButton(self.frame_25)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MicBtn.setFont(font)
        self.MicBtn.setStyleSheet("padding:2px;\n"
"margin-bottom:2px;\n"
"\n"
"")
        self.MicBtn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/iconLogos/icons/mic.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MicBtn.setIcon(icon13)
        self.MicBtn.setIconSize(QtCore.QSize(38, 38))
        self.MicBtn.setObjectName("MicBtn")
        self.verticalLayout_31.addWidget(self.MicBtn)
        self.horizontalLayout_6.addWidget(self.frame_25, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addWidget(self.frame_5, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_30.addWidget(self.frame_23)
        self.verticalLayout_19.addWidget(self.frame_22)
        self.stackedWidget.addWidget(self.greetPage)
        self.profilePage = QtWidgets.QWidget()
        self.profilePage.setObjectName("profilePage")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.profilePage)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_18 = QtWidgets.QFrame(self.profilePage)
        self.frame_18.setStyleSheet("")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.frame_20 = QtWidgets.QFrame(self.frame_18)
        self.frame_20.setAutoFillBackground(False)
        self.frame_20.setStyleSheet("")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.frame_40 = QtWidgets.QFrame(self.frame_20)
        self.frame_40.setStyleSheet("image: url(:/logo/User-removebg-preview.png);\n"
"background:none;\n"
"")
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.verticalLayout_27.addWidget(self.frame_40)
        self.frame_33 = QtWidgets.QFrame(self.frame_20)
        self.frame_33.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_33.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_33.setStyleSheet("background:none;")
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.label_16 = QtWidgets.QLabel(self.frame_33)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border-bottom:2px solid #e60540;\n"
"min-width:300px;\n"
"color:white")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_40.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.label_17 = QtWidgets.QLabel(self.frame_33)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("border-bottom:2px solid #e60540;\n"
"min-width:300px;\n"
"color:white")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_40.addWidget(self.label_17, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_18 = QtWidgets.QLabel(self.frame_33)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border-bottom:2px solid #e60540;\n"
"min-width:300px;\n"
"color:white")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_40.addWidget(self.label_18, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_27.addWidget(self.frame_33)
        self.verticalLayout_28.addWidget(self.frame_20)
        self.verticalLayout_14.addWidget(self.frame_18)
        self.stackedWidget.addWidget(self.profilePage)
        self.settingsPage = QtWidgets.QWidget()
        self.settingsPage.setObjectName("settingsPage")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.settingsPage)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_29 = QtWidgets.QFrame(self.settingsPage)
        self.frame_29.setStyleSheet("")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.frame_30 = QtWidgets.QFrame(self.frame_29)
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.label_6 = QtWidgets.QLabel(self.frame_30)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:#fff;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_37.addWidget(self.label_6)
        self.verticalLayout_36.addWidget(self.frame_30)
        self.frame_31 = QtWidgets.QFrame(self.frame_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy)
        self.frame_31.setStyleSheet("")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.frame_35 = QtWidgets.QFrame(self.frame_31)
        self.frame_35.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_35.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_35.setStyleSheet("background:none;")
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_38.addWidget(self.frame_35)
        self.frame_34 = QtWidgets.QFrame(self.frame_31)
        self.frame_34.setStyleSheet("background:none;")
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_34)
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.frame_36 = QtWidgets.QFrame(self.frame_34)
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_36)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.horizontalSlider = QtWidgets.QSlider(self.frame_36)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_7.addWidget(self.horizontalSlider, 0, QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_39.addWidget(self.frame_36)
        self.frame_37 = QtWidgets.QFrame(self.frame_34)
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.frame_39 = QtWidgets.QFrame(self.frame_37)
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.frame_39)
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.VolumeLabel = QtWidgets.QLabel(self.frame_39)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.VolumeLabel.setFont(font)
        self.VolumeLabel.setStyleSheet("color: white")
        self.VolumeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VolumeLabel.setObjectName("VolumeLabel")
        self.verticalLayout_42.addWidget(self.VolumeLabel, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_41.addWidget(self.frame_39, 0, QtCore.Qt.AlignVCenter)
        self.frame_38 = QtWidgets.QFrame(self.frame_37)
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.frame_38)
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.VolumeValue = QtWidgets.QLabel(self.frame_38)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.VolumeValue.setFont(font)
        self.VolumeValue.setStyleSheet("color:white")
        self.VolumeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.VolumeValue.setObjectName("VolumeValue")
        self.verticalLayout_43.addWidget(self.VolumeValue, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_41.addWidget(self.frame_38)
        self.verticalLayout_39.addWidget(self.frame_37)
        self.verticalLayout_38.addWidget(self.frame_34)
        self.verticalLayout_36.addWidget(self.frame_31)
        self.verticalLayout_15.addWidget(self.frame_29)
        self.stackedWidget.addWidget(self.settingsPage)
        self.feedbackPage = QtWidgets.QWidget()
        self.feedbackPage.setObjectName("feedbackPage")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.feedbackPage)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_19 = QtWidgets.QFrame(self.feedbackPage)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.frame_26 = QtWidgets.QFrame(self.frame_19)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.label_7 = QtWidgets.QLabel(self.frame_26)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#fff;")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_35.addWidget(self.label_7, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_34.addWidget(self.frame_26, 0, QtCore.Qt.AlignTop)
        self.frame_27 = QtWidgets.QFrame(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setStyleSheet("")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.frame_28 = QtWidgets.QFrame(self.frame_27)
        self.frame_28.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_28.setMaximumSize(QtCore.QSize(400, 600))
        self.frame_28.setStyleSheet("background:none;")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.label_8 = QtWidgets.QLabel(self.frame_28)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 371, 501))
        self.label_8.setStyleSheet("border-image: url(:/logo/Desktop/Feedback.jpg);\n"
"border-radius:15px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.frame_28)
        self.label_11.setGeometry(QtCore.QRect(20, 20, 361, 501))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color:rgba(0,0,0,180);\n"
"border-radius:15px;\n"
"")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_28)
        self.label_12.setGeometry(QtCore.QRect(130, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgba(255,255,255,210);\n"
"background-color:none;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.nameFdbk = QtWidgets.QLineEdit(self.frame_28)
        self.nameFdbk.setGeometry(QtCore.QRect(40, 110, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameFdbk.setFont(font)
        self.nameFdbk.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(230, 5, 64,255);\n"
"border-radius:10px;\n"
"color:rgba(255,255,255,230);\n"
"padding-left:5px;")
        self.nameFdbk.setObjectName("nameFdbk")
        self.emailFdbk = QtWidgets.QLineEdit(self.frame_28)
        self.emailFdbk.setGeometry(QtCore.QRect(40, 180, 320, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.emailFdbk.setFont(font)
        self.emailFdbk.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(230, 5, 64,255);\n"
"border-radius:10px;\n"
"color:white;\n"
"padding-left:5px;")
        self.emailFdbk.setObjectName("emailFdbk")
        self.enterFdbk = QtWidgets.QTextEdit(self.frame_28)
        self.enterFdbk.setGeometry(QtCore.QRect(40, 250, 320, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enterFdbk.setFont(font)
        self.enterFdbk.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(230, 5, 64,255);\n"
"border-radius:10px;\n"
"color:rgba(255,255,255,230);\n"
"padding-left:5px;")
        self.enterFdbk.setObjectName("enterFdbk")
        self.sendFdbk = QtWidgets.QPushButton(self.frame_28)
        self.sendFdbk.setGeometry(QtCore.QRect(40, 450, 320, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendFdbk.setFont(font)
        self.sendFdbk.setStyleSheet("QPushButton{\n"
"color:rgba(255,255,255,210);\n"
"border-radius:10px;\n"
"background-color:rgba(230, 5, 64);\n"
"}\n"
"QPushButton:hover{\n"
"color:rgba(255,255,255,210);\n"
"border-radius:10px;\n"
"background-color:rgba(0,0,0,60);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(0,0,0,40);\n"
"}\n"
"")
        self.sendFdbk.setObjectName("sendFdbk")
        self.horizontalLayout_4.addWidget(self.frame_28)
        spacerItem3 = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_34.addWidget(self.frame_27)
        self.verticalLayout_16.addWidget(self.frame_19)
        self.stackedWidget.addWidget(self.feedbackPage)
        self.appVersionPage = QtWidgets.QWidget()
        self.appVersionPage.setObjectName("appVersionPage")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.appVersionPage)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_15 = QtWidgets.QFrame(self.appVersionPage)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_10 = QtWidgets.QLabel(self.frame_16)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:#fff;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_24.addWidget(self.label_10)
        self.verticalLayout_23.addWidget(self.frame_16, 0, QtCore.Qt.AlignTop)
        self.frame_17 = QtWidgets.QFrame(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_17)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_2.setStyleSheet("color:#fff;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_25.addWidget(self.textEdit_2)
        self.verticalLayout_23.addWidget(self.frame_17)
        self.verticalLayout_17.addWidget(self.frame_15)
        self.stackedWidget.addWidget(self.appVersionPage)
        self.aboutPage = QtWidgets.QWidget()
        self.aboutPage.setObjectName("aboutPage")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.aboutPage)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_12 = QtWidgets.QFrame(self.aboutPage)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frame_13.setFont(font)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_9 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:#fff;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_21.addWidget(self.label_9, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_20.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.textEdit = QtWidgets.QTextEdit(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color:#fff;\n"
"\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_22.addWidget(self.textEdit)
        self.verticalLayout_20.addWidget(self.frame_14)
        self.verticalLayout_18.addWidget(self.frame_12)
        self.stackedWidget.addWidget(self.aboutPage)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.footer = QtWidgets.QFrame(self.main_body)
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.size_grip = QtWidgets.QFrame(self.footer)
        self.size_grip.setMinimumSize(QtCore.QSize(10, 10))
        self.size_grip.setMaximumSize(QtCore.QSize(10, 10))
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.horizontalLayout_2.addWidget(self.size_grip, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.footer, 0, QtCore.Qt.AlignBottom)
        self.gridLayout.addWidget(self.main_body, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        self.toolBox.layout().setSpacing(7)
        self.stackedWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ΔLITΔ"))
        self.profileBtn.setText(_translate("MainWindow", "Profile   "))
        self.settingsBtn.setText(_translate("MainWindow", "Settings   "))
        self.feedbackBtn.setText(_translate("MainWindow", "Feedback   "))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Menu"))
        self.appVersionBtn.setText(_translate("MainWindow", "App Version   "))
        self.aboutBtn.setText(_translate("MainWindow", "About ALITA   "))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "App Information"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.backBtn.setText(_translate("MainWindow", "Back   "))
        self.LogOut.setText(_translate("MainWindow", "Log Out  "))
        self.label_4.setText(_translate("MainWindow", "Welcome To ΔLITΔ"))
        self.Name.setPlaceholderText(_translate("MainWindow", "Name"))
        self.Email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Select Your Date Of Birth"))
        self.proceedBtn.setText(_translate("MainWindow", "PROCEED"))
        self.sendTextField.setPlaceholderText(_translate("MainWindow", "Ask ALITA anything"))
        self.label_16.setText(_translate("MainWindow", "Name"))
        self.label_17.setText(_translate("MainWindow", "Email"))
        self.label_18.setText(_translate("MainWindow", "Date Of Birth"))
        self.label_6.setText(_translate("MainWindow", "Adjust ALITA\'s Volume"))
        self.VolumeLabel.setText(_translate("MainWindow", "Volume"))
        self.VolumeValue.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "FEEDBACK"))
        self.nameFdbk.setPlaceholderText(_translate("MainWindow", "Name"))
        self.emailFdbk.setPlaceholderText(_translate("MainWindow", "Email"))
        self.enterFdbk.setPlaceholderText(_translate("MainWindow", "Feedback"))
        self.sendFdbk.setText(_translate("MainWindow", "Send"))
        self.label_10.setText(_translate("MainWindow", "Version"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">- You are running V1.0.0</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "About ΔLITΔ"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Alita is based on the python as it has a standard library in development, and a few for AI. It has an intuitive syntax, basic control flow, and data structures. Alita can help you to Complete some chores like sending emails, many more tasks can be performed over voice command and not only that you can ask some questions of which you don’t know answers like simple math problems and questions about history and assistant can give you information and resources to look upon.</span></p></body></html>"))

import iconLogos_rc
import logo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

