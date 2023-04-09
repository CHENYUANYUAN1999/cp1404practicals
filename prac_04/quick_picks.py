import random
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBER_PER_LINE = 6
quick_pick = int(input("How many quick picks? "))
for i in range(quick_pick):
    numbers = set()
    while len(numbers) < NUMBER_PER_LINE:
        numbers.add(random.randint(MIN_NUMBER, MAX_NUMBER))

    numbers = sorted(list(numbers))
    print(" ".join("{:2d}".format(number) for number in numbers))