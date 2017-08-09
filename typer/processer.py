exit = False
focus = ['global']
outputString = ''

def Print(string):
	global outputString
	outputString += string + "\n"
def current(obj):
	global focus
	focus = [obj]
def focuspush(obj):
	global focus
	focus.append(obj)
def focuspop():
	global focus
	if len(focus) > 1:
		focus.pop()
	else:
		Print( 'Cannot go back!' )
def move(params):
	paramsplit=[x for x in params.replace(', ',' ').replace(',',' ').split(' ') if x!= '']
	if len(paramsplit) != 2:
		Print( 'error' )
		return
	if paramsplit[1] in data:
		if 'objects' in data[paramsplit[1]]:
			if paramsplit[0] in data:
				delete(paramsplit[0])
				data[paramsplit[1]]['objects'].append(paramsplit[0])
	
def delete(obj):
	if obj in data:
		if 'objects' in data[focus[-1]]:
			if obj in data[focus[-1]]['objects']:
				data[focus[-1]]['objects'].remove(obj)
				return
		if 'objects' in data['global']:
			if obj in data['global']['objects']:
				data['global']['objects'].remove(obj)
				return

'''
invenkeys={'1':0,'2':1,'3':2,'4':3,
			'q':4,'w':5,'e':6,'r':7}
invenvals=['1','2','3','4','q','w','e','r']
availkeys={'a':0,'s':1,'d':2,'f':3,
			'z':4,'x':5,'c':6,'v':7}
availvals=['a','s','d','f','z','x','c','v']

def getObj(char):
	if char in invenkeys:
		if 'objects' in data['global']:
			if len(data['global']['objects']) >= invenkeys[char]:
				return data['global']['objects'][invenkeys[char]]
	if char in availkeys:
		if 'objects' in data[focus[-1]]:
			if len(data[focus[-1]]['objects']) >= availkeys[char]:
				return data[focus[-1]]['objects'][availkeys[char]]
	return ''
	
def printObj():
	invenstr=''
	availstr=''
	retstr = ''
	if 'objects' in data['global']:
		for i in range(0, len(data['global']['objects'])):
			invenstr+=invenvals[i]+': '+data['global']['objects'][i] +', '
		if len(invenstr) > 2:
			invenstr=invenstr[:-2]
		retstr += invenstr + "\n"
	if 'objects' in data[focus[-1]]:
		for i in range(0, len(data[focus[-1]]['objects'])):
			availstr+=availvals[i]+': '+data[focus[-1]]['objects'][i] +', '
		if len(availstr) > 2:
			availstr=availstr[:-2]
		retstr += availstr
	return retstr
'''


def runfunc(func):
	if func['_func']=='current':
		current(func['_param'])
	elif func['_func']=='takefocus':
		focuspush(func['_param'])
	elif func['_func']=='dropfocus':
		focuspop()
	elif func['_func']=='print':
		Print( func['_param'] )
	elif func['_func']=='move':
		move(func['_param'])
	elif func['_func']=='delete':
		delete(func['_param'])
	elif func['_param'] in data:
		if func['_func'] in data[func['_param']]:
			Print( data[func['_param']][func['_func']] )
	elif func['_func'] in data[focus[-1]]:
		Print( data[focus[-1]][func['_func']] )

def runaction(action):
	if type(action) is list:
		for i in range(0, len(action)):
			runfunc(action[i])
	else:
		runfunc(action)

def objAction(obj, act):
	if 'actions' in data[obj]:
		if act in data[obj]['actions']:
			runaction(data[obj]['actions'][act])
			return True
	if 'actions' in data['global']:
		if act in data['global']['actions']:
			focuspush(obj)
			runaction(data['global']['actions'][act])
			focuspop()
			return True
	return False

def objObject(focus, obj, act):
	if 'objects' in data[focus]:
		if obj in data[focus]['objects']:
			if not obj in data:
				Print( 'error' )
				return True
			if objAction(obj, act):
				return True

	if 'actions' in data[focus]:
		if obj in data[focus]['actions']:
			runaction(data[focus]['actions'][obj])
			return True
	return False

#def processchar(inputchar):
	#processinput(getObj(inputchar))

def processinput(inputstr):
	global outputString
	outputString = ''
	obj=''
	act='default'
	if ' ' in inputstr:
		split = inputstr.split(' ')
		obj = split[1]
		act = split[0]
	else:
		obj=inputstr

	if obj == 'exit':
		global exit
		exit = True
		return

	if objObject('global', obj, act):
		return
	if objObject(focus[-1], obj, act):
		return
		
