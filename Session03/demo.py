from random import choice # chon ngau nhien 1 phan tu trong 1 list

word = "champion"

chars = list(word)

new_chars = []
for i in range(len(chars)):
    n = choice(chars)
    new_chars.append(n)
    m = chars.index(n)
    chars.remove(chars[m])
print(new_chars)

ans = input("Your answer: ")
if ans == word:
    print("Hura")
else:
    print(":(")