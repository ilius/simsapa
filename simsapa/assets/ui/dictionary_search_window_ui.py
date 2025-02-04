# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simsapa/assets/ui/dictionary_search_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DictionarySearchWindow(object):
    def setupUi(self, DictionarySearchWindow):
        DictionarySearchWindow.setObjectName("DictionarySearchWindow")
        DictionarySearchWindow.resize(1068, 642)
        DictionarySearchWindow.setBaseSize(QtCore.QSize(800, 600))
        self.central_widget = QtWidgets.QWidget(DictionarySearchWindow)
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
        spacerItem = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.content_layout.addItem(spacerItem)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.tabs_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.tabs_layout.setContentsMargins(0, 0, 0, 0)
        self.tabs_layout.setObjectName("tabs_layout")
        self.rightside_tabs = QtWidgets.QTabWidget(self.verticalLayoutWidget_3)
        self.rightside_tabs.setMinimumSize(QtCore.QSize(500, 500))
        self.rightside_tabs.setObjectName("rightside_tabs")
        self.results_tab = QtWidgets.QWidget()
        self.results_tab.setObjectName("results_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.results_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.results_list = QtWidgets.QListWidget(self.results_tab)
        self.results_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.results_list.setObjectName("results_list")
        self.verticalLayout.addWidget(self.results_list)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.rightside_tabs.addTab(self.results_tab, "")
        self.links_tab = QtWidgets.QWidget()
        self.links_tab.setObjectName("links_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.links_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.links_layout = QtWidgets.QVBoxLayout()
        self.links_layout.setObjectName("links_layout")
        self.verticalLayout_5.addLayout(self.links_layout)
        self.rightside_tabs.addTab(self.links_tab, "")
        self.memos_tab = QtWidgets.QWidget()
        self.memos_tab.setObjectName("memos_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.memos_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.memos_layout = QtWidgets.QVBoxLayout()
        self.memos_layout.setObjectName("memos_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_memo_button = QtWidgets.QPushButton(self.memos_tab)
        self.add_memo_button.setObjectName("add_memo_button")
        self.horizontalLayout.addWidget(self.add_memo_button)
        self.clear_memo_button = QtWidgets.QPushButton(self.memos_tab)
        self.clear_memo_button.setObjectName("clear_memo_button")
        self.horizontalLayout.addWidget(self.clear_memo_button)
        self.remove_memo_button = QtWidgets.QPushButton(self.memos_tab)
        self.remove_memo_button.setObjectName("remove_memo_button")
        self.horizontalLayout.addWidget(self.remove_memo_button)
        self.memos_layout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.memos_tab)
        self.label_2.setObjectName("label_2")
        self.memos_layout.addWidget(self.label_2)
        self.front_input = QtWidgets.QPlainTextEdit(self.memos_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.front_input.sizePolicy().hasHeightForWidth())
        self.front_input.setSizePolicy(sizePolicy)
        self.front_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.front_input.setObjectName("front_input")
        self.memos_layout.addWidget(self.front_input)
        self.label_5 = QtWidgets.QLabel(self.memos_tab)
        self.label_5.setObjectName("label_5")
        self.memos_layout.addWidget(self.label_5)
        self.back_input = QtWidgets.QPlainTextEdit(self.memos_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_input.sizePolicy().hasHeightForWidth())
        self.back_input.setSizePolicy(sizePolicy)
        self.back_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.back_input.setObjectName("back_input")
        self.memos_layout.addWidget(self.back_input)
        self.label_3 = QtWidgets.QLabel(self.memos_tab)
        self.label_3.setObjectName("label_3")
        self.memos_layout.addWidget(self.label_3)
        self.memos_list = QtWidgets.QListView(self.memos_tab)
        self.memos_list.setObjectName("memos_list")
        self.memos_layout.addWidget(self.memos_list)
        self.verticalLayout_6.addLayout(self.memos_layout)
        self.rightside_tabs.addTab(self.memos_tab, "")
        self.recent_tab = QtWidgets.QWidget()
        self.recent_tab.setObjectName("recent_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.recent_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.recent_layout = QtWidgets.QVBoxLayout()
        self.recent_layout.setObjectName("recent_layout")
        self.recent_list = QtWidgets.QListWidget(self.recent_tab)
        self.recent_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.recent_list.setObjectName("recent_list")
        self.recent_layout.addWidget(self.recent_list)
        self.verticalLayout_3.addLayout(self.recent_layout)
        self.rightside_tabs.addTab(self.recent_tab, "")
        self.tabs_layout.addWidget(self.rightside_tabs)
        self.main_layout.addWidget(self.splitter)
        self.horizontalLayout_2.addLayout(self.main_layout)
        DictionarySearchWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(DictionarySearchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 20))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Windows = QtWidgets.QMenu(self.menubar)
        self.menu_Windows.setObjectName("menu_Windows")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        DictionarySearchWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DictionarySearchWindow)
        self.statusbar.setObjectName("statusbar")
        DictionarySearchWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(DictionarySearchWindow)
        self.toolBar.setObjectName("toolBar")
        DictionarySearchWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.action_Copy = QtWidgets.QAction(DictionarySearchWindow)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtWidgets.QAction(DictionarySearchWindow)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Quit = QtWidgets.QAction(DictionarySearchWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/close"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Sutta_Search = QtWidgets.QAction(DictionarySearchWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/book"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Sutta_Search.setIcon(icon1)
        self.action_Sutta_Search.setObjectName("action_Sutta_Search")
        self.action_Dictionary_Search = QtWidgets.QAction(DictionarySearchWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/dictionary"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Dictionary_Search.setIcon(icon2)
        self.action_Dictionary_Search.setObjectName("action_Dictionary_Search")
        self.action_About = QtWidgets.QAction(DictionarySearchWindow)
        self.action_About.setObjectName("action_About")
        self.action_Website = QtWidgets.QAction(DictionarySearchWindow)
        self.action_Website.setObjectName("action_Website")
        self.action_Close_Window = QtWidgets.QAction(DictionarySearchWindow)
        self.action_Close_Window.setObjectName("action_Close_Window")
        self.action_Open = QtWidgets.QAction(DictionarySearchWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Document_Reader = QtWidgets.QAction(DictionarySearchWindow)
        self.action_Document_Reader.setObjectName("action_Document_Reader")
        self.action_Library = QtWidgets.QAction(DictionarySearchWindow)
        self.action_Library.setObjectName("action_Library")
        self.action_Memos = QtWidgets.QAction(DictionarySearchWindow)
        self.action_Memos.setObjectName("action_Memos")
        self.action_Dictionaries_Manager = QtWidgets.QAction(DictionarySearchWindow)
        self.action_Dictionaries_Manager.setObjectName("action_Dictionaries_Manager")
        self.action_Links = QtWidgets.QAction(DictionarySearchWindow)
        self.action_Links.setObjectName("action_Links")
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Close_Window)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Windows.addAction(self.action_Sutta_Search)
        self.menu_Windows.addAction(self.action_Dictionary_Search)
        self.menu_Windows.addAction(self.action_Dictionaries_Manager)
        self.menu_Windows.addAction(self.action_Document_Reader)
        self.menu_Windows.addAction(self.action_Library)
        self.menu_Windows.addAction(self.action_Memos)
        self.menu_Windows.addAction(self.action_Links)
        self.menu_Help.addAction(self.action_Website)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Windows.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.action_Sutta_Search)
        self.toolBar.addAction(self.action_Dictionary_Search)

        self.retranslateUi(DictionarySearchWindow)
        self.rightside_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DictionarySearchWindow)

    def retranslateUi(self, DictionarySearchWindow):
        _translate = QtCore.QCoreApplication.translate
        DictionarySearchWindow.setWindowTitle(_translate("DictionarySearchWindow", "Dictionary Search - Simsapa"))
        self.search_button.setText(_translate("DictionarySearchWindow", "Search"))
        self.rightside_tabs.setTabText(self.rightside_tabs.indexOf(self.results_tab), _translate("DictionarySearchWindow", "Results"))
        self.rightside_tabs.setTabText(self.rightside_tabs.indexOf(self.links_tab), _translate("DictionarySearchWindow", "Links"))
        self.add_memo_button.setText(_translate("DictionarySearchWindow", "Add"))
        self.clear_memo_button.setText(_translate("DictionarySearchWindow", "Clear"))
        self.remove_memo_button.setText(_translate("DictionarySearchWindow", "Remove"))
        self.label_2.setText(_translate("DictionarySearchWindow", "Front"))
        self.label_5.setText(_translate("DictionarySearchWindow", "Back"))
        self.label_3.setText(_translate("DictionarySearchWindow", "Memos for this page"))
        self.rightside_tabs.setTabText(self.rightside_tabs.indexOf(self.memos_tab), _translate("DictionarySearchWindow", "Memos"))
        self.rightside_tabs.setTabText(self.rightside_tabs.indexOf(self.recent_tab), _translate("DictionarySearchWindow", "Recent"))
        self.menu_File.setTitle(_translate("DictionarySearchWindow", "&File"))
        self.menu_Edit.setTitle(_translate("DictionarySearchWindow", "&Edit"))
        self.menu_Windows.setTitle(_translate("DictionarySearchWindow", "&Windows"))
        self.menu_Help.setTitle(_translate("DictionarySearchWindow", "&Help"))
        self.toolBar.setWindowTitle(_translate("DictionarySearchWindow", "toolBar"))
        self.action_Copy.setText(_translate("DictionarySearchWindow", "&Copy"))
        self.action_Paste.setText(_translate("DictionarySearchWindow", "&Paste"))
        self.action_Quit.setText(_translate("DictionarySearchWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("DictionarySearchWindow", "Ctrl+Q"))
        self.action_Sutta_Search.setText(_translate("DictionarySearchWindow", "&Sutta Search"))
        self.action_Sutta_Search.setShortcut(_translate("DictionarySearchWindow", "F5"))
        self.action_Dictionary_Search.setText(_translate("DictionarySearchWindow", "&Dictionary Search"))
        self.action_Dictionary_Search.setShortcut(_translate("DictionarySearchWindow", "F6"))
        self.action_About.setText(_translate("DictionarySearchWindow", "&About"))
        self.action_Website.setText(_translate("DictionarySearchWindow", "&Website"))
        self.action_Close_Window.setText(_translate("DictionarySearchWindow", "&Close Window"))
        self.action_Open.setText(_translate("DictionarySearchWindow", "&Open..."))
        self.action_Open.setShortcut(_translate("DictionarySearchWindow", "Ctrl+O"))
        self.action_Document_Reader.setText(_translate("DictionarySearchWindow", "D&ocument Reader"))
        self.action_Document_Reader.setToolTip(_translate("DictionarySearchWindow", "Document Reader"))
        self.action_Document_Reader.setShortcut(_translate("DictionarySearchWindow", "F7"))
        self.action_Library.setText(_translate("DictionarySearchWindow", "&Library"))
        self.action_Library.setShortcut(_translate("DictionarySearchWindow", "F8"))
        self.action_Memos.setText(_translate("DictionarySearchWindow", "&Memos"))
        self.action_Memos.setToolTip(_translate("DictionarySearchWindow", "Memos"))
        self.action_Memos.setShortcut(_translate("DictionarySearchWindow", "F9"))
        self.action_Dictionaries_Manager.setText(_translate("DictionarySearchWindow", "Dictionaries &Manager"))
        self.action_Dictionaries_Manager.setShortcut(_translate("DictionarySearchWindow", "F10"))
        self.action_Links.setText(_translate("DictionarySearchWindow", "&Links"))
        self.action_Links.setShortcut(_translate("DictionarySearchWindow", "F11"))
from simsapa.assets import icons_rc
