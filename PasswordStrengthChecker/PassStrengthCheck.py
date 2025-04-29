import string


def check_password_strength():
    password = input("Enter your password: ")

    # Check password length
    if len(password) < 8:
        print("Password is too short. It should be at least 8 characters.")
        return

    # Flags for character types
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    # Special characters
    special_characters = string.punctuation

    # Check each character in the password
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    # Final password strength check
    if has_lower and has_upper and has_digit and has_special:
        print("Your password is strong.")
    else:
        print("Your password is weak. It should include:")
        if not has_lower:
            print("- At least one lowercase letter.")
        if not has_upper:
            print("- At least one uppercase letter.")
        if not has_digit:
            print("- At least one digit.")
        if not has_special:
            print("- At least one special character (e.g., !@#$%^&*).")


# Run the password strength checker
check_password_strength()
