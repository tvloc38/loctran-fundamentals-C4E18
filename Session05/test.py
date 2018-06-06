person = ["Quy", 20, 0, "Vinh Phuc", 2, ["Manga", "Coding"], 3, 20]

#dictionary
person = {
    # key : value,
    "name": "Quy",
    "age": 20,
    "ex": 0,
    "favs": ["Manga", "Coding"]
}

# print(person)

# name = person["name"]
# print(name)

#create
person["length"] = 20
print(person)

#update
person["length"] = 10
print(person)

#delete
# del person["length"]

# key = "age"
# if key in person:
#     print(person[key])
# else:
#     print("Not found")

# for key
# for k in person:
#     print(k, person[k])

# for value
# for v in person.values():
#     print(v)

# for key,value
# for k,v in person.items():
#     print(k, v)