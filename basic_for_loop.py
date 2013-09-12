my_list = [1,9,3,8,5,7]

for number in my_list:
    print 2 * number
    
start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
    square_list.append(number ** 2)
    square_list.sort()

print square_list

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a:
    if number%2==0:
        print number
        
# Combine Lists and Functions:
def fizz_count(x):
    count = 0
    for number in x:
        if number == "fizz":
            count = count + 1
    return count
  
prices = {"banana" : 4,
          "apple" : 2,
          "orange" : 1.5,
          "pear" : 3}
          
stock = {"banana" : 6,
         "apple" : 0,
         "orange" : 32,
         "pear" : 15}
         
for item in prices and stock:
    print item
    print "price: %s" % prices[item]
    print "stock: %s" % stock[item]
    
    worth = 0

for item in prices and stock:
    worth += prices[item] * stock[item]
    
print worth


def compute_bill(food):
    total = 0
    for item in food:
        total += prices[item]
    return total
  
print total