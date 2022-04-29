from main import Stack

with open('books_names.txt', 'r', encoding='utf8') as books:
    stack = Stack()
    for book in books:
        book = book.strip()
        print(book)
        stack.add(book)
    print()
    while not stack.is_empty():
        print(stack.get())


