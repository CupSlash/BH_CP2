#BH 2nd helper.py
def float_check(value):
    while True:
        try:
            return float(value)
        except ValueError:
            value = input("That is not a valid number. Please enter a number.")
