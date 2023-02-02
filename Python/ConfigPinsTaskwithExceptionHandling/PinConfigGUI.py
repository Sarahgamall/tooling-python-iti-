# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfigPinsGui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from lxml import etree as ET
import sys
import os
from xml.dom.minidom import parseString
import xmltodict
import io
from PIL import Image, ImageCms


#import guiResources_rc

class Ui_Form(object):
    PortA_Pins_Cfg = {}
    PortB_Pins_Cfg = {}
    PortC_Pins_Cfg = {}
    PortD_Pins_Cfg = {}
    
    
    Loaded_Pins_Dict = {}
    PortA=[]
    PortB=[]
    PortC=[]
    PortD=[]
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1028, 799)
        Form.setStyleSheet(u"")
        self.tab = QTabWidget(Form)
        self.tab.setObjectName(u"tab")
        self.tab.setGeometry(QRect(0, 180, 1031, 611))
        self.tab.setStyleSheet(u"")
        self.PORTA = QWidget()
        self.PORTA.setObjectName(u"PORTA")
        self.PinChoice = QGroupBox(self.PORTA)
        self.PinChoice.setObjectName(u"PinChoice")
        self.PinChoice.setGeometry(QRect(20, 20, 371, 141))
        self.PinChoice.setStyleSheet(u"\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBoxPortA = QComboBox(self.PinChoice)
        self.comboBoxPortA.addItem("")
        self.comboBoxPortA.addItem("")
        self.comboBoxPortA.addItem("")
        self.comboBoxPortA.addItem("")
        self.comboBoxPortA.addItem("")
        self.comboBoxPortA.addItem("")
        self.comboBoxPortA.addItem("")
        self.comboBoxPortA.addItem("")
        self.comboBoxPortA.addItem("")
       
        self.comboBoxPortA.setObjectName(u"comboBoxPortA")
        self.comboBoxPortA.setGeometry(QRect(10, 70, 200, 31))
        self.comboBoxPortA.setStyleSheet(u"")
        self.PinlabelPortA = QLabel(self.PinChoice)
        self.PinlabelPortA.setObjectName(u"PinlabelPortA")
        self.PinlabelPortA.setGeometry(QRect(20, 25, 121, 31))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.PinlabelPortA.setFont(font)
        self.PinlabelPortA.setMargin(5)
        self.PinlabelPortA.setIndent(5)
        self.Input_ConfigPortA = QGroupBox(self.PORTA)
        self.Input_ConfigPortA.setObjectName(u"Input_ConfigPortA")
        self.Input_ConfigPortA.setEnabled(False)
        self.Input_ConfigPortA.setGeometry(QRect(350, 370, 351, 111))
        self.Input_ConfigPortA.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pull_upRadioPortA = QRadioButton(self.Input_ConfigPortA)
        self.pull_upRadioPortA.setObjectName(u"pull_upRadioPortA")
        self.pull_upRadioPortA.setGeometry(QRect(40, 40, 95, 20))
        self.High_impRadioPortA = QRadioButton(self.Input_ConfigPortA)
        self.High_impRadioPortA.setObjectName(u"High_impRadioPortA")
        self.High_impRadioPortA.setGeometry(QRect(200, 40, 95, 20))
        self.Output_configPortA = QGroupBox(self.PORTA)
        self.Output_configPortA.setObjectName(u"Output_configPortA")
        self.Output_configPortA.setGeometry(QRect(360, 210, 321, 91))
        self.Output_configPortA.setStyleSheet(u"selection-background-color: rgb(181, 181, 181);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.HighRadioPortA = QRadioButton(self.Output_configPortA)
        self.HighRadioPortA.setObjectName(u"HighRadioPortA")
        self.HighRadioPortA.setGeometry(QRect(20, 40, 95, 20))
        self.LowRadioPortA = QRadioButton(self.Output_configPortA)
        self.LowRadioPortA.setObjectName(u"LowRadioPortA")
        self.LowRadioPortA.setGeometry(QRect(180, 40, 95, 20))
        self.PinDirectionAGroup = QGroupBox(self.PORTA)
        self.PinDirectionAGroup.setObjectName(u"PinDirectionAGroup")
        self.PinDirectionAGroup.setGeometry(QRect(10, 190, 301, 311))
        self.PinDirectionAGroup.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.outputARadio = QRadioButton(self.PinDirectionAGroup)
        self.outputARadio.setObjectName(u"outputARadio")
        self.outputARadio.setGeometry(QRect(30, 60, 95, 20))
        self.outputARadio.setChecked(True)
        self.inputARadio = QRadioButton(self.PinDirectionAGroup)
        self.inputARadio.setObjectName(u"inputARadio")
        self.inputARadio.setGeometry(QRect(30, 130, 95, 20))
        self.PinCfgPortA = QPushButton(self.PORTA)
        self.PinCfgPortA.setObjectName(u"PinCfgPortA")
        self.PinCfgPortA.setGeometry(QRect(500, 90, 321, 31))
        self.PinCfgPortA.setStyleSheet(u"")
        self.graphicsView = QGraphicsView(self.PORTA)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(-600, -60, 1621, 651))
        self.convert_to_srgb("C:/Users/sarah/Desktop/PythonGui/mcu6.webp")
        self.graphicsView.setStyleSheet(u"background-image: url(C:/Users/sarah/Desktop/PythonGui/mcu6.webp);")
        self.tab.addTab(self.PORTA, "")
        self.graphicsView.raise_()
        self.PinChoice.raise_()
        self.Input_ConfigPortA.raise_()
        self.Output_configPortA.raise_()
        self.PinDirectionAGroup.raise_()
        self.PinCfgPortA.raise_()
        self.PORTB = QWidget()
        self.PORTB.setObjectName(u"PORTB")
        self.groupBox_2 = QGroupBox(self.PORTB)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 20, 371, 141))
        self.groupBox_2.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBoxPortB = QComboBox(self.groupBox_2)
        self.comboBoxPortB.addItem("")
        self.comboBoxPortB.addItem("")
        self.comboBoxPortB.addItem("")
        self.comboBoxPortB.addItem("")
        self.comboBoxPortB.addItem("")
        self.comboBoxPortB.addItem("")
        self.comboBoxPortB.addItem("")
        self.comboBoxPortB.addItem("")
        self.comboBoxPortB.addItem("")
       
        self.comboBoxPortB.setObjectName(u"comboBoxPortB")
        self.comboBoxPortB.setGeometry(QRect(10, 70, 200, 31))
        self.PinlabelPortB = QLabel(self.groupBox_2)
        self.PinlabelPortB.setObjectName(u"PinlabelPortB")
        self.PinlabelPortB.setGeometry(QRect(20, 25, 121, 31))
        self.PinlabelPortB.setFont(font)
        self.PinlabelPortB.setMargin(5)
        self.PinlabelPortB.setIndent(5)
        self.Input_ConfigPortB = QGroupBox(self.PORTB)
        self.Input_ConfigPortB.setObjectName(u"Input_ConfigPortB")
        self.Input_ConfigPortB.setEnabled(False)
        self.Input_ConfigPortB.setGeometry(QRect(350, 370, 351, 111))
        self.Input_ConfigPortB.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pull_upRadioPortB = QRadioButton(self.Input_ConfigPortB)
        self.pull_upRadioPortB.setObjectName(u"pull_upRadioPortB")
        self.pull_upRadioPortB.setGeometry(QRect(40, 40, 95, 20))
        self.High_impRadioPortB = QRadioButton(self.Input_ConfigPortB)
        self.High_impRadioPortB.setObjectName(u"High_impRadioPortB")
        self.High_impRadioPortB.setGeometry(QRect(200, 40, 95, 20))
        self.Output_configPortB = QGroupBox(self.PORTB)
        self.Output_configPortB.setObjectName(u"Output_configPortB")
        self.Output_configPortB.setGeometry(QRect(360, 210, 321, 91))
        self.Output_configPortB.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.HighRadioPortB = QRadioButton(self.Output_configPortB)
        self.HighRadioPortB.setObjectName(u"HighRadioPortB")
        self.HighRadioPortB.setGeometry(QRect(20, 40, 95, 20))
        self.LowRadioPortB = QRadioButton(self.Output_configPortB)
        self.LowRadioPortB.setObjectName(u"LowRadioPortB")
        self.LowRadioPortB.setGeometry(QRect(180, 40, 95, 20))
        self.PinDirectionBGroup = QGroupBox(self.PORTB)
        self.PinDirectionBGroup.setObjectName(u"PinDirectionBGroup")
        self.PinDirectionBGroup.setGeometry(QRect(10, 190, 301, 311))
        self.PinDirectionBGroup.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.outputBRadio = QRadioButton(self.PinDirectionBGroup)
        self.outputBRadio.setObjectName(u"outputBRadio")
        self.outputBRadio.setGeometry(QRect(30, 60, 95, 20))
        self.outputBRadio.setChecked(True)
        self.inputBRadio = QRadioButton(self.PinDirectionBGroup)
        self.inputBRadio.setObjectName(u"inputBRadio")
        self.inputBRadio.setGeometry(QRect(30, 130, 95, 20))
        self.graphicsView_2 = QGraphicsView(self.PORTB)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(-600, -60, 2751, 1201))
        self.graphicsView_2.setStyleSheet(u"background-image: url(C:/Users/sarah/Desktop/PythonGui/mcu6.webp);")
        self.PinCfgPortB = QPushButton(self.PORTB)
        self.PinCfgPortB.setObjectName(u"PinCfgPortB")
        self.PinCfgPortB.setGeometry(QRect(500, 90, 321, 31))
        self.PinCfgPortB.setStyleSheet(u"")
        self.tab.addTab(self.PORTB, "")
        self.graphicsView_2.raise_()
        self.groupBox_2.raise_()
        self.Input_ConfigPortB.raise_()
        self.Output_configPortB.raise_()
        self.PinDirectionBGroup.raise_()
        self.PinCfgPortB.raise_()
        self.PORTC = QWidget()
        self.PORTC.setObjectName(u"PORTC")
        self.groupBox_3 = QGroupBox(self.PORTC)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 20, 371, 141))
        self.groupBox_3.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBoxPortC = QComboBox(self.groupBox_3)
        self.comboBoxPortC.addItem("")
        self.comboBoxPortC.addItem("")
        self.comboBoxPortC.addItem("")
        self.comboBoxPortC.addItem("")
        self.comboBoxPortC.addItem("")
        self.comboBoxPortC.addItem("")
        self.comboBoxPortC.addItem("")
        self.comboBoxPortC.addItem("")
        self.comboBoxPortC.addItem("")
        
        self.comboBoxPortC.setObjectName(u"comboBoxPortC")
        self.comboBoxPortC.setGeometry(QRect(10, 70, 200, 31))
        self.comboBoxPortC.setStyleSheet(u"")
        self.PinlabelPortC = QLabel(self.groupBox_3)
        self.PinlabelPortC.setObjectName(u"PinlabelPortC")
        self.PinlabelPortC.setGeometry(QRect(20, 25, 121, 31))
        self.PinlabelPortC.setFont(font)
        self.PinlabelPortC.setMargin(5)
        self.PinlabelPortC.setIndent(5)
        self.Input_ConfigPortC = QGroupBox(self.PORTC)
        self.Input_ConfigPortC.setObjectName(u"Input_ConfigPortC")
        self.Input_ConfigPortC.setEnabled(False)
        self.Input_ConfigPortC.setGeometry(QRect(350, 370, 351, 111))
        self.Input_ConfigPortC.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pull_upRadioPortC = QRadioButton(self.Input_ConfigPortC)
        self.pull_upRadioPortC.setObjectName(u"pull_upRadioPortC")
        self.pull_upRadioPortC.setGeometry(QRect(40, 40, 95, 20))
        self.High_impRadioPortC = QRadioButton(self.Input_ConfigPortC)
        self.High_impRadioPortC.setObjectName(u"High_impRadioPortC")
        self.High_impRadioPortC.setGeometry(QRect(200, 40, 95, 20))
        self.Output_configPortC = QGroupBox(self.PORTC)
        self.Output_configPortC.setObjectName(u"Output_configPortC")
        self.Output_configPortC.setGeometry(QRect(360, 210, 321, 91))
        self.Output_configPortC.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.HighRadioPortC = QRadioButton(self.Output_configPortC)
        self.HighRadioPortC.setObjectName(u"HighRadioPortC")
        self.HighRadioPortC.setGeometry(QRect(20, 40, 95, 20))
        self.LowRadioPortC = QRadioButton(self.Output_configPortC)
        self.LowRadioPortC.setObjectName(u"LowRadioPortC")
        self.LowRadioPortC.setGeometry(QRect(180, 40, 95, 20))
        self.PinDirectionCGroup = QGroupBox(self.PORTC)
        self.PinDirectionCGroup.setObjectName(u"PinDirectionCGroup")
        self.PinDirectionCGroup.setGeometry(QRect(10, 190, 301, 311))
        self.PinDirectionCGroup.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.outputCRadio = QRadioButton(self.PinDirectionCGroup)
        self.outputCRadio.setObjectName(u"outputCRadio")
        self.outputCRadio.setGeometry(QRect(30, 60, 95, 20))
        self.outputCRadio.setChecked(True)
        self.inputCRadio = QRadioButton(self.PinDirectionCGroup)
        self.inputCRadio.setObjectName(u"inputCRadio")
        self.inputCRadio.setGeometry(QRect(30, 130, 95, 20))
        self.PinCfgPortC = QPushButton(self.PORTC)
        self.PinCfgPortC.setObjectName(u"PinCfgPortC")
        self.PinCfgPortC.setGeometry(QRect(500, 90, 321, 31))
        self.PinCfgPortC.setStyleSheet(u"")
        self.graphicsView_3 = QGraphicsView(self.PORTC)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setGeometry(QRect(-600, -60, 2691, 871))
        self.graphicsView_3.setStyleSheet(u"background-image: url(C:/Users/sarah/Desktop/PythonGui/mcu6.webp);")
        self.tab.addTab(self.PORTC, "")
        self.graphicsView_3.raise_()
        self.groupBox_3.raise_()
        self.Input_ConfigPortC.raise_()
        self.Output_configPortC.raise_()
        self.PinDirectionCGroup.raise_()
        self.PinCfgPortC.raise_()
        self.PORTD = QWidget()
        self.PORTD.setObjectName(u"PORTD")
        self.groupBox_4 = QGroupBox(self.PORTD)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 20, 371, 141))
        self.groupBox_4.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBoxPortD = QComboBox(self.groupBox_4)
        self.comboBoxPortD.addItem("")
        self.comboBoxPortD.addItem("")
        self.comboBoxPortD.addItem("")
        self.comboBoxPortD.addItem("")
        self.comboBoxPortD.addItem("")
        self.comboBoxPortD.addItem("")
        self.comboBoxPortD.addItem("")
        self.comboBoxPortD.addItem("")
        self.comboBoxPortD.addItem("")
        
        self.comboBoxPortD.setObjectName(u"comboBoxPortD")
        self.comboBoxPortD.setGeometry(QRect(10, 70, 200, 31))
        self.PinlabelPortD = QLabel(self.groupBox_4)
        self.PinlabelPortD.setObjectName(u"PinlabelPortD")
        self.PinlabelPortD.setGeometry(QRect(20, 25, 121, 31))
        self.PinlabelPortD.setFont(font)
        self.PinlabelPortD.setMargin(5)
        self.PinlabelPortD.setIndent(5)
        self.Input_ConfigPortD = QGroupBox(self.PORTD)
        self.Input_ConfigPortD.setObjectName(u"Input_ConfigPortD")
        self.Input_ConfigPortD.setEnabled(False)
        self.Input_ConfigPortD.setGeometry(QRect(350, 370, 351, 111))
        self.Input_ConfigPortD.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pull_upRadioPortD = QRadioButton(self.Input_ConfigPortD)
        self.pull_upRadioPortD.setObjectName(u"pull_upRadioPortD")
        self.pull_upRadioPortD.setGeometry(QRect(40, 40, 95, 20))
        self.High_impRadioPortD = QRadioButton(self.Input_ConfigPortD)
        self.High_impRadioPortD.setObjectName(u"High_impRadioPortD")
        self.High_impRadioPortD.setGeometry(QRect(200, 40, 95, 20))
        self.Output_configPortD = QGroupBox(self.PORTD)
        self.Output_configPortD.setObjectName(u"Output_configPortD")
        self.Output_configPortD.setGeometry(QRect(360, 210, 321, 91))
        self.Output_configPortD.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.HighRadioPortD = QRadioButton(self.Output_configPortD)
        self.HighRadioPortD.setObjectName(u"HighRadioPortD")
        self.HighRadioPortD.setGeometry(QRect(20, 40, 95, 20))
        self.LowRadioPortD = QRadioButton(self.Output_configPortD)
        self.LowRadioPortD.setObjectName(u"LowRadioPortD")
        self.LowRadioPortD.setGeometry(QRect(180, 40, 95, 20))
        self.PinDirectionDGroup = QGroupBox(self.PORTD)
        self.PinDirectionDGroup.setObjectName(u"PinDirectionDGroup")
        self.PinDirectionDGroup.setGeometry(QRect(10, 190, 301, 311))
        self.PinDirectionDGroup.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.outputDRadio = QRadioButton(self.PinDirectionDGroup)
        self.outputDRadio.setObjectName(u"outputDRadio")
        self.outputDRadio.setGeometry(QRect(30, 60, 95, 20))
        self.outputDRadio.setChecked(True)
        self.inputDRadio = QRadioButton(self.PinDirectionDGroup)
        self.inputDRadio.setObjectName(u"inputDRadio")
        self.inputDRadio.setGeometry(QRect(30, 130, 95, 20))
        self.PinCfgPortD = QPushButton(self.PORTD)
        self.PinCfgPortD.setObjectName(u"PinCfgPortD")
        self.PinCfgPortD.setGeometry(QRect(500, 90, 321, 31))
        self.PinCfgPortD.setStyleSheet(u"")
        self.graphicsView_4 = QGraphicsView(self.PORTD)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setGeometry(QRect(-600, -60, 2301, 921))
        self.graphicsView_4.setStyleSheet(u"background-image: url(C:/Users/sarah/Desktop/PythonGui/mcu6.webp);")
        self.tab.addTab(self.PORTD, "")
        self.graphicsView_4.raise_()
        self.groupBox_4.raise_()
        self.Input_ConfigPortD.raise_()
        self.Output_configPortD.raise_()
        self.PinDirectionDGroup.raise_()
        self.PinCfgPortD.raise_()
        self.SaveCfg = QPushButton(Form)
        self.SaveCfg.setObjectName(u"SaveCfg")
        self.SaveCfg.setGeometry(QRect(570, 120, 141, 41))
        self.LoadCfg = QPushButton(Form)
        self.LoadCfg.setObjectName(u"LoadCfg")
        self.LoadCfg.setGeometry(QRect(750, 120, 121, 41))
        self.filePath = QLineEdit(Form)
        self.filePath.setObjectName(u"filePath")
        self.filePath.setGeometry(QRect(30, 40, 591, 31))
        self.GenerateButton = QPushButton(Form)
        self.GenerateButton.setObjectName(u"GenerateButton")
        self.GenerateButton.setGeometry(QRect(640, 40, 93, 28))
        self.outPathLabel = QLabel(Form)
        self.outPathLabel.setObjectName(u"outPathLabel")
        self.outPathLabel.setGeometry(QRect(30, 0, 181, 41))
        self.outPathLabel.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.ClearButton = QPushButton(Form)
        self.ClearButton.setObjectName(u"ClearButton")
        self.ClearButton.setGeometry(QRect(740, 40, 93, 28))
        self.filetoXml = QLineEdit(Form)
        self.filetoXml.setObjectName(u"filetoXml")
        self.filetoXml.setGeometry(QRect(20, 120, 521, 31))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 95, 161, 21))
        self.label.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.LoadingCfg = QCheckBox(Form)
        self.LoadingCfg.setObjectName(u"LoadingCfg")
        self.LoadingCfg.setGeometry(QRect(780, 170, 201, 20))
        self.retranslateUi(Form)
        self.ClearButton.clicked.connect(self.filePath.clear)
        self.GenerateButton.clicked.connect(self.generateFunction)
        QObject.connect(self.outputARadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortA.setDisabled)
        QObject.connect(self.outputARadio,SIGNAL("clicked(bool)"),self.Output_configPortA.setEnabled)
        QObject.connect(self.inputARadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortA.setEnabled)
        QObject.connect(self.inputARadio,SIGNAL("clicked(bool)"),self.Output_configPortA.setDisabled)
        
        QObject.connect(self.outputBRadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortB.setDisabled)
        QObject.connect(self.outputBRadio,SIGNAL("clicked(bool)"),self.Output_configPortB.setEnabled)
        QObject.connect(self.inputBRadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortB.setEnabled)
        QObject.connect(self.inputBRadio,SIGNAL("clicked(bool)"),self.Output_configPortB.setDisabled)
        
        QObject.connect(self.outputCRadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortC.setDisabled)
        QObject.connect(self.outputCRadio,SIGNAL("clicked(bool)"),self.Output_configPortC.setEnabled)
        QObject.connect(self.inputCRadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortC.setEnabled)
        QObject.connect(self.inputCRadio,SIGNAL("clicked(bool)"),self.Output_configPortC.setDisabled)
        
        QObject.connect(self.outputDRadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortD.setDisabled)
        QObject.connect(self.outputDRadio,SIGNAL("clicked(bool)"),self.Output_configPortD.setEnabled)
        QObject.connect(self.inputDRadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortD.setEnabled)
        QObject.connect(self.inputDRadio,SIGNAL("clicked(bool)"),self.Output_configPortD.setDisabled)
        self.SaveCfg.clicked.connect(self.SaveFunction)
        self.LoadCfg.clicked.connect(self.LoadFunction)
        self.LoadCfg.released.connect(self.filetoXml.clear)
        self.SaveCfg.released.connect(self.filetoXml.clear)
        self.PinCfgPortA.clicked.connect(self.AddPinCfgFunction)
        self.PinCfgPortB.clicked.connect(self.AddPinCfgFunction)
        self.PinCfgPortC.clicked.connect(self.AddPinCfgFunction)
        self.PinCfgPortD.clicked.connect(self.AddPinCfgFunction)
        #if(self.LoadingCfg.isChecked()!= True):
        self.comboBoxPortA.currentTextChanged.connect(self.ComboBox_PinChoice)
        self.comboBoxPortB.currentTextChanged.connect(self.ComboBox_PinChoice)
        self.comboBoxPortC.currentTextChanged.connect(self.ComboBox_PinChoice)
        self.comboBoxPortD.currentTextChanged.connect(self.ComboBox_PinChoice)
        
        Group_list=[self.PinDirectionAGroup,self.Output_configPortA,self.Input_ConfigPortA,self.PinDirectionBGroup,self.Output_configPortB,self.Input_ConfigPortB,self.PinDirectionCGroup,self.Output_configPortC,self.Input_ConfigPortC,self.PinDirectionDGroup,self.Output_configPortD,self.Input_ConfigPortD]
        for group in Group_list:
                for radioButton in group.findChildren(QRadioButton):
                    radioButton.clicked.connect(self.DisablePreSaved)
         
        self.tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def convert_to_srgb(self,file_path):
        '''Convert PIL image to sRGB color space (if possible)'''
        img = Image.open(file_path)
        icc = img.info.get('icc_profile', '')
        if icc:
            io_handle = io.BytesIO(icc)     # virtual file
            src_profile = ImageCms.ImageCmsProfile(io_handle)
            dst_profile = ImageCms.createProfile('sRGB')
            img_conv = ImageCms.profileToProfile(img, src_profile, dst_profile)
            icc_conv = img_conv.info.get('icc_profile','')
        if icc != icc_conv:
            # ICC profile was changed -> save converted file
            img_conv.save(file_path,
                        format = 'JPEG',
                        quality = 50,
                        icc_profile = icc_conv)
    
    def DisablePreSaved(self):
        self.LoadingCfg.setChecked(False)
    
    
    def LoadFunction(self):
        
        # path = self.lineEdit_load.text()+r'\DIO_Cfg.xml'
        # tree = ET.parse(path)
        # DIO=tree.getroot()
        #Pins=[PIN0,PIN1,PIN2,PIN3,PIN4,PIN5,PIN6,PIN7]
        Group_list=[self.PinDirectionAGroup,self.Output_configPortA,self.Input_ConfigPortA,self.PinDirectionBGroup,self.Output_configPortB,self.Input_ConfigPortB,self.PinDirectionCGroup,self.Output_configPortC,self.Input_ConfigPortC,self.PinDirectionDGroup,self.Output_configPortD,self.Input_ConfigPortD]
        for group in Group_list:
                group.setEnabled(True)
                for radioButton in group.findChildren(QRadioButton):
                    radioButton.setAutoExclusive(False)
                    radioButton.setChecked(False)
                    radioButton.setAutoExclusive(True)
       
        self.LoadingCfg.setChecked(True)
        #try:
        Output_Path = self.filetoXml.text()+r'DIO_Cfg.xml'
        with open(Output_Path, 'r', encoding='utf-8') as file:
            my_xml = file.read()  
        my_xml_dict = xmltodict.parse(my_xml)
       # print(my_xml_dict)
        Pin_Config_Dict = {}
        for key,item in my_xml_dict.items():
            for sub_key,value in item.items():
                if sub_key=='PORTA':
                    self.PortA = value
                elif sub_key=='PORTB':
                    self.PortB = value 
                elif sub_key=='PORTC':
                    self.PortC = value 
                elif sub_key=='PORTD':
                    self.PortD = value 
  
        if self.comboBoxPortA.currentText().upper() in self.PortA.keys():  
            
            Group_list=[self.PinDirectionAGroup,self.Output_configPortA,self.Input_ConfigPortA]
            for group in Group_list:
                
                for radioButton in group.findChildren(QRadioButton):
                    Rad_Name= str(radioButton.text().upper())
                   
                    Pin_Name=self.comboBoxPortA.currentText().upper()
                    
                  
                    if Rad_Name in self.PortA[Pin_Name].values():
                       
                        radioButton.setChecked(True) 
        if self.comboBoxPortB.currentText().upper() in self.PortB.keys(): 
            Group_list=[self.PinDirectionBGroup,self.Output_configPortB,self.Input_ConfigPortB]
            for group in Group_list:
                for radioButton in group.findChildren(QRadioButton):
                    Rad_Name= radioButton.text().upper()
                    Pin_Name=self.comboBoxPortB.currentText().upper()
                    if Rad_Name in self.PortB[Pin_Name].values():
                        radioButton.setChecked(True) 
        if self.comboBoxPortC.currentText().upper() in self.PortC.keys():  
            Group_list=[self.PinDirectionCGroup,self.Output_configPortC,self.Input_ConfigPortC]
            for group in Group_list:
                for radioButton in group.findChildren(QRadioButton):
                    Rad_Name= radioButton.text().upper()
                    Pin_Name=self.comboBoxPortC.currentText().upper()
                    if Rad_Name in self.PortC[Pin_Name].values():
                        radioButton.setChecked(True) 
        if self.comboBoxPortD.currentText().upper() in self.PortD.values():  
            Group_list=[self.PinDirectionDGroup,self.Output_configPortD,self.Input_ConfigPortD]
            for group in Group_list:
                for radioButton in group.findChildren(QRadioButton):
                    Rad_Name= radioButton.text().upper()
                    Pin_Name=self.comboBoxPortD.currentText().upper()
                    if Rad_Name in self.PortD[Pin_Name].values():
                        radioButton.setChecked(True) 
       
        # except IOError:
            # sys.stderr.write('problem reading:' + Output_Path)
        
    def SaveFunction(self):
        
        PinsA_tags = []
        PinsA_dir_tags = []
        PinsA_cfg_tags = []
        DIO = ET.Element("DIO")
        #PortA
        PORTA = ET.Element("PORTA")
        PORTA_PIN0 = ET.Element("PIN0")
        PinsA_tags.append(PORTA_PIN0)
        PORTA_PIN1 = ET.Element("PIN1")
        PinsA_tags.append(PORTA_PIN1)
        PORTA_PIN2 = ET.Element("PIN2")
        PinsA_tags.append(PORTA_PIN2)
        PORTA_PIN3 = ET.Element("PIN3")
        PORTA_PIN4 = ET.Element("PIN4")
        PORTA_PIN5 = ET.Element("PIN5")
        PORTA_PIN6 = ET.Element("PIN6")
        PORTA_PIN7 = ET.Element("PIN7")
        
        # PinsA_tags.append(PORTA_PIN3)
        # PinsA_tags.append(PORTA_PIN4)
        # PinsA_tags.append(PORTA_PIN5)
        # PinsA_tags.append(PORTA_PIN6)
        # PinsA_tags.append(PORTA_PIN7)
        
        PORTA_PIN0_DIR = ET.Element("DIR")
        PORTA_PIN0_CONFIG = ET.Element("CONFIG")
        PORTA_PIN1_DIR = ET.Element("DIR")
        PORTA_PIN1_CONFIG = ET.Element("CONFIG")
        PORTA_PIN2_DIR = ET.Element("DIR")
        PORTA_PIN2_CONFIG = ET.Element("CONFIG")
        PORTA_PIN3_DIR = ET.Element("DIR")
        PORTA_PIN3_CONFIG = ET.Element("CONFIG")
        PORTA_PIN4_DIR = ET.Element("DIR")
        PORTA_PIN4_CONFIG = ET.Element("CONFIG")
        PORTA_PIN5_DIR = ET.Element("DIR")
        PORTA_PIN5_CONFIG = ET.Element("CONFIG")
        PORTA_PIN6_DIR = ET.Element("DIR")
        PORTA_PIN6_CONFIG = ET.Element("CONFIG")
        PORTA_PIN7_DIR = ET.Element("DIR")
        PORTA_PIN7_CONFIG = ET.Element("CONFIG") 
        
        # PinsA_dir_tags.append(PORTA_PIN0_DIR)
        # PinsA_dir_tags.append(PORTA_PIN1_DIR)
        # PinsA_dir_tags.append(PORTA_PIN2_DIR)
        # PinsA_dir_tags.append(PORTA_PIN3_DIR)
        # PinsA_dir_tags.append(PORTA_PIN4_DIR)
        # PinsA_dir_tags.append(PORTA_PIN5_DIR)
        # PinsA_dir_tags.append(PORTA_PIN6_DIR)
        # PinsA_dir_tags.append(PORTA_PIN7_DIR)
        
        for pin in self.PortA_Pins_Cfg.keys():
            if(len(self.PortA_Pins_Cfg[pin])>1):
                if pin == 'Pin0':
                    PORTA_PIN0_DIR.text =self.PortA_Pins_Cfg[pin][0]
                    PORTA_PIN0_CONFIG.text =self.PortA_Pins_Cfg[pin][1]
                elif pin =='Pin1':
                    PORTA_PIN1_DIR.text =self.PortA_Pins_Cfg[pin][0]
                    PORTA_PIN1_CONFIG.text =self.PortA_Pins_Cfg[pin][1]
                elif pin =='Pin2':
                    PORTA_PIN2_DIR.text =self.PortA_Pins_Cfg[pin][0]
                    PORTA_PIN2_CONFIG.text =self.PortA_Pins_Cfg[pin][1]
                elif pin =='Pin3':
                    PORTA_PIN3_DIR.text =self.PortA_Pins_Cfg[pin][0]
                    PORTA_PIN3_CONFIG.text =self.PortA_Pins_Cfg[pin][1]
                elif pin =='Pin4':
                    PORTA_PIN4_DIR.text =self.PortA_Pins_Cfg[pin][0]
                    PORTA_PIN4_CONFIG.text =self.PortA_Pins_Cfg[pin][1]
                elif pin =='Pin5':
                    PORTA_PIN5_DIR.text =self.PortA_Pins_Cfg[pin][0]
                    PORTA_PIN5_CONFIG.text =self.PortA_Pins_Cfg[pin][1]
                elif pin =='Pin6':
                    PORTA_PIN6_DIR.text =self.PortA_Pins_Cfg[pin][0]
                    PORTA_PIN6_CONFIG.text =self.PortA_Pins_Cfg[pin][1]
                elif pin =='Pin7':
                    PORTA_PIN7_DIR.text =self.PortA_Pins_Cfg[pin][0]
                    PORTA_PIN7_CONFIG.text =self.PortA_Pins_Cfg[pin][1]
        DIO.append(PORTA)
        
        PORTA.append(PORTA_PIN0)
        PORTA_PIN0.append(PORTA_PIN0_DIR)
        PORTA_PIN0.append(PORTA_PIN0_CONFIG)
        PORTA.append(PORTA_PIN1)
        PORTA_PIN1.append(PORTA_PIN1_DIR)
        PORTA_PIN1.append(PORTA_PIN1_CONFIG)
        PORTA.append(PORTA_PIN2)
        PORTA_PIN2.append(PORTA_PIN2_DIR)
        PORTA_PIN2.append(PORTA_PIN2_CONFIG)
        PORTA.append(PORTA_PIN3)
        PORTA_PIN3.append(PORTA_PIN3_DIR)
        PORTA_PIN3.append(PORTA_PIN3_CONFIG)
        PORTA.append(PORTA_PIN4)
        PORTA_PIN4.append(PORTA_PIN4_DIR)
        PORTA_PIN4.append(PORTA_PIN4_CONFIG)
        PORTA.append(PORTA_PIN5)
        PORTA_PIN5.append(PORTA_PIN5_DIR)
        PORTA_PIN5.append(PORTA_PIN5_CONFIG)
        PORTA.append(PORTA_PIN6)
        PORTA_PIN6.append(PORTA_PIN6_DIR)
        PORTA_PIN6.append(PORTA_PIN6_CONFIG)
        PORTA.append(PORTA_PIN7)
        PORTA_PIN7.append(PORTA_PIN7_DIR)
        PORTA_PIN7.append(PORTA_PIN7_CONFIG)                  

  #PortB
        PORTB = ET.Element("PORTB")
        PORTB_PIN0 = ET.Element("PIN0")
        PORTB_PIN1 = ET.Element("PIN1")
        PORTB_PIN2 = ET.Element("PIN2")
        PORTB_PIN3 = ET.Element("PIN3")
        PORTB_PIN4 = ET.Element("PIN4")
        PORTB_PIN5 = ET.Element("PIN5")
        PORTB_PIN6 = ET.Element("PIN6")
        PORTB_PIN7 = ET.Element("PIN7")
          
        PORTB_PIN0_DIR = ET.Element("DIR")
        PORTB_PIN0_CONFIG = ET.Element("CONFIG")
        PORTB_PIN1_DIR = ET.Element("DIR")
        PORTB_PIN1_CONFIG = ET.Element("CONFIG")
        PORTB_PIN2_DIR = ET.Element("DIR")
        PORTB_PIN2_CONFIG = ET.Element("CONFIG")
        PORTB_PIN3_DIR = ET.Element("DIR")
        PORTB_PIN3_CONFIG = ET.Element("CONFIG")
        PORTB_PIN4_DIR = ET.Element("DIR")
        PORTB_PIN4_CONFIG = ET.Element("CONFIG")
        PORTB_PIN5_DIR = ET.Element("DIR")
        PORTB_PIN5_CONFIG = ET.Element("CONFIG")
        PORTB_PIN6_DIR = ET.Element("DIR")
        PORTB_PIN6_CONFIG = ET.Element("CONFIG")
        PORTB_PIN7_DIR = ET.Element("DIR")
        PORTB_PIN7_CONFIG = ET.Element("CONFIG")
        
        for pin in self.PortB_Pins_Cfg.keys():
            if(len(self.PortB_Pins_Cfg[pin])>1):
                if pin == 'Pin0':
                    PORTB_PIN0_DIR.text =self.PortB_Pins_Cfg[pin][0]
                    PORTB_PIN0_CONFIG.text =self.PortB_Pins_Cfg[pin][1]
                elif pin =='Pin1':
                    PORTB_PIN1_DIR.text =self.PortB_Pins_Cfg[pin][0]
                    PORTB_PIN1_CONFIG.text =self.PortB_Pins_Cfg[pin][1]
                elif pin =='Pin2':
                    PORTB_PIN2_DIR.text =self.PortB_Pins_Cfg[pin][0]
                    PORTB_PIN2_CONFIG.text =self.PortB_Pins_Cfg[pin][1]
                elif pin =='Pin3':
                    PORTB_PIN3_DIR.text =self.PortB_Pins_Cfg[pin][0]
                    PORTB_PIN3_CONFIG.text =self.PortB_Pins_Cfg[pin][1]
                elif pin =='Pin4':
                    PORTB_PIN4_DIR.text =self.PortB_Pins_Cfg[pin][0]
                    PORTB_PIN4_CONFIG.text =self.PortB_Pins_Cfg[pin][1]
                elif pin =='Pin5':
                    PORTB_PIN5_DIR.text =self.PortB_Pins_Cfg[pin][0]
                    PORTB_PIN5_CONFIG.text =self.PortB_Pins_Cfg[pin][1]
                elif pin =='Pin6':
                    PORTB_PIN6_DIR.text =self.PortB_Pins_Cfg[pin][0]
                    PORTB_PIN6_CONFIG.text =self.PortB_Pins_Cfg[pin][1]
                elif pin =='Pin7':
                    PORTB_PIN7_DIR.text =self.PortB_Pins_Cfg[pin][0]
                    PORTB_PIN7_CONFIG.text =self.PortB_Pins_Cfg[pin][1]
        DIO.append(PORTB)
        
        PORTB.append(PORTB_PIN0)
        PORTB_PIN0.append(PORTB_PIN0_DIR)
        PORTB_PIN0.append(PORTB_PIN0_CONFIG)
        PORTB.append(PORTB_PIN1)
        PORTB_PIN1.append(PORTB_PIN1_DIR)
        PORTB_PIN1.append(PORTB_PIN1_CONFIG)
        PORTB.append(PORTB_PIN2)
        PORTB_PIN2.append(PORTB_PIN2_DIR)
        PORTB_PIN2.append(PORTB_PIN2_CONFIG)
        PORTB.append(PORTB_PIN3)
        PORTB_PIN3.append(PORTB_PIN3_DIR)
        PORTB_PIN3.append(PORTB_PIN3_CONFIG)
        PORTB.append(PORTB_PIN4)
        PORTB_PIN4.append(PORTB_PIN4_DIR)
        PORTB_PIN4.append(PORTB_PIN4_CONFIG)
        PORTB.append(PORTB_PIN5)
        PORTB_PIN5.append(PORTB_PIN5_DIR)
        PORTB_PIN5.append(PORTB_PIN5_CONFIG)
        PORTB.append(PORTB_PIN6)
        PORTB_PIN6.append(PORTB_PIN6_DIR)
        PORTB_PIN6.append(PORTB_PIN6_CONFIG)
        PORTB.append(PORTB_PIN7)
        PORTB_PIN7.append(PORTB_PIN7_DIR)
        PORTB_PIN7.append(PORTB_PIN7_CONFIG)
        
        #portc 
        PORTC = ET.Element("PORTC")
        PORTC_PIN0 = ET.Element("PIN0")
        PORTC_PIN1 = ET.Element("PIN1")
        PORTC_PIN2 = ET.Element("PIN2")
        PORTC_PIN3 = ET.Element("PIN3")
        PORTC_PIN4 = ET.Element("PIN4")
        PORTC_PIN5 = ET.Element("PIN5")
        PORTC_PIN6 = ET.Element("PIN6")
        PORTC_PIN7 = ET.Element("PIN7")
          
        PORTC_PIN0_DIR = ET.Element("DIR")
        PORTC_PIN0_CONFIG = ET.Element("CONFIG")
        PORTC_PIN1_DIR = ET.Element("DIR")
        PORTC_PIN1_CONFIG = ET.Element("CONFIG")
        PORTC_PIN2_DIR = ET.Element("DIR")
        PORTC_PIN2_CONFIG = ET.Element("CONFIG")
        PORTC_PIN3_DIR = ET.Element("DIR")
        PORTC_PIN3_CONFIG = ET.Element("CONFIG")
        PORTC_PIN4_DIR = ET.Element("DIR")
        PORTC_PIN4_CONFIG = ET.Element("CONFIG")
        PORTC_PIN5_DIR = ET.Element("DIR")
        PORTC_PIN5_CONFIG = ET.Element("CONFIG")
        PORTC_PIN6_DIR = ET.Element("DIR")
        PORTC_PIN6_CONFIG = ET.Element("CONFIG")
        PORTC_PIN7_DIR = ET.Element("DIR")
        PORTC_PIN7_CONFIG = ET.Element("CONFIG")
        
        for pin in self.PortC_Pins_Cfg.keys():
            if(len(self.PortC_Pins_Cfg[pin])>1):
                if pin == 'Pin0':
                    PORTC_PIN0_DIR.text =self.PortC_Pins_Cfg[pin][0]
                    PORTC_PIN0_CONFIG.text =self.PortC_Pins_Cfg[pin][1]
                elif pin =='Pin1':
                    PORTC_PIN1_DIR.text =self.PortC_Pins_Cfg[pin][0]
                    PORTC_PIN1_CONFIG.text =self.PortC_Pins_Cfg[pin][1]
                elif pin =='Pin2':
                    PORTC_PIN2_DIR.text =self.PortC_Pins_Cfg[pin][0]
                    PORTC_PIN2_CONFIG.text =self.PortC_Pins_Cfg[pin][1]
                elif pin =='Pin3':
                    PORTC_PIN3_DIR.text =self.PortC_Pins_Cfg[pin][0]
                    PORTC_PIN3_CONFIG.text =self.PortC_Pins_Cfg[pin][1]
                elif pin =='Pin4':
                    PORTC_PIN4_DIR.text =self.PortC_Pins_Cfg[pin][0]
                    PORTC_PIN4_CONFIG.text =self.PortC_Pins_Cfg[pin][1]
                elif pin =='Pin5':
                    PORTC_PIN5_DIR.text =self.PortC_Pins_Cfg[pin][0]
                    PORTC_PIN5_CONFIG.text =self.PortC_Pins_Cfg[pin][1]
                elif pin =='Pin6':
                    PORTC_PIN6_DIR.text =self.PortC_Pins_Cfg[pin][0]
                    PORTC_PIN6_CONFIG.text =self.PortC_Pins_Cfg[pin][1]
                elif pin =='Pin7':
                    PORTC_PIN7_DIR.text =self.PortC_Pins_Cfg[pin][0]
                    PORTC_PIN7_CONFIG.text =self.PortC_Pins_Cfg[pin][1]
                    
        DIO.append(PORTC)
        PORTC.append(PORTC_PIN0)
        PORTC_PIN0.append(PORTC_PIN0_DIR)
        PORTC_PIN0.append(PORTC_PIN0_CONFIG)
        PORTC.append(PORTC_PIN1)
        PORTC_PIN1.append(PORTC_PIN1_DIR)
        PORTC_PIN1.append(PORTC_PIN1_CONFIG)
        PORTC.append(PORTC_PIN2)
        PORTC_PIN2.append(PORTC_PIN2_DIR)
        PORTC_PIN2.append(PORTC_PIN2_CONFIG)
        PORTC.append(PORTC_PIN3)
        PORTC_PIN3.append(PORTC_PIN3_DIR)
        PORTC_PIN3.append(PORTC_PIN3_CONFIG)
        PORTC.append(PORTC_PIN4)
        PORTC_PIN4.append(PORTC_PIN4_DIR)
        PORTC_PIN4.append(PORTC_PIN4_CONFIG)
        PORTC.append(PORTC_PIN5)
        PORTC_PIN5.append(PORTC_PIN5_DIR)
        PORTC_PIN5.append(PORTC_PIN5_CONFIG)
        PORTC.append(PORTC_PIN6)
        PORTC_PIN6.append(PORTC_PIN6_DIR)
        PORTC_PIN6.append(PORTC_PIN6_CONFIG)
        PORTC.append(PORTC_PIN7)
        PORTC_PIN7.append(PORTC_PIN7_DIR)
        PORTC_PIN7.append(PORTC_PIN7_CONFIG) 

        #portD
        PORTD = ET.Element("PORTD")
        PORTD_PIN0 = ET.Element("PIN0")
        PORTD_PIN1 = ET.Element("PIN1")
        PORTD_PIN2 = ET.Element("PIN2")
        PORTD_PIN3 = ET.Element("PIN3")
        PORTD_PIN4 = ET.Element("PIN4")
        PORTD_PIN5 = ET.Element("PIN5")
        PORTD_PIN6 = ET.Element("PIN6")
        PORTD_PIN7 = ET.Element("PIN7")
          
        PORTD_PIN0_DIR = ET.Element("DIR")
        PORTD_PIN0_CONFIG = ET.Element("CONFIG")
        PORTD_PIN1_DIR = ET.Element("DIR")
        PORTD_PIN1_CONFIG = ET.Element("CONFIG")
        PORTD_PIN2_DIR = ET.Element("DIR")
        PORTD_PIN2_CONFIG = ET.Element("CONFIG")
        PORTD_PIN3_DIR = ET.Element("DIR")
        PORTD_PIN3_CONFIG = ET.Element("CONFIG")
        PORTD_PIN4_DIR = ET.Element("DIR")
        PORTD_PIN4_CONFIG = ET.Element("CONFIG")
        PORTD_PIN5_DIR = ET.Element("DIR")
        PORTD_PIN5_CONFIG = ET.Element("CONFIG")
        PORTD_PIN6_DIR = ET.Element("DIR")
        PORTD_PIN6_CONFIG = ET.Element("CONFIG")
        PORTD_PIN7_DIR = ET.Element("DIR")
        PORTD_PIN7_CONFIG = ET.Element("CONFIG")
        
        for pin in self.PortD_Pins_Cfg.keys():
            
            if(len(self.PortD_Pins_Cfg[pin])>1):
                if pin == 'Pin0':
                    PORTD_PIN0_DIR.text =self.PortD_Pins_Cfg[pin][0]
                    PORTD_PIN0_CONFIG.text =self.PortD_Pins_Cfg[pin][1]
                elif pin =='Pin1':
                    PORTD_PIN1_DIR.text =self.PortD_Pins_Cfg[pin][0]
                    PORTD_PIN1_CONFIG.text =self.PortD_Pins_Cfg[pin][1]
                elif pin =='Pin2':
                    PORTD_PIN2_DIR.text =self.PortD_Pins_Cfg[pin][0]
                    PORTD_PIN2_CONFIG.text =self.PortD_Pins_Cfg[pin][1]
                elif pin =='Pin3':
                    PORTD_PIN3_DIR.text =self.PortD_Pins_Cfg[pin][0]
                    PORTD_PIN3_CONFIG.text =self.PortD_Pins_Cfg[pin][1]
                elif pin =='Pin4':
                    PORTD_PIN4_DIR.text =self.PortD_Pins_Cfg[pin][0]
                    PORTD_PIN4_CONFIG.text =self.PortD_Pins_Cfg[pin][1]
                elif pin =='Pin5':
                    PORTD_PIN5_DIR.text =self.PortD_Pins_Cfg[pin][0]
                    PORTD_PIN5_CONFIG.text =self.PortD_Pins_Cfg[pin][1]
                elif pin =='Pin6':
                    PORTD_PIN6_DIR.text =self.PortD_Pins_Cfg[pin][0]
                    PORTD_PIN6_CONFIG.text =self.PortD_Pins_Cfg[pin][1]
                elif pin =='Pin7':
                    PORTD_PIN7_DIR.text =self.PortD_Pins_Cfg[pin][0]
                    PORTD_PIN7_CONFIG.text =self.PortD_Pins_Cfg[pin][1]
        DIO.append(PORTD)
        
        PORTD.append(PORTD_PIN0)
        PORTD_PIN0.append(PORTD_PIN0_DIR)
        PORTD_PIN0.append(PORTD_PIN0_CONFIG)
        PORTD.append(PORTD_PIN1)
        PORTD_PIN1.append(PORTD_PIN1_DIR)
        PORTD_PIN1.append(PORTD_PIN1_CONFIG)
        PORTD.append(PORTD_PIN2)
        PORTD_PIN2.append(PORTD_PIN2_DIR)
        PORTD_PIN2.append(PORTD_PIN2_CONFIG)
        PORTD.append(PORTD_PIN3)
        PORTD_PIN3.append(PORTD_PIN3_DIR)
        PORTD_PIN3.append(PORTD_PIN3_CONFIG)
        PORTD.append(PORTD_PIN4)
        PORTD_PIN4.append(PORTD_PIN4_DIR)
        PORTD_PIN4.append(PORTD_PIN4_CONFIG)
        PORTD.append(PORTD_PIN5)
        PORTD_PIN5.append(PORTD_PIN5_DIR)
        PORTD_PIN5.append(PORTD_PIN5_CONFIG)
        PORTD.append(PORTD_PIN6)
        PORTD_PIN6.append(PORTD_PIN6_DIR)
        PORTD_PIN6.append(PORTD_PIN6_CONFIG)
        PORTD.append(PORTD_PIN7)
        PORTD_PIN7.append(PORTD_PIN7_DIR)
        PORTD_PIN7.append(PORTD_PIN7_CONFIG)
        #if os.path.exists(self.filetoXml.text()):
        try:
            path = self.filetoXml.text() + r'Dio_cfg.xml'
            with open(path, 'w', encoding='utf-8') as f:
                f.write(ET.tostring(DIO, pretty_print=True).decode())
        #File_Handler.write(ET.tostring(DIO, pretty_print=True).decode())
                f.close()
        except IOError:
            sys.stderr.write('problem reading:' + path)
                        
        # else:
             # print("the path to the file is not correct")
             
    def generateFunction(self):
        try:
            Out_path = self.filePath.text() + r'\Dio_cfg.h'
            file_Handler = open(Out_path,'w')
            file_Handler.write("#ifndef _DIO_CFG_H\n")
            file_Handler.write("#define _DIO_CFG_H\n")
            file_Handler.write("\n")
            file_Handler.write("\n")
            for pin in self.PortA_Pins_Cfg.keys():
                #print(pin+" "+ ' '.join(self.PortA_Pins_Cfg[pin])+" "+str(self.tab.tabText(0)))
                if(len(self.PortA_Pins_Cfg[pin])>1):
                    file_Handler.write("#define      DIO_"+str(self.tab.tabText(0))+"_"+pin+"_MODE        "+"DIO_"+'_'.join(self.PortA_Pins_Cfg[pin])+"\n")
            for pin in self.PortB_Pins_Cfg.keys():
                #print(pin+" "+ ' '.join(self.PortB_Pins_Cfg[pin])+" "+str(self.tab.tabText(1)))
                if(len(self.PortB_Pins_Cfg[pin])>1):
                    file_Handler.write("#define      DIO_"+str(self.tab.tabText(1))+"_"+pin+"_MODE        "+"DIO_"+'_'.join(self.PortB_Pins_Cfg[pin])+"\n")
            for pin in self.PortC_Pins_Cfg.keys():
        
                #print(pin+" "+ ' '.join(self.PortC_Pins_Cfg[pin])+" "+str(self.tab.tabText(2)))
                if(len(self.PortC_Pins_Cfg[pin])>1):
                    file_Handler.write("#define      DIO_"+str(self.tab.tabText(2))+"_"+pin+"_MODE        "+"DIO_"+'_'.join(self.PortA_Pins_Cfg[pin])+"\n")
            for pin in self.PortD_Pins_Cfg.keys():
                #print(pin+" "+ ' '.join(self.PortD_Pins_Cfg[pin])+" "+str(self.tab.tabText(3)))
                if(len(self.PortD_Pins_Cfg[pin])>1):
                    file_Handler.write("#define      DIO_"+str(self.tab.tabText(3))+"_"+pin+"_MODE        "+"DIO_"+'_'.join(self.PortD_Pins_Cfg[pin])+"\n")
            file_Handler.write("#endif /*_DIO_CFG_H*/ \n")
            file_Handler.close()
        except IOError:
             sys.stderr.write('problem reading:' + Out_path)
             
    def ComboBox_PinChoice(self):

       
        #pin_cfg = []

            Port = self.tab.currentIndex()
            if(Port == 0): 
  
            
                if(self.LoadingCfg.isChecked()!= True):
                    QObject.connect(self.outputARadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortA.setDisabled)
                    QObject.connect(self.outputARadio,SIGNAL("clicked(bool)"),self.Output_configPortA.setEnabled)
                    QObject.connect(self.inputARadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortA.setEnabled)
                    QObject.connect(self.inputARadio,SIGNAL("clicked(bool)"),self.Output_configPortA.setDisabled)
            # self.outputARadio.setAutoExclusive(False)
            # self.outputARadio.setChecked(True)
            # self.outputARadio.setAutoExclusive(True)
            
            # self.outputARadio.clicked.connect(self.Input_ConfigPortA.setDisabled)
            # self.outputARadio.clicked.connect(self.Output_configPortA.setEnabled)
            # self.inputARadio.clicked.connect(self.Output_configPortA.setDisabled)
            # self.inputARadio.clicked.connect(self.Input_ConfigPortA.setEnabled)
            
                Group_list=[self.PinDirectionAGroup,self.Output_configPortA,self.Input_ConfigPortA]
                for group in Group_list:
                    group.setEnabled(True)
                    for radioButton in group.findChildren(QRadioButton):
                        radioButton.setAutoExclusive(False)
                        radioButton.setChecked(False)
                        radioButton.setAutoExclusive(True)
                if(self.LoadingCfg.isChecked()== True): 
                    if self.comboBoxPortA.currentText().upper() in self.PortA.keys():  
            
                        Group_list=[self.PinDirectionAGroup,self.Output_configPortA,self.Input_ConfigPortA]
                        for group in Group_list:
                
                            for radioButton in group.findChildren(QRadioButton):
                                Rad_Name= str(radioButton.text().upper())
                   
                                Pin_Name=self.comboBoxPortA.currentText().upper()
                    
                  
                                if Rad_Name in self.PortA[Pin_Name].values():
                       
                                    radioButton.setChecked(True) 
             
            
            elif(Port == 1):
               
                if(self.LoadingCfg.isChecked()!= True):
                    QObject.connect(self.outputBRadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortB.setDisabled)
                    QObject.connect(self.outputBRadio,SIGNAL("clicked(bool)"),self.Output_configPortB.setEnabled)
                    QObject.connect(self.inputBRadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortB.setEnabled)
                    QObject.connect(self.inputBRadio,SIGNAL("clicked(bool)"),self.Output_configPortB.setDisabled)

                Group_list=[self.PinDirectionBGroup,self.Output_configPortB,self.Input_ConfigPortB]
                for group in Group_list:
                    group.setEnabled(True)
                    for radioButton in group.findChildren(QRadioButton):
                        radioButton.setAutoExclusive(False)
                        radioButton.setChecked(False)
                        radioButton.setAutoExclusive(True)
                if(self.LoadingCfg.isChecked()== True): 
                    
                    if self.comboBoxPortB.currentText().upper()in self.PortB.keys():  
                        Group_list=[self.PinDirectionBGroup,self.Output_configPortB,self.Input_ConfigPortB]
                        for group in Group_list:
                            for radioButton in group.findChildren(QRadioButton):
                                Rad_Name= radioButton.text().upper()
                                Pin_Name=self.comboBoxPortB.currentText().upper()
                                if Rad_Name in self.PortB[Pin_Name].values():
                                    radioButton.setChecked(True) 
                
            elif(Port == 2):
              
                
                # self.outputCRadio.clicked.connect(self.Input_ConfigPortC.setDisabled)
                # self.outputCRadio.clicked.connect(self.Output_configPortC.setEnabled)
                # self.inputCRadio.clicked.connect(self.Input_ConfigPortC.setEnabled)
                # self.inputCRadio.clicked.connect(self.Output_configPortC.setDisabled)
                
                if(self.LoadingCfg.isChecked()!= True):
                    QObject.connect(self.outputCRadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortC.setDisabled)
                    QObject.connect(self.outputCRadio,SIGNAL("clicked(bool)"),self.Output_configPortC.setEnabled)
                    QObject.connect(self.inputCRadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortC.setEnabled)
                    QObject.connect(self.inputCRadio,SIGNAL("clicked(bool)"),self.Output_configPortC.setDisabled)
                # self.outputCRadio.setAutoExclusive(False)
                # self.outputCRadio.setChecked(True)
                # self.outputCRadio.setAutoExclusive(True)
                
                Group_list=[self.PinDirectionCGroup,self.Output_configPortC,self.Input_ConfigPortC]
                for group in Group_list:
                    group.setEnabled(True)
                    for radioButton in group.findChildren(QRadioButton):
                        radioButton.setAutoExclusive(False)
                        radioButton.setChecked(False)
                        radioButton.setAutoExclusive(True)
                if(self.LoadingCfg.isChecked()== True): 
                    if self.comboBoxPortC.currentText().upper()in self.PortC.keys():  
                        Group_list=[self.PinDirectionCGroup,self.Output_configPortC,self.Input_ConfigPortC]
                        for group in Group_list:
                            for radioButton in group.findChildren(QRadioButton):
                                Rad_Name= radioButton.text().upper()
                                Pin_Name=self.comboBoxPortC.currentText().upper()
                                if Rad_Name in self.PortC[Pin_Name].values():
                                    radioButton.setChecked(True) 
            elif(Port == 3):
               
                if(self.LoadingCfg.isChecked()!= True):
                    QObject.connect(self.outputDRadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortD.setDisabled)
                    QObject.connect(self.outputDRadio,SIGNAL("clicked(bool)"),self.Output_configPortD.setEnabled)
                    QObject.connect(self.inputDRadio,SIGNAL("clicked(bool)"),self.Input_ConfigPortD.setEnabled)
                    QObject.connect(self.inputDRadio,SIGNAL("clicked(bool)"),self.Output_configPortD.setDisabled)
                # self.outputDRadio.setAutoExclusive(False)
                # self.outputDRadio.setChecked(True)
                # self.outputDRadio.setAutoExclusive(True)
                
                # self.outputDRadio.clicked.connect(self.Input_ConfigPortD.setDisabled)
                # self.outputDRadio.clicked.connect(self.Output_configPortD.setEnabled)
                # self.inputDRadio.clicked.connect(self.Input_ConfigPortD.setEnabled)
                # self.inputDRadio.clicked.connect(self.Output_configPortD.setDisabled)
                
                Group_list=[self.PinDirectionDGroup,self.Output_configPortD,self.Input_ConfigPortD]
                for group in Group_list:
                    group.setEnabled(True)
                    for radioButton in group.findChildren(QRadioButton):
                        radioButton.setAutoExclusive(False)
                        radioButton.setChecked(False)
                        radioButton.setAutoExclusive(True) 
                
                if(self.LoadingCfg.isChecked()== True): 
                    if self.comboBoxPortD.currentText().upper() in self.PortD.keys():  
                        Group_list=[self.PinDirectionDGroup,self.Output_configPortD,self.Input_ConfigPortD]
                        for group in Group_list:
                            for radioButton in group.findChildren(QRadioButton):
                                Rad_Name= radioButton.text().upper()
                                Pin_Name=self.comboBoxPortD.currentText().upper()
                                if Rad_Name in self.PortD[Pin_Name].values():
                                    radioButton.setChecked(True) 

                
     
    def AddPinCfgFunction(self):
        pin_cfg = []
        
        Port = self.tab.currentIndex()
        #PortA
        if(Port == 0): 
            if(self.outputARadio.isChecked()):
                pin_cfg.append("OUTPUT")
                if(self.HighRadioPortA.isChecked()):
                    pin_cfg.append("HIGH")
                elif(self.LowRadioPortA.isChecked()):
                    pin_cfg.append("LOW")
            elif(self.inputARadio.isChecked()):
                pin_cfg.append("INPUT")
                if(self.pull_upRadioPortA.isChecked()):
                    pin_cfg.append("PULL-UP")
                elif(self.High_impRadioPortA.isChecked()):
                    pin_cfg.append("HIGH-IMP")
            self.PortA_Pins_Cfg[self.comboBoxPortA.currentText()] = pin_cfg
        elif(Port == 1):
            
            if(self.outputBRadio.isChecked()):
                pin_cfg.append("OUTPUT")
                if(self.HighRadioPortB.isChecked()):
                    pin_cfg.append("HIGH")
                elif(self.LowRadioPortB.isChecked()):
                    pin_cfg.append("LOW")
            elif(self.inputBRadio.isChecked()):
                pin_cfg.append("INPUT")
                if(self.pull_upRadioPortB.isChecked()):
                    pin_cfg.append("PULL-UP")
                elif(self.High_impRadioPortB.isChecked()):
                    pin_cfg.append("HIGH-IMP")
            self.PortB_Pins_Cfg[self.comboBoxPortB.currentText()] = pin_cfg
        elif(Port == 2):
            if(self.outputCRadio.isChecked()):
                pin_cfg.append("OUTPUT")
                if(self.HighRadioPortC.isChecked()):
                    pin_cfg.append("HIGH")
                elif(self.LowRadioPortC.isChecked()):
                    pin_cfg.append("LOW")
            elif(self.inputCRadio.isChecked()):
                pin_cfg.append("INPUT")
                if(self.pull_upRadioPortC.isChecked()):
                    pin_cfg.append("PULL-UP")
                elif(self.High_impRadioPortC.isChecked()):
                    pin_cfg.append("HIGH-IMP")
            self.PortC_Pins_Cfg[self.comboBoxPortC.currentText()] = pin_cfg
        elif(Port == 3):
            
            if(self.outputDRadio.isChecked()):
                pin_cfg.append("OUTPUT")
                if(self.HighRadioPortD.isChecked()):
                    pin_cfg.append("HIGH")
                elif(self.LowRadioPortD.isChecked()):
                    pin_cfg.append("LOW")
            elif(self.inputDRadio.isChecked()):
                pin_cfg.append("INPUT")
                if(self.pull_upRadioPortD.isChecked()):
                    pin_cfg.append("PULL-UP")
                elif(self.High_impRadioPortD.isChecked()):
                    pin_cfg.append("HIGH-IMP")
            self.PortD_Pins_Cfg[self.comboBoxPortD.currentText()] = pin_cfg
                    
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Pins Configuration", None))
        self.PinChoice.setTitle(QCoreApplication.translate("Form", u"pin choice", None))
        self.comboBoxPortA.setItemText(0, QCoreApplication.translate("Form", u"-- Choose pin number --", None))
        self.comboBoxPortA.setItemText(1, QCoreApplication.translate("Form", u"Pin0", None))
        self.comboBoxPortA.setItemText(2, QCoreApplication.translate("Form", u"Pin1", None))
        self.comboBoxPortA.setItemText(3, QCoreApplication.translate("Form", u"Pin2", None))
        self.comboBoxPortA.setItemText(4, QCoreApplication.translate("Form", u"Pin3", None))
        self.comboBoxPortA.setItemText(5, QCoreApplication.translate("Form", u"Pin4", None))
        self.comboBoxPortA.setItemText(6, QCoreApplication.translate("Form", u"Pin5", None))
        self.comboBoxPortA.setItemText(7, QCoreApplication.translate("Form", u"Pin6", None))
        self.comboBoxPortA.setItemText(8, QCoreApplication.translate("Form", u"Pin7", None))
        self.comboBoxPortA.setItemText(9, QCoreApplication.translate("Form", u"Pin8", None))

        self.PinlabelPortA.setText(QCoreApplication.translate("Form", u"Choose Pin", None))
        self.Input_ConfigPortA.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.pull_upRadioPortA.setText(QCoreApplication.translate("Form", u"Pull-Up", None))
        self.High_impRadioPortA.setText(QCoreApplication.translate("Form", u"High-Imp", None))
