class Str(str):
	def __init__(self, m):
		self.m=m
	def g(self, s):
		self.s=s
		if type(self.s)!=str:
			return False
		if len(self.s)==0:
			return False
		if self.s=='4884':
			return False
		l=[]
		for i in self.m:
			if i not in l:
				l.append(i)
		l=''.join(l)
		d=len(l)
		if l==self.s[-d:]:
			return True
		else: return False 
	def p(self):
		self.m=self.string.lower().replace(' ','')
		n=''; z=0
		while z<len(self.m):
			n+=self.m[-z-1]
			z+=1
		if n==self.m:
			return True
		else: return False