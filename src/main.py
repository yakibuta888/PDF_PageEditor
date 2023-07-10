import os
import datetime

from pypdf import PdfMerger


now: str = datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours=9))
).strftime('%Y%m%d_%H%M%S')
file_name: str = input("file name is:") + ".pdf"
output_file_name: str = f'{file_name[:-4]}_edited{now}.pdf'
base_pdf: str = os.path.normpath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        f'../contents/{file_name}'
    )
)
output_pdf: str = os.path.normpath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        f'../contents/{output_file_name}'
    )
)

merger = PdfMerger()
merger.append(base_pdf)
number_of_pages = len(merger.pages)

print(number_of_pages)

for i in range(number_of_pages):
    if i == 0 or i == (number_of_pages - 1):
        continue

    reversed_index = number_of_pages - 1 - i
    if reversed_index % 2 != 0:
        continue
    target_index = reversed_index
    merger.pages.pop(target_index)

merger.write(output_pdf)
merger.close()
