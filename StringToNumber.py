import inflect

# Create inflect engine
p = inflect.engine()

# Ask user for a number
number = input("Enter a number (e.g., 300000000): ")

# Check if it's a valid number
if number.isdigit():
    # Convert number to words
    words = p.number_to_words(int(number))
    print(f"In words: {words}")
else:
    print("Please enter a valid number.")
