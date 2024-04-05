print("Welcome to the tip calculator!")

bill = input("What was the total bill? $")

decide_tip = input("How much tip would you like to give? 10, 12, or 15?\n")
tip_amount = int(bill) * (int(decide_tip) / 100)  #to calculate percentage you multiply percentage divided by 100
round_tip = round(tip_amount, 2)
price_with_tip = int(bill) + round_tip

people = input("How many people to split the bill?\n")
price_per_person = price_with_tip / int(people)
final_price = "{:.2f}".format(price_per_person) # A method of rounding to 2 decimal places AND allowing the .6 to become .60
print(f"Each person should pay: ${final_price}")
