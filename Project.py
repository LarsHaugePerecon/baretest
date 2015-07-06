# Import everything from matplotlib (numpy is accessible via 'np' alias)
from pylab import *
import Tkinter as Tk
import numpy as np
import pandas as pd

import csv
import string

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

# Input file
inputpath = 'C:\\Users\\Lars Petter\\'
filename = 'resultsPROTOTYPE_2_SUMMARY.CSV'
sum_filename = inputpath+filename

# Writing something new

print("Opening file: "+sum_filename)

#!/usr/bin/env python --------------------------------------
root = Tk.Tk()
root.wm_title("Plotting Generated simulation cases")

# Create a new figure of size 8x6 points, using 80 dots per inch
f=figure(figsize=(10,6), dpi=80)

# Create a new subplot from a grid of 1x1
a = f.add_subplot(1,1,1)

ListKey1=6
ListKey2=6

def changelistkey1(var):
	global ListKey1
	ListKey1=ListKey1+var

def changelistkey2(var):
	global ListKey2
	ListKey2=ListKey2+var

def PlotXNext():
	var=1
	varg=1
	Plot(var,varg)
	
def PlotXBack():
	var=1
	varg=-1
	Plot(var,varg)
	
def PlotYNext():
	var=2
	varg=1
	Plot(var,varg)
	
def PlotYBack():
	var=2
	varg=-1
	Plot(var,varg)
	
def Plot(axis,direction):
	if axis==1:
		changelistkey1(direction)
	else:
		changelistkey2(direction)
	xcolname=df.columns[ListKey1]
	ycolname=df.columns[ListKey2]
	PlotDataXAxis = df[xcolname] #you can also use df['column_name']
	PlotDataYAxis = df[ycolname]
	PlotData(PlotDataXAxis,PlotDataYAxis,xcolname,ycolname)

def PlotData(X,Y,XLabel,YLabel):
	a.clear()
	a.scatter(X, Y)
	a.set_xlabel(XLabel)
	a.set_ylabel(YLabel)
	canvas.show()
	
with open(sum_filename) as csv_file: #Do I need to close this?
		df = pd.read_csv(csv_file)

# tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

def hello():
    print "hello!"

def DropDownXCall():
	print ("Value: "+DropDownX.get())

# create a toplevel menu
menubar = Tk.Menu(root)
menubar.add_command(label="File", command=hello)
menubar.add_command(label="Quit!", command=_quit)

# display the menu
root.config(menu=menubar)

#Drop down menu
variable = Tk.StringVar(root)
variable.set("one") # default value

Value="one", "two", "three"

DropDownX = Tk.OptionMenu(root, variable,"one", "two", "three")
DropDownX.pack()

# Create buttons
button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)

buttonNextX = Tk.Button(master=root, text='Next', command=PlotXNext)
buttonNextX.pack(side=Tk.BOTTOM)

buttonNextY = Tk.Button(master=root, text='Next', command=PlotYNext)
buttonNextY.pack(side=Tk.LEFT)

buttonBackX = Tk.Button(master=root, text='Back', command=PlotXBack)
buttonBackX.pack(side=Tk.BOTTOM)

buttonBackY = Tk.Button(master=root, text='Back', command=PlotYBack)
buttonBackY.pack(side=Tk.LEFT)

Tk.mainloop()
