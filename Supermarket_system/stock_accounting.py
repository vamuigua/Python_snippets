#List of Fruit stock
shopping_list = ["banana", "orange", "apple"]

#Fruit stock/quantity as a Dictionary
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

#Prices of each Fruit    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

#Function to check stock count
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
        else:
            total = total
    return total
