#uses input to gather bill amnt, tip amnt, and number of people paying
#converts inputs to float types
#bill input uses .lstrip() (ahead of course) to remove "$" if present
#tip percent input uses .strip() + .rstrip() (ahead of course) to remove spaces and "%"
#print lines use formatting ":.2f" (ahead of course) to always display 2 decimals
#:.2f strips the output values down to 2 decimals instead of using round()
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?: ").strip().lstrip("$"))
tip_percent = float(input("What percent tip are you leaving?: ").strip().rstrip("%"))
tip_amount = ((tip_percent/100)* total_bill)
people_amount = int(input("How many people are splitting the bill?: "))
grand_total = (total_bill + tip_amount) / people_amount
print(f"Tip: ${tip_amount:.2f}")
print(f"Each person pays ${grand_total:.2f}")
