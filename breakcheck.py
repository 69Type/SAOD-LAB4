from main import Stack

def check_brackets(string):
    bracket_stack = Stack()
    for i in string:
        if i == '(':
            bracket_stack.add(i)
        elif i == ')':
            if bracket_stack.is_empty():
                return False
            bracket_stack.get()
    return bracket_stack.is_empty()

print(check_brackets('()'))
print(check_brackets('()('))
print(check_brackets('()())((('))
print(check_brackets('(()())()()()()'))
print(check_brackets('(()())()(((())))()()'))
print(check_brackets('(()())()(()()()'))
