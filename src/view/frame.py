import tkinter as tk
import tkinter.filedialog
import threading

from presentation.pdf_controller import PdfController


LINK_FONT = ('Times New Roman', 12)
TITLE_FONT = ('Arial', 12)
NORMAL_FONT = ('Arial', 10)
BOLD_FONT = ('Arial', 10, 'bold')
DISCRIPTION_FONT = ('Arial', 9)
DISCRIPTION_COLOR = '#696969'


class Frame:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root

    def change_state(
        self,
        bool_check: tk.BooleanVar,
        elements: list[tk.Label | tk.Entry | tk.Button | tk.Checkbutton]
    ):
        if bool_check.get():
            for element in elements:
                element.config(state='normal')
        else:
            for element in elements:
                element.config(state='disabled')


class FileFrame(Frame):
    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root)
        self.file_frame = tk.Frame(self.root)
        self.file_frame.grid(row=0, padx=40)

        self.file_button_img = tk.PhotoImage(file='src/view/file_explorer.png', width=30, height=30)

        self.title_input = tk.Label(self.file_frame, text='編集元ファイル', font=TITLE_FONT)
        self.filepath_input = tk.Entry(self.file_frame, width=40, font=LINK_FONT)
        self.button_select_input_file = tk.Button(
            self.file_frame,
            image=self.file_button_img,
            command=self.select_input_file
        )
        self.title_input.grid(row=0, column=0, padx=2, pady=2, sticky='w')
        self.filepath_input.grid(row=1, column=0, pady=(0, 10))
        self.button_select_input_file.grid(row=1, column=1, padx=2, pady=(0, 10))

        self.boolean_output_file = tk.BooleanVar()

        self.checkbutton_output_file = tk.Checkbutton(
            self.file_frame,
            text='出力先ファイル名を指定する',
            font=NORMAL_FONT,
            variable=self.boolean_output_file,
            command=lambda: self.change_state(
                self.boolean_output_file,
                [self.filepath_output, self.button_select_output_file]
            )
        )
        self.discription_output_file = tk.Label(
            self.file_frame,
            text='指定しない場合は元ファイルの場所に編集時間を加えたファイル名で作成します',
            font=DISCRIPTION_FONT,
            fg=DISCRIPTION_COLOR
        )
        self.filepath_output = tk.Entry(self.file_frame, width=40, font=LINK_FONT, state='disabled')
        self.button_select_output_file = tk.Button(
            self.file_frame,
            image=self.file_button_img,
            state='disabled',
            command=self.select_output_file
        )
        self.checkbutton_output_file.grid(row=2, column=0, pady=(0, 2), sticky='w')
        self.discription_output_file.grid(row=3, column=0, padx=10, pady=(0, 5), sticky='w')
        self.filepath_output.grid(row=4, column=0, pady=(0, 10))
        self.button_select_output_file.grid(row=4, column=1, padx=2, pady=(0, 10))

    def select_input_file(self):
        file_type = [('PDF', '.pdf')]
        file_name = tkinter.filedialog.askopenfilename(filetypes=file_type, initialdir='./')
        self.filepath_input.insert(0, file_name)

    def select_output_file(self):
        file_type = [('PDF', '.pdf')]
        file_name = tkinter.filedialog.asksaveasfilename(filetypes=file_type, initialdir='./')
        self.filepath_output.insert(0, file_name)


class FunctionFrame(Frame):
    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root)
        self.function_frame = tkinter.Frame(root)
        self.function_frame.grid(row=1, padx=40, sticky='w')

        self.extract_mode = tkinter.StringVar()
        self.extract_mode.set('even')

        self.title_page_extract = tkinter.Label(self.function_frame, text='ページの抽出', font=TITLE_FONT)
        self.radio_even = tkinter.Radiobutton(
            self.function_frame,
            text='偶数ページを抽出する',
            font=NORMAL_FONT,
            variable=self.extract_mode,
            value='even'
        )
        self.radio_odd = tkinter.Radiobutton(
            self.function_frame,
            text='奇数ページを抽出する',
            font=NORMAL_FONT,
            variable=self.extract_mode,
            value='odd'
        )
        self.title_page_extract.grid(row=0, column=0, sticky='w')
        self.radio_even.grid(row=1, column=0, padx=10, pady=10)
        self.radio_odd.grid(row=1, column=1, padx=10, pady=10)


