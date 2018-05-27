from random import randint,choice

words = ["champion", "meticulous", "hexagon"]
word = words[randint(0,len(words)-1)]
chars = list(word)

new_chars = []
for i in range(len(chars)):
    n = choice(chars)
    new_chars.append(n)
    m = chars.index(n)
    chars.remove(chars[m])
print(new_chars)

loop = True
while loop:
    ans = input("Your answer: ")
    if ans != word:
        print(":(")
    else:
        print("Hura")
        loop = False