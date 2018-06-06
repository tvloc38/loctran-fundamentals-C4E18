string = input("Moi nhap string: ").lower()
letter_counts = {}
for letter in string:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

print(letter_counts)

letter_items = list(letter_counts.items())
letter_items.sort()

for k,v in letter_items:
    print('{0}  {1}'.format(k,v))