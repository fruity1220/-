
word = input()

alphabet = list(range(97, 122))

for i in alphabet:
    print(word.find(chr(i)))

