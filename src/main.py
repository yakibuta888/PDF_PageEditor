from application import pdf_usecase


file_path: str = input("file path is:")

pdf = pdf_usecase.Docs(file_path)
pdf.select_even_pages(from_the_end_to=1, includes_out_of_last_range=True)
