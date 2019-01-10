class vector_expr(object):
	def __init__(self, exprs):
		self.exprs = exprs
		
	def compile(self, func, assignto):
		vars = []
		for i in range(3):
			var = calc_math(func, self.exprs[i], None if assignto == None else assignto[i])
				
			if var == None:
				return None
				
			vars.append(var)
		
		return vars
