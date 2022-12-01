import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class MyNotes:
	__root=Tk()

	# set default window width and height
	__myWidth=300
	__myHeight=300
	__textArea=Text(__root)
	__menuBar=Menu(__root)
	__fileMenu=Menu(__menuBar, tearoff=0)
	__editMenu=Menu(__menuBar, tearoff=0)
	__helpMenu=Menu(__menuBar, tearoff=0)

	# add scrollbar 
	__scroll=Scrollbar(__textArea)
	__file=None


	# constructor
	def __init__(self,**kwargs):
		#set an icon 
		try:
			self.__root.wm_iconbitmap("Notepad.ico")
		except:
			pass

		# set window size ( if any parameter passed )
		try:
			self.__myWidth=kwargs['width']
		except KeyError:
			pass

		try:
			self.__myHeight=kwargs['height']
		except KeyError:
			pass

		# set the window text 
		self.__root.title("Untitled - MyNotes")

		#center the window
		screenWidth=self.__root.winfo_screenwidth()
		screenHeight=self.__root.winfo_screenheight()

		# left align 
		left=(screenWidth/2)-(self.__myWidth/2)
		top=(screenHeight/2)-(self.__myHeight/2)

		# for top and bottom
		self.__root.geometry('%dx%d+%d+%d'%(self.__myWidth,self.__myHeight,left,top))

		# make text area auto resizable
		self.__root.grid_rowconfigure(0,weight=1)
		self.__root.grid_columnconfigure(0,weight=1)

		# add Controls 
		self.__textArea.grid(sticky=N+E+S+W)

		# to open new file 
		self.__fileMenu.add_command(label="New File", command=self.__newFile)

		# to open existing file 
		self.__fileMenu.add_command(label="Open File", command=self.__openFile)

		# to save current file
		self.__fileMenu.add_command(label="Save", command=self.__saveFile)

		# add a seperator in menu 
		self.__fileMenu.add_separator()

		# add exit option
		self.__fileMenu.add_command(label="Exit", command=self.__quitApplication)
		self.__menuBar.add_cascade(label="File",menu=self.__fileMenu)

		# cut option

		self.__editMenu.add_command(label="Cut", command=self.__cut)
		self.__editMenu.add_command(label="Copy", command=self.__copy)
		# paste option 
		self.__editMenu.add_command(label="Paste", command=self.__paste)

		# add it to menubar
		self.__menuBar.add_cascade(label="Edit", menu=self.__editMenu)

		# create help menu
		self.__helpMenu.add_command(label="About MyNotes",command=self.__showAbout)
		self.__menuBar.add_cascade(label="Help", menu=self.__helpMenu)

		self.__root.config(menu=self.__menuBar)

		self.__scroll.pack(side=RIGHT, fill=Y)

		self.__scroll.config(command=self.__textArea.yview)

		self.__textArea.config(yscrollcommand=self.__scroll.set)

	def run(self):
		self.__root.mainloop()

	def __quitApplication(self):
		self.__root.destroy()

	def __showAbout(self):
		showinfo("My Notes ", "Developed by Abhishek Gautam using Python and Tkinter library.\n This uses os module to interact with file system.")

	def __openFile(self):
		self.__file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
		if self.__file=="":
			self.__file=None
		else:
			self.__root.title(os.path.basename(self.__file)+" - My Notes")
			self.__textArea.delete(1.0,END)
			file=open(self.__file,"r")
			self.__textArea.insert(1.0,file.read())
			file.close()

	def __newFile(self):
		self.__root.title("Untitled - My Notes")
		self.__file=None
		self.__textArea.delete(1.0,END)

	def __saveFile(self):
		if self.__file==None:
			self.__file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
			if self.__file=="":
				self.__file=None
			else:
				file=open(self.__file,"w")
				file.write(self.__textArea.get(1.0,END))
				file.close()
				self.__root.title(os.path.basename(self.__file)+" - My Notes")

		else:
			file=open(self.__file,"w")
			file.write(self.__textArea.get(1.0,END))
			file.close()

	def __cut(self):
		self.__textArea.event_generate("<<Cut>>")
	def __copy(self):
		self.__textArea.event_generate("<<Copy>>")
	def __paste(self):
		self.__textArea.event_generate("<<Paste>>")


if __name__ == '__main__':
	notepad=MyNotes(width=600,height=400)
	notepad.run()
