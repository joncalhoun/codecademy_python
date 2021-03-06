shopping_list = ["banana", "orange", "apple"]

stock = { "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = { "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    cost = 0
    for f in food:
        if stock[f] > 0:
            stock[f] -= 1
            cost += prices[f]
    return cost
