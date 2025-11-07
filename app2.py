# items in the store
item0 = {
    "name": "Samsung 55\" 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
}
item1 = {
    "name": "Apple Macbook Pro 2025",
    "price": 1699.99,
    "department": "Laptops",
    "description": "Apple laptop with 16 GB RAM."
}
item2 = {
    "name": "Apple iPhone 16 Plus",
    "price": 1000.99,
    "department": "Phones",
    "description": "Apple iPhone 16 Plus with WiFi calling."
}

# intro
print("Welcome to Ayaan's Tech Store!")
print("Here is what we have for sale:")
print(item0)
print(item1)
print(item2)

cart = []

# main shopping part
want = input("For the Samsung TV, hit 1. For the Macbook, hit 2. For the iPhone 16 Plus, hit 3: ")

while want not in ("1", "2", "3"):
    print("Not a valid answer, please try again.")
    want = input("For the Samsung TV, hit 1. For the Macbook, hit 2. For the iPhone 16 Plus, hit 3: ")

if want == "1":
    print("You added the", item0["name"], "to cart.")
    cart.append(item0)
elif want == "2":
    print("You added the", item1["name"], "to cart.")
    cart.append(item1)
elif want == "3":
    print("You added the", item2["name"], "to cart.")
    cart.append(item2)

more = input("Do you want anything else? (yes/no): ").lower()

while more == "yes":
    print("Okay, here’s what we got again:")
    print(item0)
    print(item1)
    print(item2)
    want = input("Pick 1 for TV, 2 for Macbook, 3 for iPhone: ")

    if want == "1":
        print("You added the", item0["name"], "to cart.")
        cart.append(item0)
    elif want == "2":
        print("You added the", item1["name"], "to cart.")
        cart.append(item1)
    elif want == "3":
        print("You added the", item2["name"], "to cart.")
        cart.append(item2)
    else:
        print("Not valid! Try again.")

    more = input("Do you want anything else? (yes/no): ").lower()

if more == "no":
    print("Thanks for shopping with us! Here is your cart:")
    for thing in cart:
        print("-", thing["name"], "($", thing["price"], ")")
    print("Please proceed to checkout :)")