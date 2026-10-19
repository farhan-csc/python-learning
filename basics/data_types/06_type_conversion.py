""" Type conversion is the process of changing a data type, 
for example int to float or from string to int """

age = "20"
price = 15000
score = 85.7

# Before changing
print(age, type(age))
print(price, type(price))
print(score, type(score))

age_int = int(age)
price_float = float(price)
score_int = int(score)

print("")
# After changing
print(age_int, type(age_int))
print(price_float, type(price_float))
print(score_int, type(score_int))