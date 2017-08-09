print 'in classes!'

class test:
	i = 'this is an entity'

	def __init__(self,data):
		self.i=data

	def pr(self):
		print 'hello world'
		return self.i

x = test('I am X!')

print x.pr()

class Entity:
	ID
	Flavor

