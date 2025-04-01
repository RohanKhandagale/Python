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


# New modify file with GST
bill = float(input("what is the bill Amount:- \n"))
tip = int(input("How much tip you would like to give Rs:- \n"))
person = int(input("How much person spilt the bill:- \n"))
Gst = float(input("How much Percent Gst:-]\n"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
final_bill = bill + total_tip_amount
Gst_as_per = Gst / 100
Gst_amount = bill * Gst_as_per
Gst_final_amount = bill + Gst_amount + total_tip_amount
bill_per_person = round(Gst_final_amount /person ,2)
if person == 1:
    print (f"You Bill is:-{Gst_final_amount}")
else:
    print (f"Your final bill Amount is:-{Gst_final_amount}")
    print(f"You have to pay by per person :-{bill_per_person}")
