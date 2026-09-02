ram = 8
weight = 1.5
price = 30000000
discount = 9.0

print(f"Ram: {ram} {type(ram)}")
print(f"Weight: {weight} {type(weight)}")
print(f"Price: {price} {type(price)}")
print(f"Discount: {discount}% {type(discount)}")

discount_amount = price * discount / 100
final_price = price - discount_amount

print(f"The total discount is: {discount_amount}")
print(f"Total amount payable is: {final_price}")