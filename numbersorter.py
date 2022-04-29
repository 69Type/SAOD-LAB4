from main import Deque
from random import randrange

numbers = [randrange(-50, 50) for i in range(10)]
q = Deque()

for number in numbers:
    getattr(q, 'add_left' if number < 0 else 'add_right')(number)

print(numbers)

new_number = q.look_left()
while new_number < 0:
    new_number = q.get_left()
    q.add_right(new_number)
else:
    q.add_left(q.get_right())

while not q.is_empty():
    if q.look_rigth() < 0:
        print(q.get_right())
    else:
        print(q.get_left())


