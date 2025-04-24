# Program to calculate EMI for a loan
principal = float(input("Enter the loan amount : Rs\n"))
rate_of_interest = float(input("Enter the annual interest rate (in %):\n"))
loan_tenure = int(input("Enter loan tenure (in years):\n "))

# Convert annual interest rate to monthly rate
monthly_rate = rate_of_interest / 12 / 100

# Convert loan tenure in years to months
months = loan_tenure * 12

# EMI formula: EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)
emi = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

print(f"Your monthly EMI is: Rs{emi:.2f}")
