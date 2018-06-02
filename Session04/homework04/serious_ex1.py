name = input("Your full name: ").lower()

while ("  " in name):
    name = name.replace("  ", " ")

name1 = " ".join(name.split())
name2 = []
for item in name1:
    name2.append(item)
# print("name2", name2)
for i in range (len(name2)):
    if name2[i] == " ":
        name2[i+1]= name2[i+1].upper()
name2[0]=name2[0].upper()
print ("".join(name2))
