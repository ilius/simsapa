# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simsapa/assets/ui/sutta_search_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SuttaSearchWindow(object):
    def setupUi(self, SuttaSearchWindow):
        SuttaSearchWindow.setObjectName("SuttaSearchWindow")
        SuttaSearchWindow.resize(856, 581)
        SuttaSearchWindow.setBaseSize(QtCore.QSize(800, 600))
        self.central_widget = QtWidgets.QWidget(SuttaSearchWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
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
        self.splitter = QtWidgets.QSplitter(self.central_widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.content_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setObjectName("content_layout")
        self.content_title = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.content_title.setObjectName("content_title")
        self.content_layout.addWidget(self.content_title)
        self.content_html = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.content_html.setObjectName("content_html")
        self.content_layout.addWidget(self.content_html)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.results_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.results_layout.setContentsMargins(0, 0, 0, 0)
        self.results_layout.setObjectName("results_layout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.results_layout.addWidget(self.label_2)
        self.results_list = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.results_list.setObjectName("results_list")
        self.results_layout.addWidget(self.results_list)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.results_layout.addWidget(self.label_3)
        self.history_list = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.history_list.setObjectName("history_list")
        self.results_layout.addWidget(self.history_list)
        self.main_layout.addWidget(self.splitter)
        self.horizontalLayout_2.addLayout(self.main_layout)
        SuttaSearchWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(SuttaSearchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 20))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menuWindows = QtWidgets.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        SuttaSearchWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SuttaSearchWindow)
        self.statusbar.setObjectName("statusbar")
        SuttaSearchWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(SuttaSearchWindow)
        self.toolBar.setObjectName("toolBar")
        SuttaSearchWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.action_Copy = QtWidgets.QAction(SuttaSearchWindow)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtWidgets.QAction(SuttaSearchWindow)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Quit = QtWidgets.QAction(SuttaSearchWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/close"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Sutta_Search = QtWidgets.QAction(SuttaSearchWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/book"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Sutta_Search.setIcon(icon1)
        self.action_Sutta_Search.setObjectName("action_Sutta_Search")
        self.action_Dictionary_Search = QtWidgets.QAction(SuttaSearchWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/dictionary"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Dictionary_Search.setIcon(icon2)
        self.action_Dictionary_Search.setObjectName("action_Dictionary_Search")
        self.action_About = QtWidgets.QAction(SuttaSearchWindow)
        self.action_About.setObjectName("action_About")
        self.action_Website = QtWidgets.QAction(SuttaSearchWindow)
        self.action_Website.setObjectName("action_Website")
        self.menu_File.addAction(self.action_Quit)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menuWindows.addAction(self.action_Sutta_Search)
        self.menuWindows.addAction(self.action_Dictionary_Search)
        self.menu_Help.addAction(self.action_Website)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.action_Sutta_Search)
        self.toolBar.addAction(self.action_Dictionary_Search)

        self.retranslateUi(SuttaSearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SuttaSearchWindow)

    def retranslateUi(self, SuttaSearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SuttaSearchWindow.setWindowTitle(_translate("SuttaSearchWindow", "Sutta Search - Simsapa"))
        self.search_button.setText(_translate("SuttaSearchWindow", "Search"))
        self.content_title.setText(_translate("SuttaSearchWindow", "Title"))
        self.label_2.setText(_translate("SuttaSearchWindow", "Results"))
        self.label_3.setText(_translate("SuttaSearchWindow", "History"))
        self.menu_File.setTitle(_translate("SuttaSearchWindow", "&File"))
        self.menu_Edit.setTitle(_translate("SuttaSearchWindow", "&Edit"))
        self.menuWindows.setTitle(_translate("SuttaSearchWindow", "Windows"))
        self.menu_Help.setTitle(_translate("SuttaSearchWindow", "&Help"))
        self.toolBar.setWindowTitle(_translate("SuttaSearchWindow", "toolBar"))
        self.action_Copy.setText(_translate("SuttaSearchWindow", "&Copy"))
        self.action_Paste.setText(_translate("SuttaSearchWindow", "&Paste"))
        self.action_Quit.setText(_translate("SuttaSearchWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("SuttaSearchWindow", "Ctrl+Q"))
        self.action_Sutta_Search.setText(_translate("SuttaSearchWindow", "&Sutta Search"))
        self.action_Sutta_Search.setShortcut(_translate("SuttaSearchWindow", "F5"))
        self.action_Dictionary_Search.setText(_translate("SuttaSearchWindow", "&Dictionary Search"))
        self.action_Dictionary_Search.setShortcut(_translate("SuttaSearchWindow", "F6"))
        self.action_About.setText(_translate("SuttaSearchWindow", "&About"))
        self.action_Website.setText(_translate("SuttaSearchWindow", "&Website"))
from simsapa.assets import icons_rc
