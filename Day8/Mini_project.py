# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left,
# if we live until 90 years old.

'''Solution
|
|
|
|
|
|
|
|

'''

def life_in_weeks(age):
    years = 90 - age
    weeks = years * 52
    print(f"You have {weeks} weeks left.")

life_in_weeks(25)