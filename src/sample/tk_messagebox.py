import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title('Messagebox Practice')
root.geometry('300x450')
root.resizable(False, False)


def show_message():
    messagebox.showinfo('infomation', 'This is infomation.')


def show_error():
    messagebox.showerror('error', 'This is error.')


def show_warning():
    messagebox.showwarning('warning', 'This is warning.')


def ask_yesno():
    yesno = messagebox.askyesno('question', 'Are you going to close this window realy?')
    print(yesno)
    if yesno == True:
        root.destroy()


def ask_question():
    answer = messagebox.askquestion('question', 'Would you like to execute it.?')
    print(answer)


def ask_cancel():
    answer = messagebox.askokcancel('cancel', 'Will you cancel it?')
    print(answer)


def ask_retry():
    answer = messagebox.askretrycancel('retry', 'Would you like to retry?')
    print(answer)


button_1 = tkinter.Button(root, text='infomation', command=show_message)
button_2 = tkinter.Button(root, text='error', command=show_error)
button_3 = tkinter.Button(root, text='caution', command=show_warning)
button_4 = tkinter.Button(root, text='yesno question', command=ask_yesno)
button_5 = tkinter.Button(root, text='question', command=ask_question)
button_6 = tkinter.Button(root, text='cancel question', command=ask_cancel)
button_7 = tkinter.Button(root, text='retry question', command=ask_retry)

button_1.grid(row=0, column=0, padx=100, pady=30, ipadx=10)
button_2.grid(row=1, column=0, padx=100, pady=(0, 30), ipadx=10)
button_3.grid(row=2, column=0, padx=100, pady=(0, 30), ipadx=10)
button_4.grid(row=3, column=0, padx=100, pady=(0, 30), ipadx=10)
button_5.grid(row=4, column=0, padx=100, pady=(0, 30), ipadx=10)
button_6.grid(row=5, column=0, padx=100, pady=(0, 30), ipadx=10)
button_7.grid(row=6, column=0, padx=100, pady=(0, 30), ipadx=10)

root.mainloop()
