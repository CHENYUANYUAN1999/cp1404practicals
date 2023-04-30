"""
CP1404/CP5632 Practical - Suggested Solution
Guitar program.
"""
from guitar import Guitar


def main():
    guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]

    print("My guitars!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(guitar_name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "added.")
        guitar_name = input("Name: ")

    print("\n... snip ...\n")
    print("These are my guitars:")

    for i, guitar in enumerate(guitars):
        vintage_str = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i + 1}: {guitar.name} ({guitar.year}){vintage_str}, worth $ {guitar.cost:.2f}")

main()