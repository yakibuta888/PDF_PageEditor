import tkinter


root = tkinter.Tk()
root.title('greeting app')
root.geometry('400x400')
root.resizable(False, False)


output_color = '#A9A9A9'


input_frame = tkinter.Frame(root)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(fill='both', expand=True)

submit_img = tkinter.PhotoImage(file='src/sample/icons8-add-48.png')

name = tkinter.Entry(input_frame, width=30)
name.insert(0, 'Please enter a name.')
submit_button = tkinter.Button(input_frame, image=submit_img)
name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
