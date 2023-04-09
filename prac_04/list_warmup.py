numbers = [3,1,4,1,5,9,2]
"""
numbers[0] Answer: is the first element in the list
numbers[-1] Answer: is the last element in the list
numbers[3] Answer: is the fourth element in the list
numbers[:-1] Answer: is the all element except the last element in the list
numbers[3:4] Answer: is the fourth element in the list
5 in numbers Answer: is True
7 in numbers Answer: this will cause ValueError, since 7 is not in the list
"3" in numbers Answer: "3" is a string that does not in the list
numbers + [6, 5, 3] Answer: list will become numbers[3,1,4,1,5,9,2,6,5,3]
"""
"""1. Change the first element of numbers to "ten" (the string, not the number 10)"""
numbers[0] = "ten"
print(numbers)
"""2. Change the last element of numbers to 1"""
numbers[-1] = 1
print(numbers)
"""3. Print all the elements from numbers except the first two (slice)"""
print(numbers[2:])
"""4. Print whether 9 is an element of numbers"""
print(9 in numbers)