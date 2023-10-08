import tkinter
from tkinter import END


root = tkinter.Tk()
root.title('greeting app')
root.geometry('400x400')
root.resizable(False, False)


def submit_name():
    if radio_value.get() == 'morning':
        greeting_text = 'Good morning!'
    elif radio_value.get() == 'noon':
        greeting_text = 'Good after noon!'
    elif radio_value.get() == 'night':
        greeting_text = 'Good night!'
    else:
        raise Exception

    greeting_label = tkinter.Label(output_frame, text=f'{greeting_text} Mr./Ms.{name.get()}.', bg=output_color)

    greeting_label.pack()

    name.delete(0, END)


output_color = '#A9A9A9'


input_frame = tkinter.Frame(root)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(fill='both', expand=True, padx=10, pady=(0, 10))

submit_img = tkinter.PhotoImage(file='src/sample/icons8-add-48.png')

name = tkinter.Entry(input_frame, width=30)
name.insert(0, 'Please enter a name.')
submit_button = tkinter.Button(input_frame, image=submit_img, command=submit_name)
name.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
submit_button.grid(row=0, column=3, padx=10, pady=10)

radio_value = tkinter.StringVar()
radio_value.set('morning')

morning_button = tkinter.Radiobutton(input_frame, text='morning', variable=radio_value, value='morning')
noon_button = tkinter.Radiobutton(input_frame, text='noon', variable=radio_value, value='noon')
night_button = tkinter.Radiobutton(input_frame, text='night', variable=radio_value, value='night')
morning_button.grid(row=1, column=0)
noon_button.grid(row=1, column=1)
night_button.grid(row=1, column=2)


root.mainloop()
