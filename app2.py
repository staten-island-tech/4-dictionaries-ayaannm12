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

cart = []
cart.append(want)

while want not in ("1", "2", "3"):
    print("Not a valid answer, please try again.")
    print("Here is what we have for sale:")
    print(item0,item1,item2)

if want == "1":
    print("You have added the", item0, "to cart")
elif want == "2":
      print("You have added the", item1, "to cart")
if want == "3":
    print("You have added the", item2, "to cart")

more = input("Do you want anything else? (yes/no): ").lower()

while more != "no":
    print(f"Here is what we have for sale:{item0} {item1} {item2}")
    want = input("For the Samsung TV, hit 1: For the Apple macbook, hit 2: For the Apple Iphone 16 plus hit 3 ")
    cart = []
    cart.append(want)




if more == "no":
    print("thanks for shopping with us, please proceed to theck out, here is Your cart!", cart)



want = input("For the Samsung TV, hit 1: For the Apple macbook, hit 2: For the Apple Iphone 16 plus hit 3 ")


while want not in ("1", "2", "3"):
    print("Not a valid answer, please try again.")
    print("Here is what we have for sale:")
    print(item0,item1,item2)

cart = []
cart.append(want)

if want == "1":
    print("You have added the", item0, "to cart")
elif want == "2":
      print("You have added the", item1, "to cart")
if want == "3":
    print("You have added the", item2, "to cart")
      
    while more not in ["yes", "no"]:
        print("Not a valid answer, please type 'yes' or 'no'.")
        more = input("Do you want anything else? (yes/no): ").lower()

    if more == "no":
        print("thanks for shopping with us, please proceed to theck out!"
              "here is Your cart!", cart
              )
