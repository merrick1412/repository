def main():
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password must be at least 8 characters long")
        return
    hasLower = False
    for letter in password:
        if letter.islower():
            hasLower = True
    if not hasLower:
        print("Password must contain at least one lowercase letter")
        return
    hasUpper = False
    for letter in password:
        if letter.isupper():
            hasUpper = True
    if not hasUpper:
        print("Password must contain at least one uppercase letter")
        return
    hasDigit = False
    for letter in password:
        if letter.isdigit():
            hasDigit = True
    if not hasDigit:
        print("Password must contain at least one digit")
        return
    special = "@#$%^&*!"
    hasSpecial = False
    if any(letter in special for letter in password):
        hasSpecial = True
    hasSpace = False
    for letter in password:
        if letter == " ":
            hasSpace = True
    if hasSpace:
        print("Password must contain no spaces")
        return
    print("Password is valid")







if __name__ == '__main__':
    main()