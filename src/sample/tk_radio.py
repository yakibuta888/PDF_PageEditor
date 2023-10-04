import tkinter
from tkinter import IntVar


def print_number():
    if number.get() == 1:
        label_number = tkinter.Label(frame_2, text='Selected "1"')
    elif number.get() == 2:
        label_number = tkinter.Label(frame_2, text='Selected "2"')
    else:
        raise Exception

    label_number.pack()

    boolean_1_value = boolean_1.get()
    boolean_2_value = boolean_2.get()

    label_boolean_1 = tkinter.Label(frame_2, text=f'Check button 1: {boolean_1_value}')
    label_boolean_2 = tkinter.Label(frame_2, text=f'Check button 2: {boolean_2_value}')

    label_boolean_1.pack()
    label_boolean_2.pack()


root = tkinter.Tk()
root.title('Radio button practice')
root.geometry('550x550')
root.resizable(False, False)

frame_1 = tkinter.LabelFrame(root, text='text frame')
frame_2 = tkinter.Frame(root)
frame_1.pack(padx=10, pady=10)
frame_2.pack(padx=10, pady=(0, 10))

# 整数の保持用のインスタンス
number = IntVar()
number.set(1)

radio_1 = tkinter.Radiobutton(frame_1, text='out put "1"', variable=number, value=1)
radio_2 = tkinter.Radiobutton(frame_1, text='out put "2"', variable=number, value=2)
radio_1.grid(row=0, column=0, padx=10, pady=10)
radio_2.grid(row=0, column=1, padx=10, pady=10)

boolean_1 = tkinter.BooleanVar()
boolean_2 = tkinter.BooleanVar()

checkbutton_1 = tkinter.Checkbutton(frame_1, text='check button 1', variable=boolean_1)
checkbutton_2 = tkinter.Checkbutton(frame_1, text='check button 2', variable=boolean_2)
checkbutton_1.grid(row=1, column=0)
checkbutton_2.grid(row=1, column=1)

button_1 = tkinter.Button(frame_1, text='out put', command=print_number)
button_1.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
