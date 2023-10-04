import tkinter

root = tkinter.Tk()
root.title('Menu Practice')
root.geometry('260x200')
root.resizable(False, False)


def open_setting():
    subwindow = tkinter.Toplevel()
    subwindow.title('setting')
    subwindow.geometry('200x100')

    subwindow_label = tkinter.Label(subwindow, text='This is setting window')
    subwindow_label.pack()


menubar = tkinter.Menu(root)
root.config(menu=menubar)

setting_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='settings', menu=setting_menu)

file_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='file', menu=file_menu)

setting_menu.add_command(label='setting', command=open_setting)
setting_menu.add_command(label='exit')

file_menu.add_command(label='new file')

button_1 = tkinter.Button(root, text='out put')
button_1.grid(row=0, column=0, padx=100, pady=70, ipadx=10)

root.mainloop()
