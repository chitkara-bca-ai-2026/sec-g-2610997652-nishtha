username= input("Enter your username: ")
pwd=input("Enter your password: ")

print("PASSWORD VALIDATION REPORT")

print("Username:", username)
print("Password:", "*" * len(pwd))

if len(pwd) >= 8:
    print("[PASS] Minimum 8 characters")
else:
    print("[FAIL] Minimum 8 characters")


for ch in pwd:
    if ch.isupper():
        containsupper=True
    elif ch.islower():
        containslower=True
    elif ch.isdigit():
        containsdigit=True

if containsupper and containslower and containsdigit:
    print("Valid")
else:
    print("Invalid")


if (len(pwd) >= 8
    and any(char.isdigit() for char in pwd)
    and any(char.isupper() for char in pwd)):

    print("\nPassword is VALID!")
    print("Account created successfully for", username + "!")
else:
    print("\nPassword is INVALID.")