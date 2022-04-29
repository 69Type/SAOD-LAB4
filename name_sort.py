from main import Deque

with open('books_names.txt','r', encoding="utf8") as books:
    q1 = Deque()
    q2 = Deque()
    for book in books:
        if q1.is_empty():
            q1.add_left(book)
        else:
            on = q1.look_left()
            while on < book:
                on = q1.get_left()
                q2.add_left(on)
                if not q1.is_empty():
                    on = q1.look_left()
                else:
                    break
            q1.add_left(book)
            while not q2.is_empty():
                q1.add_left(q2.get_left())
    while not q1.is_empty():
        print(q1.get_left())
