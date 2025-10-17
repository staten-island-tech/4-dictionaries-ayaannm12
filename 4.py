items = [
    {
        "name": "Samsung 55\" 4K UHD TV",
        "price": 429.99,
        "department": "Televisions",
        "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
    },
    {
        "name": "Apple iphone 16 plus",
        "price": 1000.99,
        "department":"phones",
        "Description": "apple iphone 16 plus cellular phone with wifi calling"
    },
    {
        "name": "Macbook air 2025",
        "price": 1400.00,
        "department":"Laptops",
        "Description": "Apple macbook air 2025 with 512gb SSD and 16 GB of memory with m4 chip"
    }
]
# print("here are the items we have for sale")
# print(item,
#        item2,
#          item3)

sale = input("What item would you like to buy? [0] Samsung tv  [1]iphone 16  [2] Macbook air 2025")
if sale == "0":
     print(items[0]["price"])
elif sale == "b":
     print("That will be ")