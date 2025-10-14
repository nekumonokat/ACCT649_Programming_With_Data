### Q5ii


# This allows us to use the function that we wrote in retail_utility.py
import retail_utility

# Prompt user for decimal number
amount = float(input("How much do you want to spend? $"))

# How much to buy 1kg = 1000g of honey
unit_price = 98.5

# Use function to calculate how many 1kg jars of honey and change
result1000 = retail_utility.calculate_max_quantity_and_change(unit_price, amount)

# Amount of money left over is the change (second value in above tuple)
amount = result1000[1]

# How much to buy 500g of honey
unit_price = 58.5

# Use function to calculate how many 500g jars of honey and change
result500 = retail_utility.calculate_max_quantity_and_change(unit_price, amount)

# Amount of money left over is the change (second value in above tuple)
amount = result500[1]

# How many grams of honey?
honey_grams = int(1000*result1000[0] + 500*result500[0])

# Print final result
print("You can buy " + str(honey_grams) + " grams of honey. You have $" + str(amount) + " left as your change.")