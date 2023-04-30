
from guitar import Guitar

CURRENT_YEAR = 2017


def run_tests():
    name = "Gibson L-5 CES"
    YEAR = 1922
    COST = 16035.40

    guitar = Guitar(name, YEAR, COST)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {9}. Got {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")


run_tests()