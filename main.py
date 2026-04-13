def get_books(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
    parse_line = lambda line: (
        lambda parts: [parts[0], parts[1], parts[2], int(parts[3]), float(parts[4])]
    )(line.strip().split("|"))
    is_data_row = lambda line: (
        line.strip() != "" and not line.startswith("isbn")
    )

    return list(map(parse_line, filter(is_data_row, lines)))

def filtered_books(books, keyword):
    has_keyword = lambda book: keyword.lower() in book[1].lower()
    transform = lambda book: [
        book[0],
        f"{book[1]}, {book[2]}",
        book[3],
        book[4]
    ]

    return list(map(transform, filter(has_keyword, books)))

def total_price(books):
    to_tuple = lambda book: (book[0], round(book[2] * book[3], 2))
    return list(map(to_tuple, books))

if __name__ == "__main__":
    # task 1
    books = get_books("books.csv")
    print("task 1: get_books")
    list(map(print, books))

    # task 2
    python_books = filtered_books(books, "python")
    print("\n task 2: filtered_books(books, 'python')")
    list(map(print, python_books))

    # task 3
    prices = total_price(python_books)
    print("\n task 3: total_price")
    list(map(print, prices))
