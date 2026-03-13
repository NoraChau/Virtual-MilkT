base = ['Classic', 'Honey', 'Thai', 'Jasmine', 'Taro']
basePrice = [4.50, 5.00, 5.00, 5.25, 5.25]

#basePrice = {
#    "Classic": 4.50,
#    "Honey": 5.00,
#    "Thai": 5.00,
#    "Jasmine": 5.25,
#    "Taro": 5.25
#}

top = ['Black Tapioca', 'White Tapioca', 'Egg Pudding', 'Jelly Pearl', "Milk Foam"]
topPrice = [.25, .25, .75, .5, .75]

size = ['Small', 'Medium', 'Large', 'Mega']
sizePrice = [0, .25, .5, 1]

order_list = []

"""
The procedure take in a list of orders, calculate the total price, and print the receipt
"""
def print_receipt(order):
    # Calculate total
    total = 0
    for i in range(len(order)):
        if order[i][0] == 'base':
            total += basePrice[order[i][1]-1]
        elif order[i][0] == 'top':
            total += topPrice[order[i][1]-1]
        else:
            total += sizePrice[order[i][1]-1]
    
    # Receipt
    print("""
Here is your receipt:
""")
    for i in range(len(order)):
        if order[i][0] == 'base':
            print(f"{base[order[i][1]-1]} Milk Tea     ${basePrice[order[i][1]-1]}")
        elif order[i][0] == 'top':
            print(f"{top[order[i][1]-1]}     ${topPrice[order[i][1]-1]}")
        else:
            print(f"{size[order[i][1]-1]} Size         ${sizePrice[order[i][1]-1]}")
    print("-------------------------")
    print(f"Total:          ${total}")
    

######################################

print("Welcome to the Virtual MilkT. I'm Bobot (short for Boba Robot), and I will be your assistant today.")


# Print base menu, get base selection
print("""
Milk Teas""")

for i in range(len(base)):
    print(f"{i+1}. {base[i]} Milk Tea    ${basePrice[i]}")
order_list.append(['base', int(input("""
Please enter the number of your selection: """))])


# Print Size menu, get Size selection
print("""
Drink Sizes""")

for i in range(len(size)):
    print(f"{i+1}. {size[i]}     +${sizePrice[i]}")
order_list.append(['s', int(input("""
Please enter the number of your selection: """))])


# Print Topping menu, get Topping selection
print("""
Toppings""")

for i in range(len(top)):
    print(f"{i+1}. {top[i]}     ${topPrice[i]}")
print("")
while True:
    choice = int(input("""Please enter the number of your selection (0 to STOP): """))
    if choice == 0:
        break
    else:
        order_list.append(['top', choice])

print_receipt(order_list)