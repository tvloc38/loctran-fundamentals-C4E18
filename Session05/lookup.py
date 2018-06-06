teencode = {
    "hc": "hoc" ,
    "ngta": "nguoi ta" ,
    "any": "anh nguoi yeu",
    "lm": "lam",
    "ng": "nguoi",
    "stt": "status",
    "eny": "em nguoi yeu",
    "ns": "noi",
    "r": "roi",
    "pt": "phat trien",
}
while True:
    for k in teencode:
        print(k, end="\t")
    print()
    ans = input("Your code: ")
    if ans in teencode:
        print(teencode[ans])
    else:
        ans2 = input("Not found, do you want to contribute this word? (Y/N)? ").upper()
        if ans2 == "Y":
            update_teencode = input("Enter your translation: ")
            teencode[ans] = update_teencode
            print("updated")
        elif ans2 == "N":
            print("ok")
            break
