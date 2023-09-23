import fitz


def even(
    doc: fitz.Document,
    start_at: int,
    from_the_end_to: int,
    includes_out_of_first_range: bool,
    includes_out_of_last_range: bool
) -> fitz.Document:
    if isinstance(doc.page_count, int):
        number_of_pages: int = doc.page_count
    else:
        raise TypeError("Failed to retrieve page count.")

    r_start: int = start_at - 1
    r_end: int = number_of_pages - from_the_end_to
    even_pages: list[int] = [p for p in range(r_start, r_end) if p % 2 != 0]

    if includes_out_of_first_range:
        if r_start == 0:
            even_pages.insert(0, 0)
        else:
            before_pages: list[int] = [p for p in range(r_start)]
            even_pages[0:0] = before_pages

    if includes_out_of_last_range:
        if from_the_end_to == 0:
            pass
        else:
            after_pages: list[int] = [p for p in range(r_end, number_of_pages)]
            even_pages.extend(after_pages)

    doc.select(even_pages)
    return doc


TODO: "odd関数の追加"  # type:ignore
