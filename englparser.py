import re

inputfile = open('simple.dat')

'''
for line in inputfile:
	for word in re.split('\t| |\n', line):
		if len(word) > 0:

			#print word.lower()
		#print '-'
'''

def parseEntity(string):
	Parse=string.split('is', 1)
	

def populateEntity(string):
	Entity={}
	Parse=[]
	pass

def populateEntities(strings):
	Entities=[]
	for string in strings:
		Entities.append(populateEntity(string))



objects=[]
objects.append('')

for line in inputfile:
	for char in line:
		if char == '.':
			objects.append('')
		elif char == '"':
			objects.append("'")
		elif not char == '\t' and not char == '\n':
			objects[-1]+=char
		elif len(objects[-1])>1:
			if not objects[-1][-1] == ' ':
				objects[-1]+=' '

print objects


inputfile.close()
