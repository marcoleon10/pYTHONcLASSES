def products_test():
    products = [
        {
            "title": "Smartphone",
            "image": "smartphone.jpg",
            "price": 299.99,
            "category": "Electronics",
        },
        {
            "title": "Running Shoes",
            "image": "running_shoes.jpg",
            "price": 89.99,
            "category": "Footwear",
        },
        {
            "title": "Backpack",
            "image": "backpack.jpg",
            "price": 49.99,
            "category": "Accessories",
        },
        {
            "title": "Coffee Maker",
            "image": "coffee_maker.jpg",
            "price": 119.99,
            "category": "Home Appliances",
        },
        {
            "title": "Wireless Headphones",
            "image": "wireless_headphones.jpg",
            "price": 159.99,
            "category": "Electronics",
        },
        {
            "title": "Fitness Tracker",
            "image": "fitness_tracker.jpg",
            "price": 59.99,
            "category": "Wearables",
        },
        {
            "title": "Digital Camera",
            "image": "digital_camera.jpg",
            "price": 349.99,
            "category": "Electronics",
        },
        {
            "title": "Yoga Mat",
            "image": "yoga_mat.jpg",
            "price": 25.99,
            "category": "Fitness",
        },
        {
            "title": "Novel - 'Mystery of the Old Manor'",
            "image": "novel.jpg",
            "price": 14.99,
            "category": "Books",
        },
        {
            "title": "Portable Charger",
            "image": "portable_charger.jpg",
            "price": 39.99,
            "category": "Electronics",
        },
    ]

    # A) Print: title $price
    # B) What is the total of Electronics?
    # C) How many Electronics products exist in the list?
    
    total=0
    count=0
    for electronics in products:
        total += electronics["price"]
        print(f"{electronics["title"]} ${electronics["price"]}")
        if(electronics["category"] == "Electronics"):
            count += 1
    print(f"The total value is {total}")
    print(f"There are {count} Electronics")

    
    #---------------EXTRA----------------
    # D) Find the cheapest 
    # E) List of unique categories (a list with each category only once)
    
    min_value = min(products.values()) #by using only the values of the dictionary, used the min function that return the lowest value of the list
    min_key = [key for key, value in products.items() if value == min_value][0]
    print(f"The cheapest product is {min_key} with ${min_value}")
    
    #using sets to find those unique categories thanks to its property of not allowing duplicates
    categories = set()
    for category in products:
        categories.add(category["category"])
    print(categories)
    
    
products_test()