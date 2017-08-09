

globalobjectkeys={'1':0,'2':1,'3':2,'4':3}
globalactionkeys={'q':0,'w':1,'e':2,'r':3}

globalobjectvals=['1','2','3','4','5','6','7','8']
globalactionvals=['q','w','e','r','t','y','u','i']

currentobjectkeys={'a':0,'s':1,'d':2,'f':3}
currentactionkeys={'z':0,'x':1,'c':2,'v':3}

currentobjectvals=['a','s','d','f','g','h','j','k']
currentactionvals=['z','x','c','v','b','n','m',',']


def getObj(char):
	if char in globalobjectkeys:
		if 'objects' in data['global']:
			if len(data['global']['objects']) >= globalobjectkeys[char]:
				return data['global']['objects'][globalobjectkeys[char]]
	if char in globalactionkeys:
		if 'actions' in data['global']:
			if len(data['global']['actions']) >= globalactionkeys[char]:
				act = ''
				i = 0
				for a in data['global']['actions']:
					act = a
					if i == globalactionkeys[char]:
						break
					i+=1
				return act				

	if char in currentobjectkeys:
		if 'objects' in data[focus[-1]]:
			if len(data[focus[-1]]['objects']) >= currentobjectkeys[char]:
				return data[focus[-1]]['objects'][currentobjectkeys[char]]
	if char in currentactionkeys:
		if 'actions' in data[focus[-1]]:
			if len(data[focus[-1]]['actions']) >= currentactionkeys[char]:
				act = ''
				i = 0
				for a in data[focus[-1]]['actions']:
					act = a
					if i == currentactionkeys[char]:
						break
					i+=1
				return act				
	return ''
	

def printObj():
	invenstr=''
	availstr=''
	retstr = ''
	if 'objects' in data['global']:
		for i in range(0, len(data['global']['objects'])):
			invenstr+=globalobjectvals[i]+': '+data['global']['objects'][i] +', '

	if len(invenstr) > 2:
		invenstr=invenstr[:-2]
	retstr += invenstr + "\n"
	invenstr = ''

	i = 0
	if 'actions' in data['global']:
		for act in data['global']['actions']:
			invenstr+=globalactionvals[i]+': '+act+', '
			i+=1


	if len(invenstr) > 2:
		invenstr=invenstr[:-2]
	retstr += invenstr + "\n"
			
	if 'objects' in data[focus[-1]]:
		for i in range(0, len(data[focus[-1]]['objects'])):
			availstr+=currentobjectvals[i]+': '+data[focus[-1]]['objects'][i] +', '

		if len(availstr) > 2:
			availstr=availstr[:-2]
		retstr += availstr + "\n"
		availstr=''

	if 'actions' in data[focus[-1]]:
		i = 0
		for act in data[focus[-1]]['actions']:
			availstr+=currentactionvals[i]+': '+act+', '
			i+=1

		if len(availstr) > 2:
			availstr=availstr[:-2]
		retstr += availstr

	return retstr

def charrunfunc(action):
	if action['_func']=='move' or action['_func']=='delete':
		focuspop()
	runfunc(action)

def charrunaction(action):
	if type(action) is list:
		for i in range(0, len(action)):
			charrunfunc(action[i])
	else:
		charrunfunc(action)

def charobjAction(obj, act):
	if 'actions' in data[obj]:
		if act in data[obj]['actions']:
			charrunaction(data[obj]['actions'][act])
			focuspush(obj)
			return True
	if 'actions' in data['global']:
		if act in data['global']['actions']:
			focuspush(obj)
			charrunaction(data['global']['actions'][act])
			#focuspop()
			return True
	return False

def charobjObject(focus, obj, act):
	if 'objects' in data[focus]:
		if obj in data[focus]['objects']:
			if not obj in data:
				Print( 'error' )
				return True
			if charobjAction(obj, act):
				return True

	if 'actions' in data[focus]:
		if obj in data[focus]['actions']:
			charrunaction(data[focus]['actions'][obj])
			#focuspush(obj)
			return True
	return False

def processchar(inputchar):
	#processinput(getObj(inputchar))
	inputstr = getObj(inputchar)

#def processinput(inputstr):
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

	if charobjObject('global', obj, act):
		return
	if charobjObject(focus[-1], obj, act):
		return
		
