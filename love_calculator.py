# Define the function to calculate love score
def calculate_love_score(name1, name2):
    # Concatenate both names into a single string and convert to lowercase
    combined_names = (name1 + name2).lower()

    # Define the letters for TRUE and LOVE
    true_letters = 'true'
    love_letters = 'love'

    # Function to count occurrences of letters from a set of characters
    def count_letters(letters):
        count = 0
        for letter in letters:
            count += combined_names.count(letter)
        return count

    # Count the occurrences of TRUE and LOVE letters
    true_score = count_letters(true_letters)
    love_score = count_letters(love_letters)

    # Combine the scores to form a two-digit number
    love_score_combined = int(str(true_score) + str(love_score))

    # Print the love score
    print(love_score_combined)


# Call the function with hard-coded values
calculate_love_score("Kanye West", "Kim Kardashian")