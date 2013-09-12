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

def compute_bill(shopping_list):
    total = 0
    for item in shopping_list:
        if stock[item] > 0:
            stock[item] -= 1
	    total += prices[item]
    return total

print compute_bill(shopping_list)
print stock