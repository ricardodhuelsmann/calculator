# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# Author: Ricardo Dagnoni Huelsmann

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(500, 820)
        Calculator.setMinimumSize(QtCore.QSize(500, 820))
        Calculator.setMaximumSize(QtCore.QSize(500, 820))
        Calculator.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.visor_frame = QtWidgets.QFrame(self.centralwidget)
        self.visor_frame.setMaximumSize(QtCore.QSize(16777215, 180))
        self.visor_frame.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.visor_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.visor_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.visor_frame.setObjectName("visor_frame")
        self.visor = QtWidgets.QLabel(self.visor_frame)
        self.visor.setGeometry(QtCore.QRect(49, 39, 411, 101))
        self.visor.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.visor.setFont(font)
        self.visor.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(175, 175, 175);\n"
"border-radius: 15px;")
        self.visor.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.visor.setLineWidth(1)
        self.visor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.visor.setObjectName("visor")
        self.frame = QtWidgets.QFrame(self.visor_frame)
        self.frame.setGeometry(QtCore.QRect(30, 19, 451, 141))
        self.frame.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(175, 175, 175);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.visor.raise_()
        self.verticalLayout.addWidget(self.visor_frame)
        self.teclas_frame = QtWidgets.QFrame(self.centralwidget)
        self.teclas_frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.teclas_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.teclas_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.teclas_frame.setObjectName("teclas_frame")
        self.clearButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.clique("C"))
        self.clearButton.setGeometry(QtCore.QRect(20, 20, 220, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("background-color: rgb(255, 105, 105);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.clearButton.setObjectName("clearButton")
        self.multiplyButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.multiplicacao())
        self.multiplyButton.setGeometry(QtCore.QRect(260, 20, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.multiplyButton.setObjectName("multiplyButton")
        self.divisionButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.divisao())
        self.divisionButton.setGeometry(QtCore.QRect(380, 20, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.divisionButton.setFont(font)
        self.divisionButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.divisionButton.setObjectName("divisionButton")
        self.sevenButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.clique("7"))
        self.sevenButton.setGeometry(QtCore.QRect(20, 140, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.sevenButton.setFont(font)
        self.sevenButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.clique("8"))
        self.eightButton.setGeometry(QtCore.QRect(140, 140, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.eightButton.setFont(font)
        self.eightButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.clique("9"))
        self.nineButton.setGeometry(QtCore.QRect(260, 140, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.nineButton.setFont(font)
        self.nineButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.nineButton.setObjectName("nineButton")
        self.addButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.soma())
        self.addButton.setGeometry(QtCore.QRect(380, 140, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.addButton.setObjectName("addButton")
        self.fourButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.clique("4"))
        self.fourButton.setGeometry(QtCore.QRect(20, 260, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.fourButton.setFont(font)
        self.fourButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.fourButton.setObjectName("fourButton")
        self.oneButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.clique("1"))
        self.oneButton.setGeometry(QtCore.QRect(20, 380, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.oneButton.setFont(font)
        self.oneButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.oneButton.setObjectName("oneButton")
        self.threeButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.clique("3"))
        self.threeButton.setGeometry(QtCore.QRect(260, 380, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.threeButton.setFont(font)
        self.threeButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.threeButton.setObjectName("threeButton")
        self.fiveButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.clique("5"))
        self.fiveButton.setGeometry(QtCore.QRect(140, 260, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.fiveButton.setFont(font)
        self.fiveButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.fiveButton.setObjectName("fiveButton")
        self.sixButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.clique("6"))
        self.sixButton.setGeometry(QtCore.QRect(260, 260, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.sixButton.setFont(font)
        self.sixButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.sixButton.setObjectName("sixButton")
        self.equalButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.igual())
        self.equalButton.setGeometry(QtCore.QRect(380, 380, 100, 221))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.equalButton.setFont(font)
        self.equalButton.setStyleSheet("background-color: rgb(255, 155, 55);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.equalButton.setObjectName("equalButton")
        self.twoButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.clique("2"))
        self.twoButton.setGeometry(QtCore.QRect(140, 380, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.twoButton.setFont(font)
        self.twoButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.twoButton.setObjectName("twoButton")
        self.plusminusButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.mais_menos())
        self.plusminusButton.setGeometry(QtCore.QRect(140, 500, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.plusminusButton.setObjectName("plusminusButton")
        self.decimalButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.virgula())
        self.decimalButton.setGeometry(QtCore.QRect(260, 500, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.decimalButton.setFont(font)
        self.decimalButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.decimalButton.setObjectName("decimalButton")
        self.zeroButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.clique("0"))
        self.zeroButton.setGeometry(QtCore.QRect(20, 500, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.zeroButton.setFont(font)
        self.zeroButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.zeroButton.setObjectName("zeroButton")
        self.subButton = QtWidgets.QPushButton(self.teclas_frame, clicked=lambda: self.subtracao())
        self.subButton.setGeometry(QtCore.QRect(380, 260, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.subButton.setFont(font)
        self.subButton.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(230, 230, 230);\n"
"border-radius: 15px;")
        self.subButton.setObjectName("subButton")
        self.verticalLayout.addWidget(self.teclas_frame)
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def soma(self):
    	global valor_inicial
    	global operacao
    	operacao = "+"
    	valor_inicial = self.visor.text()
    	self.visor.setText("+")

    def subtracao(self):
    	global valor_inicial
    	global operacao
    	operacao = "-"
    	valor_inicial = self.visor.text()
    	self.visor.setText("-")

    def divisao(self):
    	global valor_inicial
    	global operacao
    	operacao = "/"
    	valor_inicial = self.visor.text()
    	self.visor.setText("/")

    def multiplicacao(self):
    	global valor_inicial
    	global operacao
    	operacao = "*"
    	valor_inicial = self.visor.text()
    	self.visor.setText("*")

    def igual(self):
    	global valor_final
    	valor_final = self.visor.text()
    	valor_numerico_inicial = float(valor_inicial)
    	valor_numerico_final = float(valor_final)
    	if operacao == "+":
    		resposta = valor_numerico_inicial + valor_numerico_final
    	elif operacao == "-":
    		resposta = valor_numerico_inicial - valor_numerico_final
    	elif operacao == "/":
    		resposta = valor_numerico_inicial/valor_numerico_final
    	elif operacao == "*":
    		resposta = valor_numerico_inicial*valor_numerico_final
    	#if resposta%10

    	self.visor.setText(str(resposta))

    
   
    #Cria função +/-
    def mais_menos(self):
    	valor_inicial_tela = self.visor.text()
    	valor_final_tela = str(float(valor_inicial_tela)*(-1))
    	self.visor.setText(valor_final_tela)


    # Adiciona a vírgula
    def virgula(self):
        valor_tela = self.visor.text()
        if "." in valor_tela:
            pass
        else:
            self.visor.setText(f'{valor_tela}.') 

    def clique(self, botao):
        if botao == "C":
            self.visor.setText("0")
        else:
            # Primeiro, checa-se se o valor está zerado e limpa
            if self.visor.text() == "0":
                self.visor.setText("")
            # Se foi adicionado uma conta, zera o visor antes de adicionar o próximo
            if self.visor.text() == ("+") or self.visor.text() == ("-") or self.visor.text() == ("*") or self.visor.text() == ("/"):
            	self.visor.setText("")
            # Concatena o valor com o que está sendo adicionado
            self.visor.setText(f'{self.visor.text()}{botao}')

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.visor.setText(_translate("Calculator", "0"))
        self.clearButton.setText(_translate("Calculator", "C"))
        self.multiplyButton.setText(_translate("Calculator", "X"))
        self.divisionButton.setText(_translate("Calculator", "/"))
        self.sevenButton.setText(_translate("Calculator", "7"))
        self.eightButton.setText(_translate("Calculator", "8"))
        self.nineButton.setText(_translate("Calculator", "9"))
        self.addButton.setText(_translate("Calculator", "+"))
        self.fourButton.setText(_translate("Calculator", "4"))
        self.oneButton.setText(_translate("Calculator", "1"))
        self.threeButton.setText(_translate("Calculator", "3"))
        self.fiveButton.setText(_translate("Calculator", "5"))
        self.sixButton.setText(_translate("Calculator", "6"))
        self.equalButton.setText(_translate("Calculator", "="))
        self.twoButton.setText(_translate("Calculator", "2"))
        self.plusminusButton.setText(_translate("Calculator", "+-"))
        self.decimalButton.setText(_translate("Calculator", ","))
        self.zeroButton.setText(_translate("Calculator", "0"))
        self.subButton.setText(_translate("Calculator", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
