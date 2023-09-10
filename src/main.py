import os
import datetime

from pypdf import PdfMerger, PdfReader, PdfWriter


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

reader = PdfReader(base_pdf)
bookmarks = reader.outline

new_bookmarks: list[dict[str, str | int]] = list()
for bookmark in bookmarks:
    detail: dict[str, str | object] = {key: bookmark[key] for key in bookmark.keys()}  # type: ignore
    if not isinstance(detail['/Title'], str):
        continue
    title: str = detail['/Title']
    page_number: int = detail['/Page']['/StructParents'] + 2  # type: ignore
    new_bookmark: dict[str, str | int] = {'title': title, 'page_number': page_number}
    new_bookmarks.append(new_bookmark)

merger._trim_outline(reader, bookmarks, list(range(number_of_pages)))

for a_bookmark in new_bookmarks:
    new_page_number: int = int(a_bookmark['page_number']) // 2
    a_bookmark.update({'page_number': new_page_number})
    merger.add_outline_item(title=a_bookmark['title'], page_number=a_bookmark['page_number'])
    print(a_bookmark)


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
