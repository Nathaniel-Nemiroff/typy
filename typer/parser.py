inputfile = open('ezpzrooms.dat')

def rmvwhite(string):
	index=0
	for i in range(0, len(string)):
		if string[i]==' ' or string[i]=='\t' or string[i]=='\n':
			index += 1
		else:
			break
	for i in range(len(string)-1, -1, -1):
		if not string[i]==' ' and not string[i]=='\t' and not string[i]=='\n':
			return string[index:i+1]
	return ''

def	parse1(string):
	retobj={}
	retarr=[]
	name=''
	index=0
	curl=0
	for i in range(0, len(string)):
		if string[i]=='{':
			curl += 1
			if len(name) < 1:
				name = rmvwhite(string[index:i])
				index=i+1
		elif string[i]=='}':
			curl -= 1
			if curl == 0:
				retobj[name]=parse(rmvwhite(string[index:i]))
				index=i+1
				name=''
		elif string[i]==',':
			if curl == 0:
				retarr.append(rmvwhite(string[index:i]))
				index=i+1

def buildObj(string):
	retobj={}
	name=''
	index=0
	curl=0
	for i in range(0, len(string)):
		if string[i]=='{':
			curl+=1
			if len(name)<1:
				name=rmvwhite(string[index:i])
				index=i+1
		elif string[i]=='}':
			curl-=1
			if curl==0:
				retobj[name]=parse(rmvwhite(string[index:i]))
				index=i+1
				name=''

	return retobj

def buildArr(string):
	retArr=[]
	index=0
	curl=0
	addtolast=False
	for i in range(0, len(string)):
		if string[i]=='(':
			if curl == 0:
				if i < 1:
					return 'err'
				if string[i-1]==' ' or string[i-1]=='\n' or string[i-1]=='\t':
					if len(retArr) < 1:
						return 'err'
					if retArr[-1][-1]==')':
						return 'err'
					addtolast=True
			curl+=1
		elif string[i]==')':
			curl-=1
		elif string[i]==' ':
			if curl == 0:
				if addtolast:
					retArr[-1]+=rmvwhite(string[index:i])
				else:
					retArr.append(rmvwhite(string[index:i]))
				index = i+1
	if not curl == 0:
		return 'err'
	retArr.append(rmvwhite(string[index:len(string)]))

	index = -1
	for i in range(0, len(retArr)):
		for j in range(0, len(retArr[i])):
			if retArr[i][j]=='(':
				retArr[i]={'_func':rmvwhite(retArr[i][:j]),
									 '_param':rmvwhite(retArr[i][j+1:-1])}
				break

	return retArr


def parse(string):
	for i in range(0,len(string)):
		if string[i] == '{':
			return buildObj(string)
		if string[i] =='"':
			return string[1:-1]
	return buildArr(string)
			

	if retarr:
		return retarr
	if index == 0:
		return string

	return retobj

#print parse('globle{blah} static{stuff}realTest{objects[ anObject{ some stuff here } ]actions[ anAction{ do stuff here } ]}');

parsestring = ''
for line in inputfile:
	parsestring += line

data = parse(parsestring)

inputfile.close()
