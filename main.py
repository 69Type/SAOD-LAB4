
# стек
class Stack:
    def __init__(self, array=None):
        self.array = [] if not array else array

    def is_empty(self):
        return len(self.array) == 0

    def add(self, value):
        self.array.append(value)

    def get(self):
        return self.array.pop()

    def look(self):
        return self.array[-1]


# дек
class Deque:
    def __init__(self, array=None):
        self.array = [] if not array else array

    def is_empty(self):
        return len(self.array) == 0

    def get_left(self):
        return self.array.pop(0)

    def get_right(self):
        return self.array.pop()

    def add_left(self, value):
        self.array.insert(0, value)

    def add_right(self, value):
        self.array.append(value)

    def look_left(self):
        return self.array[0]

    def look_rigth(self):
        return self.array[-1]