class OptionFrame(Frame):
    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root)
        option_frame = tkinter.Frame(root)
        option_frame.grid(row=2, padx=40, sticky='w')

        self.boolean_start_page = tkinter.BooleanVar()
        self.boolean_leave_start_page = tkinter.BooleanVar()
        self.boolean_end_page = tkinter.BooleanVar()
        self.boolean_leave_end_page = tkinter.BooleanVar()

        title_option = tkinter.Label(option_frame, text='オプション', font=TITLE_FONT)
        checkbutton_start_page = tkinter.Checkbutton(
            option_frame,
            text='開始ページを指定する',
            font=NORMAL_FONT,
            variable=self.boolean_start_page,
            command=lambda: self.change_state(
                self.boolean_start_page,
                [self.entry_start_page, label_start_page, checkbutton_leave_start_page]
            )
        )
        self.entry_start_page = tkinter.Entry(option_frame, width=5, state='disabled')
        label_start_page = tkinter.Label(
            option_frame,
            text='ページ目から開始',
            font=NORMAL_FONT,
            state='disabled'
        )
        checkbutton_leave_start_page = tkinter.Checkbutton(
            option_frame,
            text='開始ページより前を残す',
            font=NORMAL_FONT,
            variable=self.boolean_leave_start_page,
            state='disabled'
        )
        checkbutton_end_page = tkinter.Checkbutton(
            option_frame,
            text='終了ページを指定する',
            font=NORMAL_FONT,
            variable=self.boolean_end_page,
            command=lambda: self.change_state(
                self.boolean_end_page,
                [self.entry_end_page, label_end_page, checkbutton_leave_end_page]
            )
        )
        self.entry_end_page = tkinter.Entry(option_frame, width=5, state='disabled')
        label_end_page = tkinter.Label(
            option_frame,
            text='ページ前で終了',
            font=NORMAL_FONT,
            state='disabled'
        )
        checkbutton_leave_end_page = tkinter.Checkbutton(
            option_frame,
            text='終了ページより後を残す',
            font=NORMAL_FONT,
            variable=self.boolean_leave_end_page,
            state='disabled'
        )

        title_option.grid(row=0, column=0, sticky='w')
        checkbutton_start_page.grid(row=1, column=0, columnspan=2, padx=10, pady=(10, 2), sticky='w')
        self.entry_start_page.grid(row=2, column=0, padx=(30, 0), pady=(0, 5))
        label_start_page.grid(row=2, column=1, pady=(0, 5), sticky='w')
        checkbutton_leave_start_page.grid(row=3, column=0, columnspan=2, padx=(30, 0), pady=(0, 5), sticky='w')
        checkbutton_end_page.grid(row=4, column=0, columnspan=2, padx=10, pady=(10, 2), sticky='w')
        self.entry_end_page.grid(row=5, column=0, padx=(30, 0), pady=(0, 5))
        label_end_page.grid(row=5, column=1, pady=(0, 5), sticky='w')
        checkbutton_leave_end_page.grid(row=6, column=0, columnspan=2, padx=(30, 0), pady=(0, 5), sticky='w')


class InfoFrame(Frame):
    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root)
        info_frame = tkinter.LabelFrame(root, text='system infomation', borderwidth=5)
        info_frame.grid(row=4, padx=40, pady=10, sticky='we')

        self.message = tk.StringVar()
        self.message.set('')

        self.label_info = tkinter.Label(info_frame, textvariable=self.message, height=2)
        self.label_info.pack()


class ButtonFrame(Frame):
    def __init__(
        self,
        root: tk.Tk,
        pdf_controller: PdfController,
        file_frame: FileFrame,
        function_frame: FunctionFrame,
        option_frame: OptionFrame,
        info_frame: InfoFrame
    ) -> None:
        super().__init__(root)
        button_frame = tkinter.Frame(root)
        button_frame.grid(row=3)

        self.pdf_controller = pdf_controller

        self.button_create = tkinter.Button(
            button_frame,
            text='作成',
            font=BOLD_FONT,
            command=lambda: self.create_callback(
                file_frame,
                function_frame,
                option_frame,
                info_frame
            )
        )
        self.button_create.grid(row=0, column=0, ipadx=50)

    def create_callback(
        self,
        file_frame: FileFrame,
        function_frame: FunctionFrame,
        option_frame: OptionFrame,
        info_frame: InfoFrame
    ) -> None:
        th = threading.Thread(target=self.create, args=(
            file_frame,
            function_frame,
            option_frame,
            info_frame
        ))
        th.start()

    def create(
        self,
        file_frame: FileFrame,
        function_frame: FunctionFrame,
        option_frame: OptionFrame,
        info_frame: InfoFrame
    ) -> None:
        self.button_create.config(state='disabled')
        info_frame.message.set('Processing.')

        input_file_path = file_frame.filepath_input.get()

        if file_frame.boolean_output_file.get():
            output_file_path = file_frame.filepath_output.get()
        else:
            output_file_path = ""

        mode = function_frame.extract_mode.get()

        if option_frame.boolean_start_page.get():
            start_at = int(option_frame.entry_start_page.get())
        else:
            start_at = int(1)

        if option_frame.boolean_end_page.get():
            from_the_end_to = int(option_frame.entry_end_page.get())
        else:
            from_the_end_to = int(0)

        includes_out_of_first_range = option_frame.boolean_leave_start_page.get()
        includes_out_of_last_range = option_frame.boolean_leave_end_page.get()

        message = self.pdf_controller.select_pages(
            input_file_path=input_file_path,
            output_file_path=output_file_path,
            mode=mode,
            start_at=start_at,
            from_the_end_to=from_the_end_to,
            includes_out_of_first_range=includes_out_of_first_range,
            includes_out_of_last_range=includes_out_of_last_range
        )

        info_frame.message.set(message)
        self.button_create.config(state='normal')
