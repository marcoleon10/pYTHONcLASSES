def about_me():
    me = {
        "first":"Marco",
        "last":"Leon",
        "age":21,
        "address": {
            "street":"Evergreen",
            "number":"42",
            "city": "Springfield",
            "zip": "12345"
        }
    }
    
    print(me)
    
    #read values
    print(me["first"] + " " + me["last"])
    print(f"And I'm {me["age"]} years old")
    
    #print(me["address"]["street"]) #first option
    
    address = me["address"] #second option
    print(address["street"])
    
    street = address["street"]
    number = address["number"]
    city = address["city"]
    
    
    print(f"Street: {address["street"]}, Number:#{address["number"]}, City: {address["city"]}, ZIP: {address["zip"]}") #first option
    print(f"Street: {street}, Number:#{number}, City: {city}, ZIP: {address["zip"]}") #second option
    
    

about_me()