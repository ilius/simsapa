# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simsapa/assets/ui/cards_browser_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CardsBrowserWindow(object):
    def setupUi(self, CardsBrowserWindow):
        CardsBrowserWindow.setObjectName("CardsBrowserWindow")
        CardsBrowserWindow.resize(856, 581)
        CardsBrowserWindow.setBaseSize(QtCore.QSize(800, 600))
        self.central_widget = QtWidgets.QWidget(CardsBrowserWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.front_input = QtWidgets.QPlainTextEdit(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.front_input.sizePolicy().hasHeightForWidth())
        self.front_input.setSizePolicy(sizePolicy)
        self.front_input.setMinimumSize(QtCore.QSize(0, 50))
        self.front_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.front_input.setObjectName("front_input")
        self.verticalLayout.addWidget(self.front_input)
        self.label_2 = QtWidgets.QLabel(self.central_widget)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.back_input = QtWidgets.QPlainTextEdit(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_input.sizePolicy().hasHeightForWidth())
        self.back_input.setSizePolicy(sizePolicy)
        self.back_input.setMinimumSize(QtCore.QSize(0, 50))
        self.back_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.back_input.setObjectName("back_input")
        self.verticalLayout.addWidget(self.back_input)
        self.main_layout.addLayout(self.verticalLayout)
        self.searchbar_layout = QtWidgets.QHBoxLayout()
        self.searchbar_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.searchbar_layout.setObjectName("searchbar_layout")
        self.search_input = QtWidgets.QLineEdit(self.central_widget)
        self.search_input.setMinimumSize(QtCore.QSize(0, 35))
        self.search_input.setClearButtonEnabled(True)
        self.search_input.setObjectName("search_input")
        self.searchbar_layout.addWidget(self.search_input)
        self.search_button = QtWidgets.QPushButton(self.central_widget)
        self.search_button.setMinimumSize(QtCore.QSize(0, 40))
        self.search_button.setObjectName("search_button")
        self.searchbar_layout.addWidget(self.search_button)
        self.main_layout.addLayout(self.searchbar_layout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cards_list = QtWidgets.QListView(self.central_widget)
        self.cards_list.setObjectName("cards_list")
        self.verticalLayout_2.addWidget(self.cards_list)
        self.main_layout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.main_layout)
        CardsBrowserWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(CardsBrowserWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 20))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Windows = QtWidgets.QMenu(self.menubar)
        self.menu_Windows.setObjectName("menu_Windows")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Cards = QtWidgets.QMenu(self.menubar)
        self.menu_Cards.setObjectName("menu_Cards")
        CardsBrowserWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CardsBrowserWindow)
        self.statusbar.setObjectName("statusbar")
        CardsBrowserWindow.setStatusBar(self.statusbar)
        self.toolBar_2 = QtWidgets.QToolBar(CardsBrowserWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        CardsBrowserWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.action_Copy = QtWidgets.QAction(CardsBrowserWindow)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtWidgets.QAction(CardsBrowserWindow)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Quit = QtWidgets.QAction(CardsBrowserWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/close"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Sutta_Search = QtWidgets.QAction(CardsBrowserWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/book"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Sutta_Search.setIcon(icon1)
        self.action_Sutta_Search.setObjectName("action_Sutta_Search")
        self.action_Dictionary_Search = QtWidgets.QAction(CardsBrowserWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/dictionary"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Dictionary_Search.setIcon(icon2)
        self.action_Dictionary_Search.setObjectName("action_Dictionary_Search")
        self.action_About = QtWidgets.QAction(CardsBrowserWindow)
        self.action_About.setObjectName("action_About")
        self.action_Website = QtWidgets.QAction(CardsBrowserWindow)
        self.action_Website.setObjectName("action_Website")
        self.action_Close_Window = QtWidgets.QAction(CardsBrowserWindow)
        self.action_Close_Window.setObjectName("action_Close_Window")
        self.action_Open = QtWidgets.QAction(CardsBrowserWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Document_Reader = QtWidgets.QAction(CardsBrowserWindow)
        self.action_Document_Reader.setObjectName("action_Document_Reader")
        self.action_Add = QtWidgets.QAction(CardsBrowserWindow)
        self.action_Add.setObjectName("action_Add")
        self.action_Remove = QtWidgets.QAction(CardsBrowserWindow)
        self.action_Remove.setObjectName("action_Remove")
        self.action_Open_Selected = QtWidgets.QAction(CardsBrowserWindow)
        self.action_Open_Selected.setObjectName("action_Open_Selected")
        self.action_Library = QtWidgets.QAction(CardsBrowserWindow)
        self.action_Library.setObjectName("action_Library")
        self.action_Sync_to_Anki = QtWidgets.QAction(CardsBrowserWindow)
        self.action_Sync_to_Anki.setObjectName("action_Sync_to_Anki")
        self.action_Cards = QtWidgets.QAction(CardsBrowserWindow)
        self.action_Cards.setObjectName("action_Cards")
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Close_Window)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Windows.addAction(self.action_Sutta_Search)
        self.menu_Windows.addAction(self.action_Dictionary_Search)
        self.menu_Windows.addAction(self.action_Document_Reader)
        self.menu_Windows.addAction(self.action_Library)
        self.menu_Windows.addAction(self.action_Cards)
        self.menu_Help.addAction(self.action_Website)
        self.menu_Help.addAction(self.action_About)
        self.menu_Cards.addAction(self.action_Sync_to_Anki)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Windows.menuAction())
        self.menubar.addAction(self.menu_Cards.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar_2.addAction(self.action_Add)
        self.toolBar_2.addAction(self.action_Remove)
        self.toolBar_2.addAction(self.action_Sync_to_Anki)

        self.retranslateUi(CardsBrowserWindow)
        QtCore.QMetaObject.connectSlotsByName(CardsBrowserWindow)

    def retranslateUi(self, CardsBrowserWindow):
        _translate = QtCore.QCoreApplication.translate
        CardsBrowserWindow.setWindowTitle(_translate("CardsBrowserWindow", "Library - Simsapa"))
        self.label.setText(_translate("CardsBrowserWindow", "Front"))
        self.label_2.setText(_translate("CardsBrowserWindow", "Back"))
        self.search_button.setText(_translate("CardsBrowserWindow", "Search"))
        self.menu_File.setTitle(_translate("CardsBrowserWindow", "&File"))
        self.menu_Edit.setTitle(_translate("CardsBrowserWindow", "&Edit"))
        self.menu_Windows.setTitle(_translate("CardsBrowserWindow", "&Windows"))
        self.menu_Help.setTitle(_translate("CardsBrowserWindow", "&Help"))
        self.menu_Cards.setTitle(_translate("CardsBrowserWindow", "&Cards"))
        self.toolBar_2.setWindowTitle(_translate("CardsBrowserWindow", "toolBar_2"))
        self.action_Copy.setText(_translate("CardsBrowserWindow", "&Copy"))
        self.action_Paste.setText(_translate("CardsBrowserWindow", "&Paste"))
        self.action_Quit.setText(_translate("CardsBrowserWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("CardsBrowserWindow", "Ctrl+Q"))
        self.action_Sutta_Search.setText(_translate("CardsBrowserWindow", "&Sutta Search"))
        self.action_Sutta_Search.setShortcut(_translate("CardsBrowserWindow", "F5"))
        self.action_Dictionary_Search.setText(_translate("CardsBrowserWindow", "&Dictionary Search"))
        self.action_Dictionary_Search.setShortcut(_translate("CardsBrowserWindow", "F6"))
        self.action_About.setText(_translate("CardsBrowserWindow", "&About"))
        self.action_Website.setText(_translate("CardsBrowserWindow", "&Website"))
        self.action_Close_Window.setText(_translate("CardsBrowserWindow", "&Close Window"))
        self.action_Open.setText(_translate("CardsBrowserWindow", "&Open..."))
        self.action_Open.setShortcut(_translate("CardsBrowserWindow", "Ctrl+O"))
        self.action_Document_Reader.setText(_translate("CardsBrowserWindow", "D&ocument Reader"))
        self.action_Document_Reader.setToolTip(_translate("CardsBrowserWindow", "Document Reader"))
        self.action_Document_Reader.setShortcut(_translate("CardsBrowserWindow", "F7"))
        self.action_Add.setText(_translate("CardsBrowserWindow", "&Add..."))
        self.action_Remove.setText(_translate("CardsBrowserWindow", "&Remove"))
        self.action_Remove.setShortcut(_translate("CardsBrowserWindow", "Del"))
        self.action_Open_Selected.setText(_translate("CardsBrowserWindow", "&Open Selected"))
        self.action_Library.setText(_translate("CardsBrowserWindow", "&Library"))
        self.action_Library.setShortcut(_translate("CardsBrowserWindow", "F8"))
        self.action_Sync_to_Anki.setText(_translate("CardsBrowserWindow", "&Sync to Anki"))
        self.action_Cards.setText(_translate("CardsBrowserWindow", "&Cards"))
        self.action_Cards.setToolTip(_translate("CardsBrowserWindow", "Cards"))
        self.action_Cards.setShortcut(_translate("CardsBrowserWindow", "F9"))
from simsapa.assets import icons_rc
