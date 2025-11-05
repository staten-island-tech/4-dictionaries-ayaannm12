# My Lil Store 🛒

items = [
    {"name": "Apple", "price": 1.00},
    {"name": "Bread", "price": 2.50},
    {"name": "Milk", "price": 2.00},
    {"name": "Eggs", "price": 3.50},
    {"name": "Chocolate", "price": 1.25}
]

print("Hi! Welcome to my store!")

cart = []
keep_going = True

while keep_going:
    print("Here’s what I have:")
    for i, thing in enumerate(items):
        print(f"{i+1}. {thing['name']} - ${thing['price']}")

    choice = input("Pick a number: ")

    if choice.isdigit():
        num = int(choice) - 1
        if 0 <= num < len(items):
            cart.append(items[num])
            print("You got a", items[num]['name'])
        else:
            print("That number is not real!")
    else:
        print("Type a number please!")

    again = input("More? (yes/no): ").lower()
    if again != "yes":
        keep_going = False

print("Your cart:")
total = 0

if cart:
    for thing in cart:
        print("-", thing['name'], "$", thing['price'])
        total += thing["price"]
    print("Total:", "$", total)
else:
    print("Your cart is empty 😢")

print("Thanks for shopping! 🎉")

