#BH 2nd input_validators.py
# Check to see if the user input is a positive number between 0 and 100. If it is, return the number. If it isn't, ask them to try again until they enter a valid number.
def check_float_value(value):
    message = "Please enter a positive number between 0 and 100."
    while True:
        try:
            value = float(value)

            if (value >= 0 and value <= 100):
                return value
            else:
                value = input(message)
        except ValueError:
            value = input(message)
