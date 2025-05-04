## Let's buils  TIP Calculator.
print("Welcome to the tip calculator.")
## Let's take the total bill amount from user
total_bill= float(input("What was the total bill? $"))
## Let's take the percentage of tip from user
tip_percentage= int(input("What percentage tip would you like to give? 10, 12, or 15? "))
## Let's take the no of people to split the bill from user
no_of_people= int(input("How many people to split the bill? "))
## Let's calculate the total bill amount after adding the tip
total_bill_with_tip= total_bill + (total_bill * tip_percentage / 100)
## Each person will pay the total bill amount after adding the tip divided by the no of people
each_person_pay= round(total_bill_with_tip / no_of_people, 2) # round off to 2 decimal places that how economy works
## Let's print the each person pay amount
print(f"Each person should pay: ${each_person_pay}")
