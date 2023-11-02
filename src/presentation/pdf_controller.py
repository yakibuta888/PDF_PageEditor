from application import pdf_usecase

# def pdf_router() -> None:
#     file_path: str = input("file path is:")

#     pdf = pdf_usecase.Docs(file_path)
#     pdf.select_even_pages(from_the_end_to=1, includes_out_of_last_range=True)


class PdfController:
    def __init__(self) -> None:
        pass

    def select_pages(
        self,
        input_file_path: str,
        output_file_path: str,
        mode: str,
        start_at: int,
        from_the_end_to: int,
        includes_out_of_first_range: bool,
        includes_out_of_last_range: bool
    ) -> str:
        pdf = pdf_usecase.Docs()
        message = pdf.select_pages(
            input_file_path,
            output_file_path,
            mode,
            start_at,
            from_the_end_to,
            includes_out_of_first_range,
            includes_out_of_last_range
        )
        return message
