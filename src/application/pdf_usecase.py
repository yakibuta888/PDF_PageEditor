import fitz

from domain import select_pages, util


class Docs:
    def __init__(self, input_file_path: str, output_file_path: str = "") -> None:
        __path = util.File(input_file_path, output_file_path)
        self.__doc = fitz.Document(__path.input_file_path)
        self.__output_file_path = __path.output_file_path

    def select_even_pages(
        self,
        start_at: int = 1,
        from_the_end_to: int = 0,
        includes_out_of_first_range: bool = False,
        includes_out_of_last_range: bool = False
    ) -> None:
        self.__doc = select_pages.even(self.__doc, start_at, from_the_end_to, includes_out_of_first_range, includes_out_of_last_range)
        self.__doc.save(self.__output_file_path)
