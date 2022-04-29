from main import Deque
from random import shuffle

d = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
shuffle(d)
d = ''.join(d)

keys = Deque()
for letter in d:
    keys.add_left(letter)



def encode(c):
    for i in range(len(keys.array)):
        x = keys.get_left()
        if x == c:
            keys.add_right(x)
            val = keys.get_left()
            keys.add_left(val)
            return val
        keys.add_right(x)


def decode(c):
    for i in range(len(keys.array)):
        x = keys.get_right()
        if x == c:
            keys.add_left(x)
            val = keys.get_right()
            keys.add_left(val)
            return val
        keys.add_left(x)

text = 'эти слова никто не прочитает'

encoded = ''
for letter in text:
    encoded_letter = encode(letter)
    if encoded_letter:
        encoded += encoded_letter
    else:
        encoded += letter

decoded = ''
for letter in encoded:
    decoded_letter = decode(letter)
    if decoded_letter:
        decoded += decoded_letter
    else:
        decoded += letter


print(encoded)
print(decoded)