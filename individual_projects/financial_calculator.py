#BH 2nd Financial Calculator
#FUNCTION
def tip_discount_calculator(tip_or_discount):
        bill = float(input("How much is the bill?"))
        modifier = float(input(f"What is the {tip_or_discount}?"))
        if tip_or_discount == "tip":
            total = bill + modifier
        else:
            total = bill - modifier
        print(f"your total is ${total}")
def calculator():
    #ask what mode they want to do
    mode_choice = input("Please choose the number that corresponds to your choice:\n 1. Savings Time Calculator\n 2. Compound Interest Calculator\n 3. Budget Allocator\n 4. Sale Price Calculator\n 5. Tip Calculator\n")
    #find out what they said
    if mode_choice == "1":
    #Savings time calculator
        saving_amount = float(input("What amount are you saving to?"))
        contribution_money = float(input("How much money are you contributing monthly?"))
        months = saving_amount/contribution_money
        print(f"It will take {months} months to save ${saving_amount}")
    elif mode_choice == "2":
    #Compund interest calculator
        starting_amount = float(input("What is your starting amount"))
        interest_rate = float(input("What is your yearly interest rate as a decimal?"))
        time_compounding = float(input("How many years will you spend compounding"))
        investment_gain = interest_rate * time_compounding
        final_amount = starting_amount * investment_gain
        print(f"In {time_compounding} years, you will have ${final_amount}")
    elif mode_choice == "3":
    #Budget allocator
        monthly_income = float(input("What is your monthly income:"))
        needs_percent = float(input("What decimal percentage of your monthly income is spent on things you need?"))
        wants_percent = float(input("What decimal percentage of your monthly income is spent on things you want?"))
        savings_percent = float(input("What decimal percentage of your monthly income is put into savings?"))
        needs_cash = monthly_income * needs_percent
        wants_cash = monthly_income * wants_percent
        savings_cash = monthly_income * savings_percent
        print(f"You spend ${needs_cash} on your monthly needs, ${wants_cash} on your monthly wants, and ${savings_cash} goes into your savings account each month.")
    elif mode_choice == "4":
    #sales price
        tip_or_discount = "discount"
        tip_discount_calculator(tip_or_discount)
    elif mode_choice == "5":
    #tip calculator
        tip_or_discount = "tip"
        tip_discount_calculator(tip_or_discount)
    else:
    #else statement
        print("That is not an option.")









calculator()