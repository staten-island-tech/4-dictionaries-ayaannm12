items = {
    "name": "Samsung 55\" 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
}

print("Here is what we have for sale:", items)

want = input("For the Samsung TV, hit 1: ")

# Input validation for the first item
while want != "1":
    print("Not a valid answer, please try again.")
    print("Here is what we have for sale:")
    print(items)
    want = input("For the Samsung TV, hit 1: ")

print("Added to cart!")

# Ask if they want more
more = input("Do you want anything else? (yes/no): ").lower()

# Keep looping until user says no
while more != "no":
    # If it's not yes or no, show error message
    while more not in ["yes", "no"]:
        print("Not a valid answer, please type 'yes' or 'no'.")
        more = input("Do you want anything else? (yes/no): ").lower()

    if more == "no":
        break

    # If yes, repeat the process
    print("\nHere is what we have for sale again:")
    print(items)

    want = input("For the Samsung TV, hit 1: ")
    while want != "1":
        print("Not a valid answer, please try again.")
        want = input("For the Samsung TV, hit 1: ")

    print("Added to cart!")
    more = input("Do you want anything else? (yes/no): ").lower()

print("Thanks for shopping with us!")