#BH 2nd Financial Calculator
#FUNCTION
def calculate_compound_interest(P, r, t):
    A = P * (1+r/12)**(12*t)
    return A
def application():
    def calculate_tip_discount(tip_or_discount):
        bill = float(input("How much is the bill?"))
        modifier = float(input(f"What is the {tip_or_discount}?"))
        if tip_or_discount == "tip":
            total = bill + modifier
        else:
            total = bill - modifier
        print(f"your total is ${total:.2f}")
    def process_savings_time():
        saving_amount = float(input("What amount are you saving to?"))
        contribution_money = float(input("How much money are you contributing monthly?"))
        months = saving_amount/contribution_money
        print(f"It will take {months} months to save ${saving_amount:.2f}")
    def process_compound_interest():
        P = float(input("What is your starting amount?"))
        r = float(input("What is your yearly interest rate as a decimal?"))
        t = float(input("How many years will you spend compounding?"))
        A = calculate_compound_interest(P, r, t)
        print(f"In {t} years, you will have ${A:.2f}")
    def process_budget_allocation():
        monthly_income = float(input("What is your monthly income:"))
        needs_percent = float(input("What decimal percentage of your monthly income is spent on things you need?"))
        wants_percent = float(input("What decimal percentage of your monthly income is spent on things you want?"))
        savings_percent = float(input("What decimal percentage of your monthly income is put into savings?"))
        needs_cash = monthly_income * needs_percent
        wants_cash = monthly_income * wants_percent
        savings_cash = monthly_income * savings_percent
        print(f"You spend ${needs_cash:.2f} on your monthly needs, ${wants_cash:.2f} on your monthly wants, and ${savings_cash:.2f} goes into your savings account each month.")
    def process_sales_price():
        tip_or_discount = "discount"
        calculate_tip_discount(tip_or_discount)
    def process_tip():
        tip_or_discount = "tip"
        calculate_tip_discount(tip_or_discount)
    def calculator():
        while True:
            #ask what mode they want to do
            mode_choice = input("Please choose the number that corresponds to your choice:\n 1. Savings Time Calculator\n 2. Compound Interest Calculator\n 3. Budget Allocator\n 4. Sale Price Calculator\n 5. Tip Calculator\n 6. Exit\n")
            #find out what they said
            if mode_choice == "1":
                process_savings_time()
            #Savings time calculator
            elif mode_choice == "2":
                process_compound_interest()
            #Compund interest calculator
            elif mode_choice == "3":
            #Budget allocator
                process_budget_allocation()
            elif mode_choice == "4":
            #sales price
                process_sales_price()
            elif mode_choice == "5":
            #tip calculator
                process_tip()
            elif mode_choice == "6":
                print("bye!")
                break
            else:
            #else statement
                print("That is not an option.")
    calculator()
application()