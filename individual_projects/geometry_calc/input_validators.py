#BH 2nd input_validators.py
# Check to see that the input value is a positive float. If it is, return the value as a float. If it isn't, ask the user to enter a new value until they enter a valid one.
def positive_float_check(value):
    message = "Please enter a positive number."
    while True:
        try:
            value = float(value)

            if (value > 0):
                return value
            else:
                value = input(message)
        except ValueError:
            value = input(message)