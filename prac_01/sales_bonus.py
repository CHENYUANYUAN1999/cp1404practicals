"""
1.Sale Bonus
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
while sales >= 0
    calculate bonus
    get sales
do next thing
"""
sales = float(input("Enter sales: $"))
UPPER_BONUS_RATE = 0.15
LOWER_BONUS_RATE = 0.1
while sales >= 1000:
    bonus = sales * UPPER_BONUS_RATE
    print(f"Bonus is: ${bonus}")
    sales = float(input("Enter sales: $"))
bonus = sales * LOWER_BONUS_RATE
print(f"Bonus is: ${bonus}")