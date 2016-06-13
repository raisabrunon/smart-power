# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogSubstation.ui'
#
# Created: Mon Mar  2 22:55:39 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys

class SubstationDialog(QtGui.QWidget):

    def __init__(self, item):
        super(SubstationDialog, self).__init__()
        self.dialog = QtGui.QDialog(self)
        self.item = item
        self.setupUi(self.dialog)
        self.dialog.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(473, 370)
        #Define o tamanho da caixa dialogo
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 330, 341, 32))
        #Define o tamanho do layout dos botões do dialogo
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(5, 5, 453, 330))

        self.grid = QtGui.QGridLayout(self.gridLayoutWidget)
        self.grid.setSpacing(5)

        #definição da propriedade NOME
        self.nomeLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.nomeLabel.setObjectName("nomeLabel")
        self.grid.addWidget(self.nomeLabel, 0, 0)

        self.nomeLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.nomeLineEdit.setObjectName("nomeLineEdit")
        self.nomeLineEdit.setPlaceholderText(str(self.item.substation.nome))
        self.grid.addWidget(self.nomeLineEdit, 0, 1, 1, 4)
        self.nomeLineEdit.textChanged.connect(self.en_dis_button)

        #definição da propriedade NÚMERO DE TRANSFORMADORES
        self.numTransformadoresLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.numTransformadoresLabel.setObjectName("numTransformadoresLabel")
        self.grid.addWidget(self.numTransformadoresLabel, 1, 0)

        self.numTransformadoresLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.numTransformadoresLineEdit.setObjectName("numTransformadoresLineEdit")
        self.numTransformadoresLineEdit.setPlaceholderText(str(self.item.substation.n_transformadores))
        self.grid.addWidget(self.numTransformadoresLineEdit, 1, 1, 1, 4)

        #definição da propriedade TENSÃO PRIMÁRIO
        self.tpLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.tpLabel.setObjectName("tpLabel")
        self.grid.addWidget(self.tpLabel, 2, 0)

        self.tpLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.tpLineEdit.setObjectName("tpLineEdit")
        self.tpLineEdit.setPlaceholderText(str(self.item.substation.tensao_primario))
        self.grid.addWidget(self.tpLineEdit, 2, 1, 1, 4)

        #definição da propriedade TENSÃO SECUNDÁRIO
        self.tsLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.tsLabel.setObjectName("tsLabel")
        self.grid.addWidget(self.tsLabel, 3, 0)

        self.tsLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.tsLineEdit.setObjectName("tsLineEdit")
        self.tsLineEdit.setPlaceholderText(str(self.item.substation.tensao_secundario))
        self.grid.addWidget(self.tsLineEdit, 3, 1, 1, 4)

        #definição da propriedade POTENCIA
        self.potLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.potLabel.setObjectName("potLabel")
        self.grid.addWidget(self.potLabel, 4, 0)

        self.potLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.potLineEdit.setObjectName("potLineEdit")
        self.potLineEdit.setPlaceholderText(str(self.item.substation.potencia))
        self.grid.addWidget(self.potLineEdit, 4, 1, 1, 4)

        #definição da propriedade IMPEDANCIA SEQUENCIA POSITIVA
        self.impedanciaPositiva = QtGui.QLabel(self.gridLayoutWidget)
        self.impedanciaPositiva.setObjectName("impedanciaPositiva")
        self.grid.addWidget(self.impedanciaPositiva, 5, 0)

        self.r_posLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.r_posLineEdit.setObjectName("r_posLineEdit")
        self.r_posLineEdit.setPlaceholderText(str(self.item.substation.r_pos))
        self.grid.addWidget(self.r_posLineEdit, 5, 1)

        self.sinalMaisLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.sinalMaisLabel.setObjectName("sinalMaisLabel")
        self.grid.addWidget(self.sinalMaisLabel, 5, 2)

        self.i_posLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.i_posLineEdit.setObjectName("i_posLineEdit")
        self.i_posLineEdit.setPlaceholderText(str(self.item.substation.i_pos))
        self.grid.addWidget(self.i_posLineEdit, 5, 3)

        self.jLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.jLabel.setObjectName("jLabel")
        self.grid.addWidget(self.jLabel, 5, 4)

        #definição da propriedade IMPEDANCIA SEQUENCIA ZERO
        self.impedanciaZero = QtGui.QLabel(self.gridLayoutWidget)
        self.impedanciaZero.setObjectName("impedanciaZero")
        self.grid.addWidget(self.impedanciaZero, 6, 0)

        self.r_zeroLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.r_zeroLineEdit.setObjectName("r_zeroLineEdit")
        self.r_zeroLineEdit.setPlaceholderText(str(self.item.substation.r_zero))
        self.grid.addWidget(self.r_zeroLineEdit, 6, 1)

        self.sinalMais2Label = QtGui.QLabel(self.gridLayoutWidget)
        self.sinalMais2Label.setObjectName("sinalMaisLabel2")
        self.grid.addWidget(self.sinalMais2Label, 6, 2)

        self.i_zeroLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.i_zeroLineEdit.setObjectName("i_zeroLineEdit")
        self.i_zeroLineEdit.setPlaceholderText(str(self.item.substation.i_zero))
        self.grid.addWidget(self.i_zeroLineEdit, 6, 3)

        self.j2Label = QtGui.QLabel(self.gridLayoutWidget)
        self.j2Label.setObjectName("j2Label")
        self.grid.addWidget(self.j2Label, 6, 4)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        if self.nomeLineEdit.text() == "":
            print self.buttonBox.buttons()
            self.buttonBox.buttons()[0].setEnabled(False)
        else:
            self.buttonBox.buttons()[0].setEnabled(True)
        if self.nomeLineEdit.placeholderText() != "":
            self.buttonBox.buttons()[0].setEnabled(True)

    def en_dis_button(self):

        if self.nomeLineEdit.text() == "":
            print self.buttonBox.buttons()
            self.buttonBox.buttons()[0].setEnabled(False)
        else:
            self.buttonBox.buttons()[0].setEnabled(True)

    def retranslateUi(self, Dialog):
        #Tradução dos nomes dados aos objetos para os nomes gráficos do programa
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Subestação - Propriedades", None, QtGui.QApplication.UnicodeUTF8))
        self.nomeLabel.setText(QtGui.QApplication.translate("Dialog", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.numTransformadoresLabel.setText(QtGui.QApplication.translate("Dialog", "Número de transformadores:", None, QtGui.QApplication.UnicodeUTF8))
        self.tpLabel.setText(QtGui.QApplication.translate("Dialog", "Tensão Primário (kV):", None, QtGui.QApplication.UnicodeUTF8))
        self.tsLabel.setText(QtGui.QApplication.translate("Dialog", "Tensão Secundário (kV):", None, QtGui.QApplication.UnicodeUTF8))
        self.potLabel.setText(QtGui.QApplication.translate("Dialog", "Potência (MVA):", None, QtGui.QApplication.UnicodeUTF8))
        self.impedanciaPositiva.setText(QtGui.QApplication.translate("Dialog", "Impedância - Sequência Positiva (ohms):", None, QtGui.QApplication.UnicodeUTF8))
        self.sinalMaisLabel.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.jLabel.setText(QtGui.QApplication.translate("Dialog", "j", None, QtGui.QApplication.UnicodeUTF8)) 
        self.impedanciaZero.setText(QtGui.QApplication.translate("Dialog", "Impedância - Sequência Zero (ohms):", None, QtGui.QApplication.UnicodeUTF8))
        self.sinalMais2Label.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.j2Label.setText(QtGui.QApplication.translate("Dialog", "j", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    SubstationDialog = SubstationDialog()
    sys.exit(app.exec_())
