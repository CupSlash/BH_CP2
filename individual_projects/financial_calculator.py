#BH 2nd Financial Calculator
#ask what mode they want to do
mode_choice = input("Please choose the number that corresponds to your choice:\n 1. Savings Time Calculator\n 2. Compound Interest Calculator\n 3. Budget Allocator\n 4. Sale Price Calculator\n 5. Tip Calculator")
#find out what they said
if mode_choice == "1":
#Savings time calculator
    saving_amount = input("What amount are you saving to?")
    contribution_money = input("How much money are you contributing monthly?")
    months = saving_amount/contribution_money
    print(f"It will take {months} months to save ${saving_amount}")
elif mode_choice == "2":
#Compund interest calculator
    starting_amount = input("What is your starting amount")
    interest_rate = input("What is your yearly interest rate as a decimal?")
    time_compounding = input("How many years will you spend compounding")
    investment_gain = interest_rate * time_compounding
    final_amount = starting_amount * investment_gain
    print(f"In {time_compounding} years, you will have ${final_amount}")
elif mode_choice == "3":
#Budget allocator
    budget_cats = input("How many budget categories do you have?")
    for i in range(budget_cats):
    monthly_income = ("What is your monthly income:")
elif mode_choice == "4":
#sales price
elif mode_choice == "5":
#tip calculator
    bill = ("How much is the bill?")
    what per
else:
#else statement
    print("That is not an option.")