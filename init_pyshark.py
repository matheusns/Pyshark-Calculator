from PyQt4 import QtCore, QtGui
import sys
from calculator import Ui_MainWindow # Importa todos os recursos graficos do QT
from brackets import *
from balancing import * #Classe responsavel pela analise do balanceamento dos parenteses
import sympy as sp #modulo sympy, responsavel pelo calculo das expressoes
import re #Modulo regular expression, responsavel pela analise lexica das expressoes

class software(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.var_atribuidas={} #Dicionario que contem as variaveis atribuidas
     
    def calcular(self):
   
	try: 
		self.lista = [] #Lista de variaveis
		self.expr_str = str(self.ui.expr.text())
		a1 = just_par(self.expr_str)#Invoca a classe just_par, que analisara a presenca ou nao de brackets e curly brackets
		if not a1.check(): 	
			a = balance(self.expr_str) #invoca a classe responsavel por analisar o balanceamento de parenteses	
			print "var_atribuidas = " + str(self.var_atribuidas) 
			if a.check(): #Metodo responsavel pelo retorno

				for item in re.findall("\s*(?:(\d+)|(\w+)|(.))",self.expr_str): #re.findall faz o processo de analise lexica
					if item[1] == "sqrt": #Impede que "sqrt" seja atribuida como simbolo
						print "none"
					elif item[1]: #analisa a existencia de variaveis
						self.lista.append(item[1]) #adiciona as variaveis a lista
	
				for var in self.lista:
					var = sp.symbols(""+str(var)) #Declara as variaveis encontradas como simbolos
		
				regular = sp.sympify(self.expr_str) #Utiliza a 'expr' e a converte para um objeto sympy
				status = False
				if self.var_atribuidas == {}: #Analisa se ha atribuicoes de variaveis
			
					self.ui.result_list.addItem(str(regular)) #Caso esteja vazia, retorna o valor da expressao para alista
				else:
					status = True
					for obj in self.var_atribuidas: #analisa todas as atribuicoes realizadas no dicionario
						old = regular.subs(obj,self.var_atribuidas.get(obj)) # recebe o valor atual da expressao e substitui cada variavel do dicionario ao seu valor correspondente
						regular = old # Recebe a expressao ja atribuida
				if status:
					self.ui.result_list.addItem(str(regular))
					self.ui.lista.addItem("----------------------------------") # Facilita a vizualizacao das variaveis
				self.ui.result_list.addItem("----------------------------------") # Facilita a vizualizacao dos resultados	
			
			else: #Caso o balanceamento nao esteja correto	
				msg = QtGui.QMessageBox()
				msg.setIcon(QtGui.QMessageBox.Information)
				msg.setText("Please, check the parentheses distribution of the expression!")
				msg.setWindowTitle("Parentheses Match Error")
				ret = msg.exec_()
		else:
				msg = QtGui.QMessageBox()
				msg.setIcon(QtGui.QMessageBox.Critical)
				msg.setText("Please, just use parentheses in your operations!")
				msg.setDetailedText("Do you know, that you can replace brackets and curly brackets by parentheses?\nForgive us, but in the next version you'll able to use all of them!")
				msg.setWindowTitle("You can only use Parentheses")
				ret = msg.exec_()
		self.var_atribuidas = {} #Limpa o dicionario de atribuicoes	
		
	except:
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Critical)
		msg.setText("Please, check the syntax of your expression!")
		#msg.setInformativeText("                            The expression field is blank.")
		msg.setWindowTitle("Something is wrong!")
		msg.setDetailedText("If you need some help, use the examples, find them on the button at the bottom right.")
		ret = msg.exec_()
		self.ui.expr.clear
	
    def atrib(self): #Ate o momento so podemos atribuir a variaveis numeros inteiros
    	try:
		expression = str(self.ui.expr.text()) # Para analisar se existem variaveis correspondentes 
		atribuido = str(self.ui.variaveis.text()) # String com os valores das variaveis
		self.ui.variaveis.clear	
		if not self.ui.expr.text(): # Verifica se o campo "expr" possui algo
			msg = QtGui.QMessageBox()
			msg.setIcon(QtGui.QMessageBox.Critical)
			msg.setText("Please, before assign a value to a variable, insert your expression!")
			msg.setInformativeText("                            The expression field is blank.")
			msg.setWindowTitle("Expression Field Error")
			ret = msg.exec_()		
                elif self.ui.variaveis.text():
			 index = 0 #Controle da ordem de termos
			 status = True #Variavel de Controle para adicao de variaveis
			 tam = len(re.findall("\s*(\d+|\w+|.)",atribuido)) # Recebe a quantidade de termos da expressao de atribuicao
			 #print 	re.findall("\s*(\d+|\w+|.)",atribuido)
			 control = re.findall("\s*(\d+|\w+|.)",atribuido) #Lista com os termos da expressao
			 		 
		         a = software() #cria um objeto da classe atual para referenciar o metodo 'teste()'
			 print "Control= " + str(control)	
			 if tam==3 or tam==4 and control[3] == " ": # Analisa se a expressao possui a quantidade de termos necessarios
				for item in re.findall("\s*(?:(\d+)|(\w+)|(.))",atribuido):
				 									
					if index == 0 and item[1]:
						if a.teste(item[1],expression): #invoca a funcao 'teste ()'
							b = item[1] # Variavel que sera associada ao dicionario	
													
						else: #Caso 'teste()' retorne False
							msg = QtGui.QMessageBox()
							msg.setIcon(QtGui.QMessageBox.Critical)
							msg.setText("Variable not found! Please, insert an existent variable!")
							msg.setWindowTitle("Variable not found!")
							ret = msg.exec_()
							status = False
							break	
					elif index == 1 and item[2]: 
						if item[2] == "=":
							print "muito bem, tem '='!" #Controle de Fluxo
						else:#Caso nao haja atribuicao
							msg = QtGui.QMessageBox()
							msg.setIcon(QtGui.QMessageBox.Critical)
							msg.setText("Please, insert the '=' for assign a value.")
							msg.setWindowTitle("Syntax Assignment Error")
							ret = msg.exec_()
							status = False	
					
					elif index == 2 and item[0]:
						c = item[0] #Valor da variavel que sera associada a chave 'b' do dicionario
					
					index+=1
				if status: #Caso a atribuicao de variaveis esteja correta
					self.var_atribuidas[b] = c #Atribui a variavel encontrada como uma chave ao dicionario e associa ao seu valor atribuido, sera usado na classe calcular 				
					self.ui.variaveis.clear #Limpa o campo de atribuicao
				        self.ui.lista.addItem(self.ui.variaveis.text()) # Adiciona a atribuicao a lista
			 else: # Caso a sintaxe de atribuicao esteja errada
				msg = QtGui.QMessageBox()
				msg.setIcon(QtGui.QMessageBox.Critical)
				msg.setWindowTitle("Something is wrong!")
				msg.setText("Please, check your assigment syntax!")
				msg.setDetailedText("The correct syntax is:variable_name = value")
				ret = msg.exec_()
               	
				
    	except: #Caso algum outro erro nao previsto ocorra no momento da atribuicao
		msg = QtGui.QMessageBox()
		msg.setIcon(QtGui.QMessageBox.Critical)
		msg.setText("Please, check the syntax of your assignment!")
		msg.setWindowTitle("Something is wrong!")
		msg.setDetailedText("If you need some help, use the examples, find them on the button at the bottom right.")
		ret = msg.exec_()
		self.ui.variaveis.clear
    def teste(self,var_teste,expression): #Valida a existencia das variaveis de acordo com a expressao atual 
	
    
    	for item in re.findall("\s*(?:(\d+)|(\w+)|(.))",expression): #Utiliza a analise lexica para comparar as variaveis
		if item[1] == str(var_teste): #Caso exista, retorna True
			return True
	return False
	
        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = software()
    av.show()
    sys.exit(app.exec_())
