# BH 2nd recursion.py
number = 5
factorial = 1
while number > 0:
    factorial *= number
    number -= 1

print(factorial)

def factor(num):
    if num == 1: return 1
    return num * factor(num-1)

print(factor(5))
number = 10
sequence = [1,1]

for i in range(1, number):
    sequence.append(sequence[i] + sequence[i-1])

print(sequence)