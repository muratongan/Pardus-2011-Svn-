# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/bug_reporter.ui'
#
# Created: Wed Aug 24 16:20:08 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

import gettext
__trans = gettext.translation('bug-reporting-tool', fallback=True)
i18n = __trans.ugettext
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_BugReporter(object):
    def setupUi(self, BugReporter):
        BugReporter.setObjectName(_fromUtf8("BugReporter"))
        BugReporter.resize(595, 527)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BugReporter.sizePolicy().hasHeightForWidth())
        BugReporter.setSizePolicy(sizePolicy)
        BugReporter.setMaximumSize(QtCore.QSize(595, 527))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../.designer/backup/images/warning.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BugReporter.setWindowIcon(icon)
        BugReporter.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(BugReporter)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 581, 471))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page1 = QtGui.QWidget()
        self.page1.setObjectName(_fromUtf8("page1"))
        self.frameTitlePage1 = QtGui.QFrame(self.page1)
        self.frameTitlePage1.setGeometry(QtCore.QRect(10, 10, 561, 51))
        self.frameTitlePage1.setStyleSheet(_fromUtf8("#frameTitlePage1{\n"
"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"}"))
        self.frameTitlePage1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameTitlePage1.setFrameShadow(QtGui.QFrame.Raised)
        self.frameTitlePage1.setObjectName(_fromUtf8("frameTitlePage1"))
        self.lblTitlePae1 = QtGui.QLabel(self.frameTitlePage1)
        self.lblTitlePae1.setGeometry(QtCore.QRect(50, 10, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblTitlePae1.setFont(font)
        self.lblTitlePae1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitlePae1.setWordWrap(True)
        self.lblTitlePae1.setObjectName(_fromUtf8("lblTitlePae1"))
        self.frameWelcomeMessage = QtGui.QFrame(self.page1)
        self.frameWelcomeMessage.setGeometry(QtCore.QRect(10, 70, 561, 361))
        self.frameWelcomeMessage.setStyleSheet(_fromUtf8("#frameWelcomeMessage{\n"
"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"}"))
        self.frameWelcomeMessage.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameWelcomeMessage.setFrameShadow(QtGui.QFrame.Raised)
        self.frameWelcomeMessage.setObjectName(_fromUtf8("frameWelcomeMessage"))
        self.lblquestionPage1 = QtGui.QLabel(self.frameWelcomeMessage)
        self.lblquestionPage1.setGeometry(QtCore.QRect(20, 20, 521, 331))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblquestionPage1.setFont(font)
        self.lblquestionPage1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblquestionPage1.setWordWrap(True)
        self.lblquestionPage1.setObjectName(_fromUtf8("lblquestionPage1"))
        self.btnNextPage1 = QtGui.QPushButton(self.page1)
        self.btnNextPage1.setGeometry(QtCore.QRect(500, 440, 71, 31))
        self.btnNextPage1.setObjectName(_fromUtf8("btnNextPage1"))
        self.btnCancelPage1 = QtGui.QPushButton(self.page1)
        self.btnCancelPage1.setGeometry(QtCore.QRect(430, 440, 68, 31))
        self.btnCancelPage1.setObjectName(_fromUtf8("btnCancelPage1"))
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtGui.QWidget()
        self.page2.setObjectName(_fromUtf8("page2"))
        self.frameTitlePage2 = QtGui.QFrame(self.page2)
        self.frameTitlePage2.setGeometry(QtCore.QRect(10, 10, 561, 51))
        self.frameTitlePage2.setStyleSheet(_fromUtf8("#frameTitlePage2{\n"
"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"}"))
        self.frameTitlePage2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameTitlePage2.setFrameShadow(QtGui.QFrame.Raised)
        self.frameTitlePage2.setObjectName(_fromUtf8("frameTitlePage2"))
        self.lblTitlePage2 = QtGui.QLabel(self.frameTitlePage2)
        self.lblTitlePage2.setGeometry(QtCore.QRect(50, 10, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblTitlePage2.setFont(font)
        self.lblTitlePage2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitlePage2.setWordWrap(True)
        self.lblTitlePage2.setObjectName(_fromUtf8("lblTitlePage2"))
        self.frameProducts = QtGui.QFrame(self.page2)
        self.frameProducts.setGeometry(QtCore.QRect(10, 70, 561, 361))
        self.frameProducts.setStyleSheet(_fromUtf8("#frameProducts{\n"
"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"}"))
        self.frameProducts.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameProducts.setFrameShadow(QtGui.QFrame.Raised)
        self.frameProducts.setObjectName(_fromUtf8("frameProducts"))
        self.rbDisplay = QtGui.QRadioButton(self.frameProducts)
        self.rbDisplay.setGeometry(QtCore.QRect(20, 60, 521, 21))
        self.rbDisplay.setChecked(True)
        self.rbDisplay.setObjectName(_fromUtf8("rbDisplay"))
        self.lblquestion = QtGui.QLabel(self.frameProducts)
        self.lblquestion.setGeometry(QtCore.QRect(20, 20, 521, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblquestion.setFont(font)
        self.lblquestion.setWordWrap(True)
        self.lblquestion.setObjectName(_fromUtf8("lblquestion"))
        self.rbStorage = QtGui.QRadioButton(self.frameProducts)
        self.rbStorage.setGeometry(QtCore.QRect(20, 100, 521, 21))
        self.rbStorage.setObjectName(_fromUtf8("rbStorage"))
        self.rbSoundAudio = QtGui.QRadioButton(self.frameProducts)
        self.rbSoundAudio.setGeometry(QtCore.QRect(20, 140, 521, 21))
        self.rbSoundAudio.setObjectName(_fromUtf8("rbSoundAudio"))
        self.rbOthers = QtGui.QRadioButton(self.frameProducts)
        self.rbOthers.setGeometry(QtCore.QRect(20, 180, 521, 21))
        self.rbOthers.setObjectName(_fromUtf8("rbOthers"))
        self.btnBackPage2 = QtGui.QPushButton(self.page2)
        self.btnBackPage2.setGeometry(QtCore.QRect(430, 440, 68, 31))
        self.btnBackPage2.setObjectName(_fromUtf8("btnBackPage2"))
        self.btnNextPage2 = QtGui.QPushButton(self.page2)
        self.btnNextPage2.setGeometry(QtCore.QRect(500, 440, 71, 31))
        self.btnNextPage2.setObjectName(_fromUtf8("btnNextPage2"))
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtGui.QWidget()
        self.page3.setObjectName(_fromUtf8("page3"))
        self.frameDetails = QtGui.QFrame(self.page3)
        self.frameDetails.setGeometry(QtCore.QRect(10, 70, 561, 361))
        self.frameDetails.setStyleSheet(_fromUtf8("#frameDetails{\n"
"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"}"))
        self.frameDetails.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameDetails.setFrameShadow(QtGui.QFrame.Raised)
        self.frameDetails.setObjectName(_fromUtf8("frameDetails"))
        self.lblSteps = QtGui.QLabel(self.frameDetails)
        self.lblSteps.setGeometry(QtCore.QRect(40, 220, 71, 16))
        self.lblSteps.setObjectName(_fromUtf8("lblSteps"))
        self.txtSummary = QtGui.QTextEdit(self.frameDetails)
        self.txtSummary.setGeometry(QtCore.QRect(130, 20, 411, 31))
        self.txtSummary.setLineWidth(1)
        self.txtSummary.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.txtSummary.setLineWrapColumnOrWidth(1)
        self.txtSummary.setObjectName(_fromUtf8("txtSummary"))
        self.lblSummary = QtGui.QLabel(self.frameDetails)
        self.lblSummary.setGeometry(QtCore.QRect(40, 30, 71, 16))
        self.lblSummary.setObjectName(_fromUtf8("lblSummary"))
        self.lblDetails = QtGui.QLabel(self.frameDetails)
        self.lblDetails.setGeometry(QtCore.QRect(40, 90, 71, 16))
        self.lblDetails.setObjectName(_fromUtf8("lblDetails"))
        self.txtDetails = QtGui.QTextEdit(self.frameDetails)
        self.txtDetails.setGeometry(QtCore.QRect(130, 60, 411, 121))
        self.txtDetails.setLineWidth(2)
        self.txtDetails.setObjectName(_fromUtf8("txtDetails"))
        self.txtSteps = QtGui.QTextEdit(self.frameDetails)
        self.txtSteps.setGeometry(QtCore.QRect(130, 190, 411, 141))
        self.txtSteps.setLineWidth(2)
        self.txtSteps.setObjectName(_fromUtf8("txtSteps"))
        self.frameTitlePage3 = QtGui.QFrame(self.page3)
        self.frameTitlePage3.setGeometry(QtCore.QRect(10, 10, 561, 51))
        self.frameTitlePage3.setStyleSheet(_fromUtf8("#frameTitlePage3{\n"
"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"}"))
        self.frameTitlePage3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameTitlePage3.setFrameShadow(QtGui.QFrame.Raised)
        self.frameTitlePage3.setObjectName(_fromUtf8("frameTitlePage3"))
        self.lblTitlePage3 = QtGui.QLabel(self.frameTitlePage3)
        self.lblTitlePage3.setGeometry(QtCore.QRect(50, 10, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblTitlePage3.setFont(font)
        self.lblTitlePage3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitlePage3.setWordWrap(True)
        self.lblTitlePage3.setObjectName(_fromUtf8("lblTitlePage3"))
        self.btnBackPage3 = QtGui.QPushButton(self.page3)
        self.btnBackPage3.setGeometry(QtCore.QRect(430, 440, 68, 31))
        self.btnBackPage3.setObjectName(_fromUtf8("btnBackPage3"))
        self.btnNextPage3 = QtGui.QPushButton(self.page3)
        self.btnNextPage3.setGeometry(QtCore.QRect(500, 440, 71, 31))
        self.btnNextPage3.setObjectName(_fromUtf8("btnNextPage3"))
        self.stackedWidget.addWidget(self.page3)
        self.page4 = QtGui.QWidget()
        self.page4.setObjectName(_fromUtf8("page4"))
        self.frameDetailsPage4 = QtGui.QFrame(self.page4)
        self.frameDetailsPage4.setGeometry(QtCore.QRect(10, 70, 561, 361))
        self.frameDetailsPage4.setStyleSheet(_fromUtf8("#frameDetailsPage4{\n"
"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"}"))
        self.frameDetailsPage4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameDetailsPage4.setFrameShadow(QtGui.QFrame.Raised)
        self.frameDetailsPage4.setObjectName(_fromUtf8("frameDetailsPage4"))
        self.gridLayout = QtGui.QGridLayout(self.frameDetailsPage4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.frameDetailsPage4)
        self.treeWidget.setLineWidth(2)
        self.treeWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setAllColumnsShowFocus(True)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.treeWidget.header().setDefaultSectionSize(200)
        self.treeWidget.header().setMinimumSectionSize(50)
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.btnBackPage4 = QtGui.QPushButton(self.page4)
        self.btnBackPage4.setGeometry(QtCore.QRect(430, 440, 68, 31))
        self.btnBackPage4.setObjectName(_fromUtf8("btnBackPage4"))
        self.btnSendPage4 = QtGui.QPushButton(self.page4)
        self.btnSendPage4.setGeometry(QtCore.QRect(500, 440, 71, 31))
        self.btnSendPage4.setObjectName(_fromUtf8("btnSendPage4"))
        self.frameTitlePage4 = QtGui.QFrame(self.page4)
        self.frameTitlePage4.setGeometry(QtCore.QRect(10, 10, 561, 51))
        self.frameTitlePage4.setStyleSheet(_fromUtf8("#frameTitlePage4{\n"
"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"}"))
        self.frameTitlePage4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameTitlePage4.setFrameShadow(QtGui.QFrame.Raised)
        self.frameTitlePage4.setObjectName(_fromUtf8("frameTitlePage4"))
        self.lblTitlePage4 = QtGui.QLabel(self.frameTitlePage4)
        self.lblTitlePage4.setGeometry(QtCore.QRect(50, 10, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblTitlePage4.setFont(font)
        self.lblTitlePage4.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitlePage4.setWordWrap(True)
        self.lblTitlePage4.setObjectName(_fromUtf8("lblTitlePage4"))
        self.stackedWidget.addWidget(self.page4)
        self.page5 = QtGui.QWidget()
        self.page5.setObjectName(_fromUtf8("page5"))
        self.frameTitlePage5 = QtGui.QFrame(self.page5)
        self.frameTitlePage5.setGeometry(QtCore.QRect(10, 10, 561, 51))
        self.frameTitlePage5.setStyleSheet(_fromUtf8("#frameTitlePage5{\n"
"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"}"))
        self.frameTitlePage5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameTitlePage5.setFrameShadow(QtGui.QFrame.Raised)
        self.frameTitlePage5.setObjectName(_fromUtf8("frameTitlePage5"))
        self.lblTitlePage5 = QtGui.QLabel(self.frameTitlePage5)
        self.lblTitlePage5.setGeometry(QtCore.QRect(50, 10, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblTitlePage5.setFont(font)
        self.lblTitlePage5.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitlePage5.setWordWrap(True)
        self.lblTitlePage5.setObjectName(_fromUtf8("lblTitlePage5"))
        self.frameResultPage5 = QtGui.QFrame(self.page5)
        self.frameResultPage5.setGeometry(QtCore.QRect(10, 70, 561, 361))
        self.frameResultPage5.setStyleSheet(_fromUtf8("#frameResultPage5{\n"
"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"}"))
        self.frameResultPage5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameResultPage5.setFrameShadow(QtGui.QFrame.Raised)
        self.frameResultPage5.setObjectName(_fromUtf8("frameResultPage5"))
        self.label = QtGui.QLabel(self.frameResultPage5)
        self.label.setGeometry(QtCore.QRect(20, 30, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frameResultPage5)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 131, 16))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lblBugID = QtGui.QLabel(self.frameResultPage5)
        self.lblBugID.setGeometry(QtCore.QRect(190, 90, 341, 16))
        self.lblBugID.setWordWrap(True)
        self.lblBugID.setObjectName(_fromUtf8("lblBugID"))
        self.label_4 = QtGui.QLabel(self.frameResultPage5)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 131, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lblLinkToBug = QtGui.QLabel(self.frameResultPage5)
        self.lblLinkToBug.setGeometry(QtCore.QRect(190, 130, 351, 41))
        self.lblLinkToBug.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblLinkToBug.setWordWrap(True)
        self.lblLinkToBug.setObjectName(_fromUtf8("lblLinkToBug"))
        self.btnQuitPage5 = QtGui.QPushButton(self.page5)
        self.btnQuitPage5.setGeometry(QtCore.QRect(500, 440, 71, 31))
        self.btnQuitPage5.setObjectName(_fromUtf8("btnQuitPage5"))
        self.stackedWidget.addWidget(self.page5)
        self.page6 = QtGui.QWidget()
        self.page6.setObjectName(_fromUtf8("page6"))
        self.frameTitlePage6 = QtGui.QFrame(self.page6)
        self.frameTitlePage6.setGeometry(QtCore.QRect(10, 10, 561, 51))
        self.frameTitlePage6.setStyleSheet(_fromUtf8("#frameTitlePage6{\n"
"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"}"))
        self.frameTitlePage6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameTitlePage6.setFrameShadow(QtGui.QFrame.Raised)
        self.frameTitlePage6.setObjectName(_fromUtf8("frameTitlePage6"))
        self.lblTitlePage5_2 = QtGui.QLabel(self.frameTitlePage6)
        self.lblTitlePage5_2.setGeometry(QtCore.QRect(50, 10, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblTitlePage5_2.setFont(font)
        self.lblTitlePage5_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitlePage5_2.setWordWrap(True)
        self.lblTitlePage5_2.setObjectName(_fromUtf8("lblTitlePage5_2"))
        self.frameResultPage6 = QtGui.QFrame(self.page6)
        self.frameResultPage6.setGeometry(QtCore.QRect(10, 70, 561, 361))
        self.frameResultPage6.setStyleSheet(_fromUtf8("#frameResultPage6{\n"
"border: 3px solid gray;\n"
"border-radius: 10px;\n"
"}"))
        self.frameResultPage6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameResultPage6.setFrameShadow(QtGui.QFrame.Raised)
        self.frameResultPage6.setObjectName(_fromUtf8("frameResultPage6"))
        self.label_6 = QtGui.QLabel(self.frameResultPage6)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.frameResultPage6)
        self.label_7.setGeometry(QtCore.QRect(20, 120, 131, 16))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(self.frameResultPage6)
        self.label_9.setGeometry(QtCore.QRect(20, 160, 131, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.txtMail = QtGui.QTextEdit(self.frameResultPage6)
        self.txtMail.setGeometry(QtCore.QRect(150, 110, 251, 31))
        self.txtMail.setObjectName(_fromUtf8("txtMail"))
        self.txtPassword = QtGui.QTextEdit(self.frameResultPage6)
        self.txtPassword.setGeometry(QtCore.QRect(150, 150, 251, 31))
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.btnLogin = QtGui.QPushButton(self.frameResultPage6)
        self.btnLogin.setGeometry(QtCore.QRect(300, 200, 99, 31))
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.btnQuitPage6 = QtGui.QPushButton(self.page6)
        self.btnQuitPage6.setGeometry(QtCore.QRect(500, 440, 71, 31))
        self.btnQuitPage6.setObjectName(_fromUtf8("btnQuitPage6"))
        self.btnBackPage6 = QtGui.QPushButton(self.page6)
        self.btnBackPage6.setGeometry(QtCore.QRect(420, 440, 71, 31))
        self.btnBackPage6.setObjectName(_fromUtf8("btnBackPage6"))
        self.stackedWidget.addWidget(self.page6)
        BugReporter.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BugReporter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        BugReporter.setMenuBar(self.menubar)

        self.retranslateUi(BugReporter)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BugReporter)

    def retranslateUi(self, BugReporter):
        BugReporter.setWindowTitle(i18n("Bug Reporter"))
        self.lblTitlePae1.setText(i18n("Pardus Bug Reporting Tool"))
        self.lblquestionPage1.setText(i18n("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wellcome to Pardus Bug Reporting Tool. This tool allows you to enter bugs that you have encountered in your Pardus system.</p></body></html>"))
        self.btnNextPage1.setText(i18n("Next"))
        self.btnCancelPage1.setText(i18n("Cancel"))
        self.lblTitlePage2.setText(i18n("Pardus Bug Reporting Tool"))
        self.rbDisplay.setText(i18n("Display"))
        self.lblquestion.setText(i18n("Select the type of the problem you have encountered. "))
        self.rbStorage.setText(i18n("Storage"))
        self.rbSoundAudio.setText(i18n("Sound / Audio"))
        self.rbOthers.setText(i18n("Others"))
        self.btnBackPage2.setText(i18n("Back"))
        self.btnNextPage2.setText(i18n("Next"))
        self.lblSteps.setText(i18n("Steps"))
        self.txtSummary.setToolTip(i18n("A short summary that describes the bug you have entered..."))
        self.lblSummary.setText(i18n("Summary"))
        self.lblDetails.setText(i18n("Details"))
        self.txtDetails.setToolTip(i18n("Detailed description of the bug you have encountered..."))
        self.txtSteps.setToolTip(i18n("Steps that explains how you have encountered the bug. Please make sure that you entered all necessary steps one by one to help devolopers fix the problem..."))
        self.txtSteps.setHtml(i18n("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.lblTitlePage3.setText(i18n("Pardus Bug Reporting Tool"))
        self.btnBackPage3.setText(i18n("Back"))
        self.btnNextPage3.setText(i18n("Next"))
        self.treeWidget.headerItem().setText(0, i18n("Fields"))
        self.treeWidget.headerItem().setText(1, i18n("Data"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, i18n("Architecture"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, i18n("OS"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, i18n("Kernel"))
        self.treeWidget.topLevelItem(1).setText(0, i18n("User Data"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, i18n("Problem Type"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, i18n("Summary"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, i18n("Description"))
        self.treeWidget.topLevelItem(2).setText(0, i18n("System Data"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, i18n("Commands"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, i18n("Log Files"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.btnBackPage4.setText(i18n("Back"))
        self.btnSendPage4.setText(i18n("Send"))
        self.lblTitlePage4.setText(i18n("Pardus Bug Reporting Tool"))
        self.lblTitlePage5.setText(i18n("Pardus Bug Reporting Tool"))
        self.label.setText(i18n("Your bug details has been sent to Pardus devolopers. Bug details are as following"))
        self.label_2.setText(i18n("Bug ID"))
        self.lblBugID.setText(i18n("ID"))
        self.label_4.setText(i18n("Link to Bug"))
        self.lblLinkToBug.setText(i18n("ID"))
        self.btnQuitPage5.setText(i18n("Quit"))
        self.lblTitlePage5_2.setText(i18n("Pardus Bug Reporting Tool"))
        self.label_6.setText(i18n("You need to log in to send this bug entry. Please login to bugzilla by using your e-mail and password"))
        self.label_7.setText(i18n("E-Mail"))
        self.label_9.setText(i18n("Password"))
        self.btnLogin.setText(i18n("Login"))
        self.btnQuitPage6.setText(i18n("Quit"))
        self.btnBackPage6.setText(i18n("Back"))

