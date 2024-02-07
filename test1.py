def say_hello():
    print("Hello World")
    print("Im in a function")
    
def say_hi(name):
    print("Hi" + name)
    
    
def give_me_a_beer(age):
    if age >= 18:
        print("Here is your beer")
    elif age >= 90:
        print("Your beer is from the house")
    else:
        print("You are a minor")
    
say_hello()

say_hi("Marco")

give_me_a_beer(15)
give_me_a_beer(18)
give_me_a_beer(90)