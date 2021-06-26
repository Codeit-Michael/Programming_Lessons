from tkinter import *
from classEngine import *

root = Tk()
root.title('Calculator')
set1 = []
set2 = []
opt = []
num_stack = []
problem = calculator()

# appending chosen numbers
def nums(num):
	num_stack.append(num)
	label.config(text=''.join(num_stack))

# appending chosen operations
def operation(meth):
	for n in num_stack:
		set1.append(n)
	num_stack.clear()
	opt.append(meth)

# solving the problem
def eq():
	for n in num_stack:
		set2.append(n)
	num_stack.clear()
	ans = problem.compute(set1,opt,set2)
	label.config(text=ans)
	set1.clear()
	set2.clear()
	opt.clear()

# deleting latest number appended
def delete():
	if len(num_stack) > 1:
		n = num_stack[-1]
		num_stack.remove(n)
		label.config(text=''.join(num_stack))
	else:
		label.config(text='0')

# terminating the pane
def off():
	global root
	root.destroy()

# canvas
canvas = Canvas(root, height = 350, width = 310, bg = '#585858')
canvas.pack()

# calculator screen display
label = Label(canvas,font = 'Digital',text = 0,height = 2,width = 29,bg = 'light green')
label.place(relx = 0.03,rely = 0.03)

# buttons
button1 = Button(canvas,font = 'Digital',text = '1',height = 2,width = 4,bg = 'brown',activebackground = 'red',command = lambda: nums('1'))
button1.place(relx=0.03,rely=0.2)

button2 = Button(canvas,font = 'Digital',text = '2',height = 2,width = 4,bg = 'brown',activebackground = 'red',command = lambda: nums('2'))
button2.place(relx=0.27,rely=0.2)

button3 = Button(canvas,font = 'Digital',text = '3',height = 2,width = 4,bg = 'brown',activebackground = 'red',command = lambda: nums('3'))
button3.place(relx=0.51,rely=0.2)



button4 = Button(canvas,font = 'Digital',text = '4',height = 2,width = 4,bg = 'brown',activebackground = 'red',command = lambda: nums('4'))
button4.place(relx=0.03,rely=0.36)

button5 = Button(canvas,font = 'Digital',text = '5',height = 2,width = 4,bg = 'brown',activebackground = 'red',command = lambda: nums('5'))
button5.place(relx=0.27,rely=0.36)

button6 = Button(canvas,font = 'Digital',text = '6',height = 2,width = 4,bg = 'brown',activebackground = 'red',command = lambda: nums('6'))
button6.place(relx=0.51,rely=0.36)



button7 = Button(canvas,font = 'Digital',text = '7',height = 2,width = 4,bg = 'brown',activebackground = 'red',command = lambda: nums('7'))
button7.place(relx=0.03,rely=0.52)

button8 = Button(canvas,font = 'Digital',text = '8',height = 2,width = 4,bg = 'brown',activebackground = 'red',command = lambda: nums('8'))
button8.place(relx=0.27,rely=0.52)

button9 = Button(canvas,font = 'Digital',text = '9',height = 2,width = 4,bg = 'brown',activebackground = 'red',command = lambda: nums('9'))
button9.place(relx=0.51,rely=0.52)

buttonDot = Button(canvas,font = 'Digital',text = '.',height = 2,width = 4,bg = 'grey',command = lambda: nums('.'))
buttonDot.place(relx=0.03,rely=0.68)

button0 = Button(canvas,font = 'Digital',text = '0',height = 2,width = 4,bg = 'brown',activebackground = 'red',command = lambda: nums('0'))
button0.place(relx=0.27,rely=0.68)



plus = Button(canvas,font = 'Digital',text = '+',height = 2,width = 4,bg = 'yellow',activebackground = 'orange',command = lambda: operation('+'))
plus.place(relx=0.75,rely=0.2)

minus = Button(canvas,font = 'Digital',text = '-',height = 2,width = 4,bg = 'yellow',activebackground = 'orange',command = lambda: operation('-'))
minus.place(relx=0.75,rely=0.36)

times = Button(canvas,font = 'Digital',text = 'x',height = 2,width = 4,bg = 'yellow',activebackground = 'orange',command = lambda: operation('*'))
times.place(relx=0.75,rely=0.52)

dividedBy = Button(canvas,font = 'Digital',text = '/',height = 2,width = 4,bg = 'yellow',activebackground = 'orange',command = lambda: operation('/'))
dividedBy.place(relx=0.75,rely=0.68)

equals = Button(canvas,font = 'Digital',text = '=',height = 2,width = 4,bg = 'grey',command = eq)
equals.place(relx=0.51,rely=0.68)

DEL = Button(canvas,font = 'Digital',text = 'DEL',height = 2,width = 12,bg = 'green',activebackground = 'dark green',command = delete)
DEL.place(relx=0.5,rely=0.84)

exit = Button(canvas,font = 'Digital',text = 'OFF',height = 2,width = 12,bg = 'green',activebackground = 'dark green',command = off)
exit.place(relx=0.03,rely=0.84)

root.mainloop()
