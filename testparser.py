#from PIL import Image
#from appJar import gui
from tkinter import *
import re
inputfile = open('example.dat')

'''
for line in inputfile:
	for char in line:
		if not char=='\n' and not char=='\t' and not char=='\s':
			print '---'
			print char
			print '+++'
		else:
			print '|||||'
	#print '-------------------------'
	#print line
	#print '-------------------------'
'''
for line in inputfile:
	print re.split('\s \n \t', line)

inputfile.close()

'''
img = cv2.imread('img.jpg',0)
cv2.imgshow('image', img)
cv2.waitkey(0)
cv2.destroyAllWindows()
'''

#image = Image.open('safe.png')
#image.show();

'''
app = gui()
app.appLabel('title', 'welcome to this')
app.setLabelBG('bgtitle', 'red')

app.go()
'''
