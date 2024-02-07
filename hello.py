print ("Hello World!")
var = 10
print (var)

#variables
x = 5
y = 3

#operations
sum = x + y

#string operations
name = "adrian"
greating = "Hello, " + name + "!"
print(greating)

#list //this is the arrays
numbers = [1, 2, 3, 4, 5]


#loop
for number in numbers:
    print(number)
    
age = 15
if age < 18:
    print("You are a minor")
else:
    print("You are an adult")
    
print("you're an adult") if age >= 18 else print("you're a minor")

#for(i-0;i<numbers.lenght;i++)
    #let number = numbers[i]
    #console.log(number)

#JS compartive
#function(){
    #console.log("Hello World")
#}

#Define the function in python
def greet(name):
    return "Hello" + name

#Call the function
result = greet("Marco")
example = 1
example2 = "2"
print(example + int(example2))

#function to calculate the power of a number
def power(base, exponent=2):
    return base ** exponent

result = power(2)
result2 = power(2, 3)

#print the result
print(result)
print(result2)

#Create a funciton that multiply 2 parameters (numbers)
def multiply(num1, num2):
    return num1 * num2

product = multiply(12,12)
print(product)