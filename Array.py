login = [
    ["Thomas", "Passssword"],
    ["Leo", "Bread"],
    ["Evan", "1234"],
]

username = input("Username: ")
password = input("Password: ")

for user in login:
    if username == user[0] and password == user[1]:
        print("Login successful!")
        break
else:
    print("Incorrect username or password")