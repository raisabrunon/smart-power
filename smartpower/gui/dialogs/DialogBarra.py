# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogBarra.ui'
#
# Created: Sun Mar  1 19:05:57 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys
class BarraDialog(QtGui.QWidget):

    def __init__(self, item):
        super(BarraDialog, self).__init__()
        self.dialog = QtGui.QDialog(None)
        self.item = item
        self.setupUi(self.dialog)
        self.dialog.exec_()

    def setupUi(self, Propriedades):
        Propriedades.setObjectName("Propriedades")
        Propriedades.resize(451, 231)
        #Define o tamanho da caixa dialogo

        self.buttonBox = QtGui.QDialogButtonBox(Propriedades)
        self.buttonBox.setGeometry(QtCore.QRect(0, 181, 341, 32))
        #Define o tamanho do layout dos botões do dialogo
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.gridLayoutWidget = QtGui.QWidget(Propriedades)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(5, 5, 431, 181))

        self.grid = QtGui.QGridLayout(self.gridLayoutWidget)
        self.grid.setSpacing(5)

        #definição da propriedade NOME
        self.nomeLabel = QtGui.QLabel()
        self.nomeLabel.setObjectName("nomeLabel")
        self.grid.addWidget(self.nomeLabel, 0, 0)

        self.nomeLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.nomeLineEdit.setObjectName("nomeLineEdit")
        self.nomeLineEdit.setPlaceholderText(str(self.item.barra.nome))
        self.nomeLineEdit.textChanged.connect(self.en_dis_button)
        self.grid.addWidget(self.nomeLineEdit, 0, 1, 1, 4)
        
        # #definição da propriedade FASES
        self.fasesLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.fasesLabel.setObjectName("fasesLabel")
        self.grid.addWidget(self.fasesLabel, 1, 0,)

        self.fasesLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.fasesLineEdit.setObjectName("fasesLineEdit")
        self.fasesLineEdit.setText(str(self.item.barra.phases))
        self.grid.addWidget(self.fasesLineEdit, 1, 1, 1, 4)

        # #definição da propriedade IMPEDANCIA SEQUENCIA POSITIVA
        self.impedanciaPositiva = QtGui.QLabel(self.gridLayoutWidget)
        self.impedanciaPositiva.setObjectName("impedanciaPositiva")
        self.grid.addWidget(self.impedanciaPositiva, 2, 0)

        self.r_posLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.r_posLineEdit.setObjectName("r_posLineEdit")
        self.r_posLineEdit.setText(str(self.item.barra.r_pos))
        self.grid.addWidget(self.r_posLineEdit, 2, 1)

        self.sinalMaisLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.sinalMaisLabel.setObjectName("sinalMaisLabel")
        self.grid.addWidget(self.sinalMaisLabel, 2, 2)

        self.i_posLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.i_posLineEdit.setObjectName("i_posLineEdit")
        self.i_posLineEdit.setText(str(self.item.barra.i_pos))
        self.grid.addWidget(self.i_posLineEdit, 2, 3)

        self.jLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.jLabel.setObjectName("jLabel")
        self.grid.addWidget(self.jLabel, 2, 4)

        # #definição da propriedade IMPEDANCIA SEQUENCIA ZERO
        self.impedanciaZero = QtGui.QLabel(self.gridLayoutWidget)
        self.impedanciaZero.setObjectName("impedanciaZero")
        self.grid.addWidget(self.impedanciaZero, 3, 0)

        self.r_zeroLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.r_zeroLineEdit.setObjectName("r_zeroLineEdit")
        self.r_zeroLineEdit.setText(str(self.item.barra.r_zero))
        self.grid.addWidget(self.r_zeroLineEdit, 3, 1)

        self.sinalMais2Label = QtGui.QLabel(self.gridLayoutWidget)
        self.sinalMais2Label.setObjectName("sinalMaisLabel2")
        self.grid.addWidget(self.sinalMais2Label, 3, 2)

        self.i_zeroLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.i_zeroLineEdit.setObjectName("i_zeroLineEdit")
        self.i_zeroLineEdit.setText(str(self.item.barra.i_zero))
        self.grid.addWidget(self.i_zeroLineEdit, 3 , 3)

        self.j2Label = QtGui.QLabel(self.gridLayoutWidget)
        self.j2Label.setObjectName("j2Label")
        self.grid.addWidget(self.j2Label, 3, 4)

        self.retranslateUi(Propriedades)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Propriedades.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Propriedades.reject)
        QtCore.QMetaObject.connectSlotsByName(Propriedades)

        self.en_dis_button()
        if self.nomeLineEdit.placeholderText() != "":
            if self.fasesLineEdit.text() != "0":
                if self.r_posLineEdit.text() != "0.0":
                    if self.i_posLineEdit.text() != "0.0":
                        if self.r_zeroLineEdit.text() != "0.0":
                            if self.i_zeroLineEdit.text() != "0.0":
                                self.buttonBox.buttons()[0].setFocus()
                            else:
                                self.i_zeroLineEdit.setFocus()
                        else:
                            self.r_zeroLineEdit.setFocus()
                    else:
                        self.i_posLineEdit.setFocus()
                else:
                    self.r_posLineEdit.setFocus()
            else:
                self.fasesLineEdit.setFocus()
        else:
            self.nomeLineEdit.setFocus()

    def en_dis_button(self):

        if self.nomeLineEdit.text() == "":
            print self.buttonBox.buttons()
            self.buttonBox.buttons()[0].setEnabled(False)
        else:
            self.buttonBox.buttons()[0].setEnabled(True)
        if self.nomeLineEdit.placeholderText() != "":
            self.buttonBox.buttons()[0].setEnabled(True)

    def retranslateUi(self, Propriedades):
        #Tradução dos nomes dados aos objetos para os nomes gráficos do programa
        Propriedades.setWindowTitle(QtGui.QApplication.translate("Propriedades", "Barra - Propriedades", None, QtGui.QApplication.UnicodeUTF8))
        self.nomeLabel.setText(QtGui.QApplication.translate("Propriedades", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.fasesLabel.setText(QtGui.QApplication.translate("Propriedades", "Fases:", None, QtGui.QApplication.UnicodeUTF8))
        self.impedanciaPositiva.setText(QtGui.QApplication.translate("Dialog", "Impedância - Sequência Positiva (pu):", None, QtGui.QApplication.UnicodeUTF8))
        self.sinalMaisLabel.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.jLabel.setText(QtGui.QApplication.translate("Dialog", "j", None, QtGui.QApplication.UnicodeUTF8))
        self.impedanciaZero.setText(QtGui.QApplication.translate("Dialog", "Impedância - Sequência Zero (pu):", None, QtGui.QApplication.UnicodeUTF8))
        self.sinalMais2Label.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.j2Label.setText(QtGui.QApplication.translate("Dialog", "j", None, QtGui.QApplication.UnicodeUTF8))
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    BarraDialog = BarraDialog()
    sys.exit(app.exec_())
