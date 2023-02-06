print("Welcome to the TIP-calculator.")
print()
bill = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))

tip = bill * percentage / 100
total_bill = tip + bill
total_bill_for_person = total_bill / people

print(f"Each person should pay: {total_bill_for_person:.2f}")




