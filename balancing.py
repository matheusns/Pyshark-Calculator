from Stack import *

class balance (Stack):
	
	def __init__(self, sequencia):
		self.lista = sequencia
	def check(self):
    		s = Stack()
    		balanced = True
    		index = 0
		cont = 0
    		while index < len(self.lista) and balanced:
        		symbol = self.lista[index]
        		if symbol == "(":
            			s.push(symbol)
        		elif symbol == ")":
            			if s.isEmpty():
                			balanced = False
					
            			else:
                			s.pop()

    		    	index = index + 1
		

    		if balanced and s.isEmpty():
    			return True
  		else:
        		return False
