import os

#inputfile = open('ezpzrooms.dat')
execfile('parser.py')
execfile('processer.py')
execfile('charprocesser.py')
execfile('getch.py')

def charloop(data):
	global outputString
	global exit
	if not 'actions' in data[focus[-1]]:
		print 'error'
		return
	runaction(data[focus[-1]]['actions']['start'])
	clear()
	print 'Press any key to begin....'
	getch()
	splitPrint(printObj(), outputString)
	while(not exit):
		ch = getch()
		if ch == chr(27):
			break
		processchar(ch)
		splitPrint(printObj(), outputString)
	
def textloop(data):
	global outputString
	global exit
	if not 'actions' in data[focus[-1]]:
		print 'error'
		return
	runaction(data[focus[-1]]['actions']['start'])
	splitPrint(outputString,'')
	while(not exit):
		inputstr = raw_input('input: ')
		processinput(inputstr)
		splitPrint(outputString,'')

		

#loop(data)

		
print "Play in charmode?[y/N]"
ch = getch()
if ch == 'y' or ch == 'Y':
	charloop(data)
else:
	textloop(data)

clear()
print "thank you for playing!"
