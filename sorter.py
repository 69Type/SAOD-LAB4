from main import Stack

text = 'Если вы находитесь в универе после 20.00, с вами должен находиться преподаватель и об этом должна знать охрана!!!'

letters = Stack()
digits = Stack()
others = Stack()

for c in text:
    if c.isalpha():
        letters.add(c)
    elif c.isdigit():
        digits.add(c)
    else:
        others.add(c)


digits_text = ''
while not digits.is_empty():
    digits_text += digits.get()

letters_text = ''
while not letters.is_empty():
    letters_text += letters.get()

others_text = ''
while not others.is_empty():
    others_text += others.get()

text = digits_text[::-1] + letters_text[::-1] + others_text[::-1]
print(text)