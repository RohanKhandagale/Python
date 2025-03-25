print("Welcome to the tip Calculator!!")
bill =float(input("What was the total bill?:-\n"))
# print(bill)
tip =int(input("How much tip would you like to give:- 10,12,15,20?\n"))
# print(tip)
peolpe =int(input("How many people split the bill:-\n"))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / peolpe
final_bill = round(bill_per_person , 2)
print(f"Each person should pay:-{final_bill}")
