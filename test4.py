
def computer_store():
    catalog = [
        {"title": "Keyboard", "price": 45.33},
        {"title": "Mouse", "price": 20.00},
        {"title": "4K Monitor", "price": 195.93},
        {"title": "Ultrawide Monitor", "price": 425.16},
        {"title": "Webcam", "price": 42.50},
    ]
    
    #a) print all the titles
    #b) the total value of the catalog (sum of all prices)
    total = 0
    for product in catalog:
        print(product["title"])
        total += product["price"]
    
    print(f"The total is{total}")
    




def school():
    students = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "age": 34,
            "grade": "A",
            "due_balance": 325.00,
        },
        {
            "first_name": "Carlos",
            "last_name": "Rodriguez",
            "age": 56,
            "grade": "B",
            "due_balance": 30.00,
        },
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "age": 37,
            "grade": "B",
            "due_balance": 0.00,
        },
        {
            "first_name": "Carlos",
            "last_name": "Rodriguez",
            "age": 56,
            "grade": "B",
            "due_balance": 30.00,
        },
        {
            "first_name": "Emma",
            "last_name": "Smith",
            "age": 22,
            "grade": "B",
            "due_balance": 150.00,
        },
        {
            "first_name": "Liam",
            "last_name": "Johnson",
            "age": 20,
            "grade": "A",
            "due_balance": 200.00,
        },
        {
            "first_name": "Olivia",
            "last_name": "Williams",
            "age": 23,
            "grade": "C",
            "due_balance": 220.00,
        },
        {
            "first_name": "Noah",
            "last_name": "Brown",
            "age": 21,
            "grade": "B",
            "due_balance": 180.00,
        },
        {
            "first_name": "Ava",
            "last_name": "Jones",
            "age": 24,
            "grade": "A",
            "due_balance": 300.00,
        },
        {
            "first_name": "Ethan",
            "last_name": "Garcia",
            "age": 25,
            "grade": "C",
            "due_balance": 100.00,
        },
        {
            "first_name": "Sophia",
            "last_name": "Miller",
            "age": 26,
            "grade": "B",
            "due_balance": 250.00,
        },
    ]
    
    #a)print First Last name for A students
    #b) the total due_balance of all students
    total = 0
    """
    Create a for loop 
    get every student from the list
    from the student get the first and last
    """
    
    for student in students:
        total += student["due_balance"]
        if(student["grade"] == "A"):
            print(f"First: {student["first_name"]}, Last: {student["last_name"]}")

    print(f"The total due_balance is {total}")

#fn calls
computer_store()
school()