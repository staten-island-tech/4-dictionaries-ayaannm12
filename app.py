item0 = {
    "name": "Samsung 55\" 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps.",
}
item1 = {
    "name": "Apple Macbook pro 2025  ",
    "price": 1699.99,
    "department": "Laptops",
    "description": "Apple laptop with 16 gb ram."
}
item2 = {

 "name": "Apple iphone 16 plus",
        "price": 1000.99,
        "department":"phones",
        "Description": "apple iphone 16 plus cellular phone with wifi calling"

}
print(f"Here is what we have for sale:{item0} {item1} {item2}")

want = input("For the Samsung TV, hit 1: For the Apple macbook, hit 2: For the Apple Iphone 16 plus hit 3 ")

while want != "1" "2" "3":
    print("Not a valid answer, please try again.")
    print("Here is what we h ave for sale:")
    print(item0,item1)
    
    want = input("For the Samsung TV, hit 1:  For the Apple Macbook pro, hit 2: For the Apple Iphone 16 plus hit 3  ")

print("Added to cart!") 


more = input("Do you want anything else? (yes/no): ").lower()

while more != "no":
 
    while more not in ["yes", "no"]:
        print("Not a valid answer, please type 'yes' or 'no'.")
        more = input("Do you want anything else? (yes/no): ").lower()

    if more == "no":
        break

    print("Here is what we have for sale again:")
    print(item0,item1)

    want = input("For the Samsung TV, hit 1:  For the Apple macbook, hit 2: For the Apple Iphone 16 plus hit 3  ")
    while want != "1" "2":
        print("Not a valid answer, please try again.")
        want = input("For the Samsung TV, hit 1: For the Apple macbook, hit 2: For the Apple Iphone 16 plus hit 3 ")

    print("Added to cart!")
    more = input("Do you want anything else? (yes/no): ").lower()

print("Thanks for shopping with us!")
#now find a way to keep track of the cart so the user can go back to take a look at it
