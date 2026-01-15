#BH 2nd Financial Calculator
#FUNCTION
def application():
    def tip_discount_calculator(tip_or_discount):
            bill = float(input("How much is the bill?"))
            modifier = float(input(f"What is the {tip_or_discount}?"))
            if tip_or_discount == "tip":
                total = bill + modifier
            else:
                total = bill - modifier
            print(f"your total is ${total}")
    def savings_time():
        saving_amount = float(input("What amount are you saving to?"))
        contribution_money = float(input("How much money are you contributing monthly?"))
        months = saving_amount/contribution_money
        print(f"It will take {months} months to save ${saving_amount}")
    def compund_interest():
        starting_amount = float(input("What is your starting amount"))
        interest_rate = float(input("What is your yearly interest rate as a decimal?"))
        time_compounding = float(input("How many years will you spend compounding"))
        investment_gain = (interest_rate + 1)**time_compounding
        final_amount = starting_amount * investment_gain
        print(f"In {time_compounding} years, you will have ${final_amount}")
    def budget_allocator():
        monthly_income = float(input("What is your monthly income:"))
        needs_percent = float(input("What decimal percentage of your monthly income is spent on things you need?"))
        wants_percent = float(input("What decimal percentage of your monthly income is spent on things you want?"))
        savings_percent = float(input("What decimal percentage of your monthly income is put into savings?"))
        needs_cash = monthly_income * needs_percent
        wants_cash = monthly_income * wants_percent
        savings_cash = monthly_income * savings_percent
        print(f"You spend ${needs_cash} on your monthly needs, ${wants_cash} on your monthly wants, and ${savings_cash} goes into your savings account each month.")
    def sales_price():
        tip_or_discount = "discount"
        tip_discount_calculator(tip_or_discount)
    def tip_calculator():
        tip_or_discount = "tip"
        tip_discount_calculator(tip_or_discount)
    def calculator():
        while True:
            #ask what mode they want to do
            mode_choice = input("Please choose the number that corresponds to your choice:\n 1. Savings Time Calculator\n 2. Compound Interest Calculator\n 3. Budget Allocator\n 4. Sale Price Calculator\n 5. Tip Calculator\n 6. Exit\n")
            #find out what they said
            if mode_choice == "1":
                savings_time()
            #Savings time calculator
            elif mode_choice == "2":
                compund_interest()
            #Compund interest calculator
            elif mode_choice == "3":
            #Budget allocator
                budget_allocator
            elif mode_choice == "4":
            #sales price
                sales_price
            elif mode_choice == "5":
            #tip calculator
                tip_calculator()
            elif mode_choice == "6":
                print("bye!")
                break
            else:
            #else statement
                print("That is not an option.")
    calculator()
application()