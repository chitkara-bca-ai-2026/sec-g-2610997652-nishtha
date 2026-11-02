pwd=input("Enter password:")

spaces=0
spc=0
const=0
digits=0
vowels=0

for ch in pwd:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels+=1
        else:
            const+=1
    elif ch.isspace():
        spaces+=1
    elif ch.isdigit():
        digits+=1
    else:
        spc+=1

if vowels and spaces and spc and const and digits:
    print("Valid")
else:
    print("Invalid")

