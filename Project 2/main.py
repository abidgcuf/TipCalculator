# print("Welcmoe to Bmi Calculator! ")

# waight = input("Please Input your waight in kg ")

# height = input("Please Input your height in m ")

# bmi = float(waight)/ float(height)** 2

# print(int(bmi))

print("Welcmoe to Tip Calculator! ")
bill = float(input("What was the total Bill? $ "))
tip = int(input("how much tip you would like to give? 10, 12 or 15? "))
peopel = int(input("how many people to split the bill? "))
tip_as_percent = tip /100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/peopel
final_amount = round(bill_per_person,2)
print(f"Each Person Should pay:${final_amount}")