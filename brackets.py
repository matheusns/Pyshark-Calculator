class just_par:
	def __init__(self,expr):
		
		self.string = expr
	def check(self):
		for i in xrange(0,len(self.string)):
			if self.string[i] == "[":
				return True
			if self.string[i] == "]":
				return True
			if self.string[i] == "{":
				return True
			if self.string[i] == "}":
				return True
		return False
			
