import tkinter
from tkinter import END
from decimal import Decimal

root = tkinter.Tk()
root.title('calculator')
icon = tkinter.PhotoImage(file='src/sample/calc_113237.png')
root.iconphoto(False, icon)
root.geometry('325x415')
root.resizable(False, False)

operation: str = ''
first_number: str = ''


def clear_number():
    screen.delete(0, END)

    unlock_button()


def negate():
    calculated_number = str(-1 * float(screen.get()))
    screen.delete(0, END)
    screen.insert(0, calculated_number)


def percentage():
    calculated_number = str(0.01 * float(screen.get()))
    screen.delete(0, END)
    screen.insert(0, calculated_number)


def add_element(number: str):
    screen.insert(END, number)

    if '.' in screen.get():
        decimal_button.config(state='disabled')


def unlock_button():
    global operation, first_number

    decimal_button.config(state='normal')
    add_button.config(state='normal')
    substract_button.config(state='normal')
    multiply_button.config(state='normal')
    divide_button.config(state='normal')

    operation = ''
    first_number = ''


def operate(operator: str) -> None:
    global operation, first_number
    operation = operator
    first_number = screen.get()

    screen.delete(0, END)

    add_button.config(state='disabled')
    substract_button.config(state='disabled')
    multiply_button.config(state='disabled')
    divide_button.config(state='disabled')

    decimal_button.config(state='normal')


def calculate():
    if operation == 'add':
        calculated_number = str(Decimal(first_number) + Decimal(screen.get()))
    elif operation == 'substract':
        calculated_number = str(Decimal(first_number) - Decimal(screen.get()))
    elif operation == 'multiply':
        calculated_number = str(Decimal(first_number) * Decimal(screen.get()))
    elif operation == 'divide':
        if screen.get() == '0':
            calculated_number = 'ERROR'
        else:
            calculated_number = str(Decimal(first_number) / Decimal(screen.get()))
    else:
        calculated_number = screen.get()

    screen.delete(0, END)
    screen.insert(0, calculated_number)

    unlock_button()


screen_font = ('Segoe UI', 30, 'bold')
button_font = ('Segoe UI', 20, 'bold')
light_orange = '#FFEFD5'
button_color_1 = '#DCDCDC'
button_color_2 = '#27D8C7'
button_color_3 = '#FFBBA3'
fg_color = 'white'

screen_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
screen_frame.pack(padx=2, pady=(5, 0))
button_frame.pack(padx=2)

screen = tkinter.Entry(screen_frame, width=40, font=screen_font, bg=light_orange, justify='right', borderwidth=5)
screen.pack()

clear_button = tkinter.Button(button_frame, text='C', font=button_font, bg=button_color_1, command=clear_number)
negate_button = tkinter.Button(button_frame, text='+/-', font=button_font, bg=button_color_1, command=negate)
percentage_button = tkinter.Button(button_frame, text='%', font=button_font, bg=button_color_1, command=percentage)
divide_button = tkinter.Button(button_frame, text='/', font=button_font, bg=button_color_2, fg=fg_color, command=lambda: operate('divide'))
seven_button = tkinter.Button(button_frame, text='7', font=button_font, bg=button_color_3, fg=fg_color, command=lambda: add_element('7'))
eight_button = tkinter.Button(button_frame, text='8', font=button_font, bg=button_color_3, fg=fg_color, command=lambda: add_element('8'))
nine_button = tkinter.Button(button_frame, text='9', font=button_font, bg=button_color_3, fg=fg_color, command=lambda: add_element('9'))
multiply_button = tkinter.Button(button_frame, text='*', font=button_font, bg=button_color_2, fg=fg_color, command=lambda: operate('multiply'))
four_button = tkinter.Button(button_frame, text='4', font=button_font, bg=button_color_3, fg=fg_color, command=lambda: add_element('4'))
five_button = tkinter.Button(button_frame, text='5', font=button_font, bg=button_color_3, fg=fg_color, command=lambda: add_element('5'))
six_button = tkinter.Button(button_frame, text='6', font=button_font, bg=button_color_3, fg=fg_color, command=lambda: add_element('6'))
substract_button = tkinter.Button(button_frame, text='-', font=button_font, bg=button_color_2, fg=fg_color, command=lambda: operate('substract'))
one_button = tkinter.Button(button_frame, text='1', font=button_font, bg=button_color_3, fg=fg_color, command=lambda: add_element('1'))
two_button = tkinter.Button(button_frame, text='2', font=button_font, bg=button_color_3, fg=fg_color, command=lambda: add_element('2'))
three_button = tkinter.Button(button_frame, text='3', font=button_font, bg=button_color_3, fg=fg_color, command=lambda: add_element('3'))
add_button = tkinter.Button(button_frame, text='+', font=button_font, bg=button_color_2, fg=fg_color, command=lambda: operate('add'))
zero_button = tkinter.Button(button_frame, text='0', font=button_font, bg=button_color_3, fg=fg_color, command=lambda: add_element('0'))
decimal_button = tkinter.Button(button_frame, text='.', font=button_font, bg=button_color_3, fg=fg_color, command=lambda: add_element('.'))
equal_button = tkinter.Button(button_frame, text='=', font=button_font, bg=button_color_2, fg=fg_color, command=calculate)

clear_button.grid(row=0, column=0, sticky='WE', ipady=10)
negate_button.grid(row=0, column=1, sticky='WE', ipady=10)
percentage_button.grid(row=0, column=2, sticky='WE', ipady=10)
divide_button.grid(row=0, column=3, sticky='WE', ipady=10)

seven_button.grid(row=1, column=0, sticky='WE', ipadx=16, ipady=10)
eight_button.grid(row=1, column=1, sticky='WE', ipadx=16, ipady=10)
nine_button.grid(row=1, column=2, sticky='WE', ipadx=16, ipady=10)
multiply_button.grid(row=1, column=3, sticky='WE', ipadx=16, ipady=10)

four_button.grid(row=2, column=0, sticky='WE', ipady=10)
five_button.grid(row=2, column=1, sticky='WE', ipady=10)
six_button.grid(row=2, column=2, sticky='WE', ipady=10)
substract_button.grid(row=2, column=3, sticky='WE', ipady=10)

one_button.grid(row=3, column=0, sticky='WE', ipady=10)
two_button.grid(row=3, column=1, sticky='WE', ipady=10)
three_button.grid(row=3, column=2, sticky='WE', ipady=10)
add_button.grid(row=3, column=3, sticky='WE', ipady=10)

zero_button.grid(row=4, column=0, sticky='WE', ipady=10, columnspan=2)
decimal_button.grid(row=4, column=2, sticky='WE', ipady=10)
equal_button.grid(row=4, column=3, sticky='WE', ipady=10)

root.mainloop()
