### Q5i

# Returns a tuple that contains two values:
#   - Maximum quantity of that item that can be bought with given amonut of money
#   - Change that customer should get
def calculate_max_quantity_and_change(unit_price, amount):
    
    # Determine maximum quantity
    max_quantity = int(amount // unit_price)
    
    # Determine change
    change = amount % unit_price
    
    # Return a tuple to hold both above results
    return (max_quantity, change)

    
# Use above function (for testing purposes)
#print(calculate_max_quantity_and_change(58.5, 130))