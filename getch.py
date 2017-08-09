import os

class _Getch:
	"""gets a single character from standardinput.  Does not echo to the screen."""
	def __init__(self):
		try:
			self.impl = _GetchWindows()
		except ImportError:
			self.impl = _GetchUnix()

	def __call__(self): return self.impl()

class _GetchUnix:
	def __init__(self):
		import tty, sys

	def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

class _GetchWindows:
	def __init__(self):
		import msvcrt

	def __call__(self):
		import msvcrt
		return msvcrt.getch()

getch = _Getch()

def clear():
	try:
		os.system('clear')
	except:
		os.system('cls')

def countRows(string, columns):
	col = 0
	retrows = 1;
	for i in range(0, len(string)):
		col = col + 1
		if string[i] == '\n':
			col = 0
			retrows = retrows + 1
		if col > columns:
			col = 0
			retrows = retrows + 1
	return retrows

def splitPrint(string1, string2):
	rows, columns = os.popen('stty size', 'r').read().split()
	displacement1 = countRows(string1, columns)
	displacement2 = countRows(string2, columns)
	if displacement1 + displacement2 > rows:
		print "window is too small, please resize before continuing"
		return
	print string1
	for i in range(0, int(rows) - (displacement1+displacement2) - 1):
		print
	'''
	print "-------------"
	print displacement1
	print displacement2
	print "-------------"
	'''
	
	print string2
	
