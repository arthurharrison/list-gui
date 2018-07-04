#TODO: I Hate TODO, but, I will keep this format and work on filenavigation.py and finish this script by having guitest.py as a reference
import tkinter as tk
from tkinter import ttk#,Scrollbar ,Text , Menu, messagebox
from tkinter import *

class Culture:


	def __init__(self):
		print('hai')
		self.win = tk.Tk()


		#Will config the win
		self.win.title('List Saver')
		self.win.iconbitmap('icon.ico')
		self.win.minsize(260,110)
		self.win.maxsize(261,111)

		#Initializing body vars
		#to know: lambda will make buttonclicked accept parameters in command
		self.name = tk.StringVar()
		self.nameEntered = ttk.Entry(self.win, width = 42,textvariable=self.name)
		self.action = ttk.Button(self.win, text='Movies', command = lambda: self.buttonClicked(8))
		self.action2 = ttk.Button(self.win, text='Books', command = lambda: self.buttonClicked(8))
		self.action3 = ttk.Button(self.win, text='Graphic Novels', command = self.newWindow)
		self.action4 = ttk.Button(self.win, text='Read Mvs', command = lambda: self.buttonClicked(8))
		self.action5 = ttk.Button(self.win, text='Read Bks', command = lambda: self.buttonClicked(8))
		self.action6 = ttk.Button(self.win, text='Read HQ', command = lambda: self.buttonClicked(8))


		#will call the methods that does everything
		self.createMenu()

	def createMenu(self):
		menuBar= Menu(self.win)
		self.win.config(menu=menuBar)
		#Top Menu configuration
		optionsMenu= Menu(menuBar, tearoff=0)
		optionsMenu.add_command(label='Remove')
		optionsMenu.add_command(label='Path Config')
		optionsMenu.add_separator()
		optionsMenu.add_command(label='Exit',command=self._quit)
		menuBar.add_cascade(label='Options', menu=optionsMenu)

		helpMenu = Menu(menuBar, tearoff=0)
		helpMenu.add_command(label='About', command=self._aboutBox)
		menuBar.add_cascade(label='Help', menu=helpMenu)


		labelInfo=ttk.Label(self.win, text = "Enter Name:").grid(column=0,row=0)

		self.nameEntered.focus()
		self.nameEntered.grid(column=0,row=1)
		self.action.place(x=5,y=45)
		self.action2.place(x=85,y=45)
		self.action3.place(x=165,y=45)
		self.action4.place(x=5,y=75)
		self.action5.place(x=85,y=75)
		self.action6.place(x=172,y=75)






	#---Top Menu Commands
	def _quit(self):
		self.win.quit()
		self.win.destroy()
		exit()

	def newWindow(self, text = 'beep boop'):
		#make it a list? how will it display? will i really use this method?
		window = tk.Tk()
		window.iconbitmap('icon.ico')
		window.title('new Window')
		scroll = Scrollbar(window)
		textB = Text(window, height=4, width=50)
		scroll.pack(side=RIGHT, fill=Y)
		textB.pack(side=LEFT, fill=Y)
		scroll.config(command=textB.yview)
		textB.config(yscrollcommand=scroll.set)
		textB.insert(END, text)
		#label = ttk.Label(window, text= text)
		#label.pack()
		window.mainloop()

	def _aboutBox(self):
		messagebox.showinfo('Author info', 'This was developed by Arthur Harrison\nLast Updated: June 2018')

	def _errorBox(self, type=0):
		if(type==0):
			messagebox.showerror('Error','Dev Error/Dev work in progress')
		elif(type==1):
			messagebox.showwarning('Error','This already exists!')
		else:
			messagebox.showerror('Sorry',"This wasn't supossed to happen :(")

	#----Handler
	def buttonClicked(self, action=0):
		tempText = self.name.get().lower() #lower to check if it already exists, but saves normally
		if(action == 0):
			#salvar info de movies
			self.action.configure(text= "Done!" + self.name.get())
			self.nameEntered.delete(0,'end')
			self.nameEntered.focus()
		elif(action == 1):
			#salvar info de books
			print('bahia')
		elif(action == 2):
			#salvar info de graphic novels
			print('bahia')
		elif(action == 3):
			#ler movies
			print('bahia')
		elif(action == 4):
			#ler Books
			print('bahia')
		elif(action == 5):
			#ler graphic novels
			print('bahia')
		else:
			#nunca deve acontecer
			self._errorBox(0)



starter = Culture()
starter.win.mainloop()
