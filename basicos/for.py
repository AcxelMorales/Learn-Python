for letter in "PYTHON":
    print(letter)
else:
    print("END LETTERS")

for i in range(10):
    print(i)
else:
    print("END NUMBERS")

for i in range(10):
    if i % 2 != 0:
        continue
    print(i)
