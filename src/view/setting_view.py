import tkinter as tk

from view import frame
from presentation.pdf_controller import PdfController


class SettingView:
    def __init__(self) -> None:
        root = tk.Tk()
        root.title('PDF page editor settings')
        icon = tk.PhotoImage(file='src/view/pdf_generate_icon.png')
        root.iconphoto(False, icon)
        root.geometry('550x520')
        root.resizable(False, False)

        self.pdf_controller = PdfController()

        file_frame = frame.FileFrame(root)
        function_frame = frame.FunctionFrame(root)
        option_frame = frame.OptionFrame(root)
        info_frame = frame.InfoFrame(root)
        frame.ButtonFrame(
            root,
            self.pdf_controller,
            file_frame,
            function_frame,
            option_frame,
            info_frame
        )

        root.mainloop()
