"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: When the user's input is non-integer
2. When will a ZeroDivisionError occur?
Answer: When the input of denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: Yes, we can add the error checking before performing division operation.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator can not be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")