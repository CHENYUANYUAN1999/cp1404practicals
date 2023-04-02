import random
dir(random)
"""What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
Answer: line 1 The smallest number is 5, The largest number is 19

What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
Answer: line 2 The smallest number is 3, The largest number is 9, and no

What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
Answer: line 3 The smallest number is 2.500000000000, The largest number is 5.49999999999999999

Write code, not a comment, to produce a random number between 1 and 100 inclusive."""

print(random.randint(5, 20))
print(random.randrange(3, 10, 2))
print(random.uniform(2.5, 5.5))

print(random.randint(1,101))