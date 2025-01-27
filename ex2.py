#Count all letters, digits, and special symbols from a given string

word = 'P@#yn26at^&i5ve'
chars = 0
digits = 0
symbol = 0
for i in word:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        chars += 1
    else:
        symbol += 1
print(f"chars = {chars}")
print(f"digits = {digits}")
print(f"symbol = {symbol}")
