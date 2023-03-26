"Shop calculator"
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
DISCOUNT = 0.9
sum = 0
for i in range(1,number_of_items+1):
    price_of_item = float(input(("Price of item: ")))
    sum += price_of_item
    if sum > 100:
        sum = sum * DISCOUNT
    else:
        sum = sum
print(sum)