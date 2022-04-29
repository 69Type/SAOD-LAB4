
from main import Stack

A = Stack()
B = Stack()
C = Stack()

disks = 8

for i in range(disks, 0, -1):
    A.add(i)

def move(a, b):
    if len(a.array) == 0 and len(b.array) > 0:
        a.add(b.get())
    elif len(a.array) > 0 and len(b.array) == 0:
        b.add(a.get())
    elif a.look() > b.look():
        a.add(b.get())
    else:
        b.add(a.get())

if disks % 2 == 0:
    while len(C.array) != disks:
        move(A, B)
        move(A, C)
        move(B, C)
else:
    while len(C.array) != disks:
        move(A, C)
        move(A, B)
        move(B, C)

while not C.is_empty():
    print(C.get())