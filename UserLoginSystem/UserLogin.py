# Login System

correct_username = "admin"
correct_password = "1234"

attempts = 3

while attempts > 0:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print(f"Incorrect. Attempts remaining: {attempts}")

if attempts == 0:
    print("Account locked due to too many failed attempts.")
