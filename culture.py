#TODO: I Hate TODO, but, I will keep this format and work on filenavigation.py and finish this script by having guitest.py as a reference
import tkinter as tk
from tkinter import ttk, Menu, messagebox

class Culture:


	def __init__(self):
		print('hai')
		self.win = tk.Tk()
		
		#Will config the win
		self.win.title('List Saver')
		self.win.iconbitmap('icon.ico')
		self.win.minsize(260,110)
		
		#will call the methods that does everything
		self.createMenu()
	
	def createMenu(self):
		menuBar= Menu(self.win)
		self.win.config(menu=menuBar)
		optionsMenu= Menu(menuBar, tearoff=0)
		optionsMenu.add_command(label='Remove')
		optionsMenu.add_command(label='Path Config')
		optionsMenu.add_separator()
		optionsMenu.add_command(label='Exit',command=self._quit)
		menuBar.add_cascade(label='Options', menu=optionsMenu)

		helpMenu = Menu(menuBar, tearoff=0)
		helpMenu.add_command(label='About', command=self._aboutBox)
		menuBar.add_cascade(label='Help', menu=helpMenu)






	#---Top Menu Commands
	def _quit(self):
		self.win.quit()
		self.win.destroy()
		exit()

	def _aboutBox(self):
		messagebox.showinfo('Author info', 'This was developed by Arthur Harrison\nLast Updated: June 2018')

	def _errorBox(self, type=0):
		if(type==0):
			messagebox.showerror('Error','Dev Error')
		elif(type==1):
			messagebox.showwarning('Error','This already exists!')
		else:
			messagebox.showerror('Sorry',"This wasn't supossed to happen :(")



starter = Culture()
starter.win.mainloop()