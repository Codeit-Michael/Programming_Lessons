from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('text editor')
root.geometry('400x500')

named = []

def open_file():
	text_file = filedialog.askopenfile(initialdir='/home/michael/Desktop/Programming/Simple_Projects/text_editor_app',title='Select File',filetypes=(('text files','*.txt'),('all files','*.*')))
	fulldir = text_file.name
	filename = fulldir.split('/')
	global named
	named.append(filename[-1])
	textfile = open(filename[-1],'r')
	openit = textfile.read()
	text.insert(END, openit)
	textfile.close()	

def save_file():
	if len(named) == 0:
		None
	else:
		text_file = open(named[-1],'w')
		text_file.write(text.get(1.0,END))
		text_file.close()

def killIt():
	global root
	root.destroy()

text = Text(root,height=27,width=48,bg='grey')
text.place(relx=0.01,rely=0.06)

openfile = Button(root,text='Open File',height=1,width=5,bg='orange',activebackground='yellow',command=open_file)
openfile.place(relx=0.19)

save = Button(root,text='Save File',height=1,width=5,bg='orange',activebackground='yellow',command=save_file)
save.place(relx=0.01)

exit = Button(root,text='Exit',height=1,width=5,bg='brown',activebackground='red',command=killIt)
exit.place(relx=0.37)

root.mainloop()