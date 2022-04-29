from main import Deque

def check_square_brackets(string):
    bracket_stack = Deque()
    for i in string:
        if i == '[':
            bracket_stack.add_left(i)
        elif i == ']':
            if bracket_stack.is_empty():
                return False
            bracket_stack.get_left()
    return bracket_stack.is_empty()

print(check_square_brackets('[][]'))
print(check_square_brackets('[[][][]'))