#if QT_CONFIG(tooltip)
        self.Output_configPortA.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Output_configPortA.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.HighRadioPortA.setText(QCoreApplication.translate("Form", u"High", None))
        self.LowRadioPortA.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PinDirectionAGroup.setTitle(QCoreApplication.translate("Form", u"Pin Direction", None))
        self.outputARadio.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputARadio.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PinCfgPortA.setText(QCoreApplication.translate("Form", u"Add Pin Configuration ", None))
        self.tab.setTabText(self.tab.indexOf(self.PORTA), QCoreApplication.translate("Form", u"PORTA", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"pin choice", None))
        self.comboBoxPortB.setItemText(0, QCoreApplication.translate("Form", u"-- Choose pin number --", None))
        self.comboBoxPortB.setItemText(1, QCoreApplication.translate("Form", u"Pin0", None))
        self.comboBoxPortB.setItemText(2, QCoreApplication.translate("Form", u"Pin1", None))
        self.comboBoxPortB.setItemText(3, QCoreApplication.translate("Form", u"Pin2", None))
        self.comboBoxPortB.setItemText(4, QCoreApplication.translate("Form", u"Pin3", None))
        self.comboBoxPortB.setItemText(5, QCoreApplication.translate("Form", u"Pin4", None))
        self.comboBoxPortB.setItemText(6, QCoreApplication.translate("Form", u"Pin5", None))
        self.comboBoxPortB.setItemText(7, QCoreApplication.translate("Form", u"Pin6", None))
        self.comboBoxPortB.setItemText(8, QCoreApplication.translate("Form", u"Pin7", None))
        self.comboBoxPortB.setItemText(9, QCoreApplication.translate("Form", u"Pin8", None))

        self.PinlabelPortB.setText(QCoreApplication.translate("Form", u"Choose Pin", None))
        self.Input_ConfigPortB.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.pull_upRadioPortB.setText(QCoreApplication.translate("Form", u"Pull-Up", None))
        self.High_impRadioPortB.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.Output_configPortB.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.HighRadioPortB.setText(QCoreApplication.translate("Form", u"High", None))
        self.LowRadioPortB.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PinDirectionBGroup.setTitle(QCoreApplication.translate("Form", u"Pin Direction", None))
        self.outputBRadio.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputBRadio.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PinCfgPortB.setText(QCoreApplication.translate("Form", u"Add Pin Configuration ", None))
        self.tab.setTabText(self.tab.indexOf(self.PORTB), QCoreApplication.translate("Form", u"PORTB", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"pin choice", None))
        self.comboBoxPortC.setItemText(0, QCoreApplication.translate("Form", u"-- Choose pin number --", None))
        self.comboBoxPortC.setItemText(1, QCoreApplication.translate("Form", u"Pin0", None))
        self.comboBoxPortC.setItemText(2, QCoreApplication.translate("Form", u"Pin1", None))
        self.comboBoxPortC.setItemText(3, QCoreApplication.translate("Form", u"Pin2", None))
        self.comboBoxPortC.setItemText(4, QCoreApplication.translate("Form", u"Pin3", None))
        self.comboBoxPortC.setItemText(5, QCoreApplication.translate("Form", u"Pin4", None))
        self.comboBoxPortC.setItemText(6, QCoreApplication.translate("Form", u"Pin5", None))
        self.comboBoxPortC.setItemText(7, QCoreApplication.translate("Form", u"Pin6", None))
        self.comboBoxPortC.setItemText(8, QCoreApplication.translate("Form", u"Pin7", None))
        self.comboBoxPortC.setItemText(9, QCoreApplication.translate("Form", u"Pin8", None))

        self.PinlabelPortC.setText(QCoreApplication.translate("Form", u"Choose Pin", None))
        self.Input_ConfigPortC.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.pull_upRadioPortC.setText(QCoreApplication.translate("Form", u"Pull-Up", None))
        self.High_impRadioPortC.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.Output_configPortC.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.HighRadioPortC.setText(QCoreApplication.translate("Form", u"High", None))
        self.LowRadioPortC.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PinDirectionCGroup.setTitle(QCoreApplication.translate("Form", u"Pin Direction", None))
        self.outputCRadio.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputCRadio.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PinCfgPortC.setText(QCoreApplication.translate("Form", u"Add Pin Configuration ", None))
        self.tab.setTabText(self.tab.indexOf(self.PORTC), QCoreApplication.translate("Form", u"PORTC", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"pin choice", None))
        self.comboBoxPortD.setItemText(0, QCoreApplication.translate("Form", u"-- Choose pin number --", None))
        self.comboBoxPortD.setItemText(1, QCoreApplication.translate("Form", u"Pin0", None))
        self.comboBoxPortD.setItemText(2, QCoreApplication.translate("Form", u"Pin1", None))
        self.comboBoxPortD.setItemText(3, QCoreApplication.translate("Form", u"Pin2", None))
        self.comboBoxPortD.setItemText(4, QCoreApplication.translate("Form", u"Pin3", None))
        self.comboBoxPortD.setItemText(5, QCoreApplication.translate("Form", u"Pin4", None))
        self.comboBoxPortD.setItemText(6, QCoreApplication.translate("Form", u"Pin5", None))
        self.comboBoxPortD.setItemText(7, QCoreApplication.translate("Form", u"Pin6", None))
        self.comboBoxPortD.setItemText(8, QCoreApplication.translate("Form", u"Pin7", None))
        self.comboBoxPortD.setItemText(9, QCoreApplication.translate("Form", u"Pin8", None))

        self.PinlabelPortD.setText(QCoreApplication.translate("Form", u"Choose Pin", None))
        self.Input_ConfigPortD.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.pull_upRadioPortD.setText(QCoreApplication.translate("Form", u"Pull-Up", None))
        self.High_impRadioPortD.setText(QCoreApplication.translate("Form", u"High-Imp", None))
        self.Output_configPortD.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.HighRadioPortD.setText(QCoreApplication.translate("Form", u"High", None))
        self.LowRadioPortD.setText(QCoreApplication.translate("Form", u"Low", None))
        self.PinDirectionDGroup.setTitle(QCoreApplication.translate("Form", u"Pin Direction", None))
        self.outputDRadio.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputDRadio.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PinCfgPortD.setText(QCoreApplication.translate("Form", u"Add Pin Configuration ", None))
        self.tab.setTabText(self.tab.indexOf(self.PORTD), QCoreApplication.translate("Form", u"PORTD", None))
        self.SaveCfg.setText(QCoreApplication.translate("Form", u"Save Configuration", None))
        self.LoadCfg.setText(QCoreApplication.translate("Form", u"Load Configuration", None))
        self.filePath.setText(QCoreApplication.translate("Form", u"Enter the path to generate the configuration", None))
        self.GenerateButton.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.outPathLabel.setText(QCoreApplication.translate("Form", u"Output Path", None))
        self.ClearButton.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.filetoXml.setText(QCoreApplication.translate("Form", u"Enter the path to save or load xml file", None))
        self.label.setText(QCoreApplication.translate("Form", u"Path to Configuration", None))
        self.LoadingCfg.setText(QCoreApplication.translate("Form", u"Presaved Configuration shown", None))
    # retranslateUi

app=QApplication(sys.argv)
Widget=QWidget()
Form=Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())# -*- coding: utf-8 -*-