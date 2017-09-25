import re
import sympy as sp
from balancing import *
from brackets import *

lista = []

expr = str(raw_input("Type your expression:\n"))
try:
	a1 = just_par(expr)

	if not a1.check(): 
		a = balance(expr)
		if a.check():
			for item in re.findall("\s*(?:(\d+)|(\w+)|(.))",expr): 
				if item[1]: 
					lista.append(item[1])

			for var in lista:
				var = sp.symbols(""+str(var))

			regular = sp.sympify(expr)
			print regular

		else:
			print "Please, check your parenthese!"
	else:
		print "Please, just use parentheses!"
except:
	print "Please, check your syntax!"
