#RESTAURANT
#informing the number of people and the price of the meal, the program will calculate the total amount to be paid and the amount per person.
#introduction and menu
print(15*'-')
print("WELCOME TO THE RESTAURANT!")
print("\nHere is the menu:")

menu = {
    "Chicken": 10.99, 
    "Beef": 12.99,
    "Fish": 14.99,
    "Vegetarian": 9.99,
}
for item, price in menu.items():
    print(f"{item}: ${price:.2f}")

#dictionary to store the names and orders of people joining
people_joining = {}

#loop to get the names and orders of people joining
while True:
    name = input("\nEnter your name: ")
    print("What would you like to order?")

    while True:
        order = input("Enter your order: ")

        if order.title() in menu:
            order_price = menu[order.title()]
            break
        else:
            print("Sorry, we don't have that item on the menu. Please choose from the menu.")
            print(15*'-')

    #store the order in the dictionary
    people_joining[name] = order_price

    print("\nIs someone else joining you for the order?")
    else_joining = input("Type 'yes' if you want to join someone else's order or 'no' if there's none after you: ")

    if else_joining.lower() == "no":
        break

#calculate the total amount to be paid and the amount per person and the 15% tip
total_amount = 0
for order_price in people_joining.values():
    total_amount += order_price

tip = total_amount * 0.15
total_amount_with_tip = total_amount + tip

#calculate the amount per person
amount_per_person = total_amount_with_tip / len(people_joining)

#display the total amount to be paid and the amount per person
print(f"The total amount to be paid is: ${total_amount:.2f}")
print(f"The tip is: ${tip:.2f}")
print(f"The total amount with tip is: ${total_amount_with_tip:.2f}")
print(f"The amount per person is: ${amount_per_person:.2f}")