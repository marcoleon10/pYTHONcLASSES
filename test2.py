def students():
    names = ["Dave", "Jazper",  "Andy", "Corey", "Samuel", "Cesar", "Darius", "Demetri", "Janaye", "Donald", "Marco"]
    print(names)
    names.append("Sergio")
    
    for x in names:
        print(x)
        
    print(len[students])
    
    
def products():
    prices = [23, 234, 34, 672, 77, 214, 756, 76, 500, 479, 629, 325, 389, 29, 101, 50, 67, 800, 54]
    
    # A) print every price
    # B) sum of all prices
    # C) how many prices are lower than 500
    # D) how many are greater or equal to 500
    
    total = 0
    count = 0
    
    for price in prices:
        print(price)
        total += price
        if price < 500:
            count += 1
            
    print(total)
    print(count)

def art():
    colors = ["red", "blue", "pink", "blue", "white", "blak", "green", "blak", "red", "white", "blue", "yellow"]
    
    #a) how many colors are in the list
    print(len(colors))
    
    #b) how many are blue
    countBlue=0
    for x in colors:
        if x == "blue":
            count += 1
    print("blues are " + str(countBlue)) 
            
    #c) how many are white or black
    countBlackWhite = 0
    for x in colors:
        if x == "white" or x == "black":
            countBlackWhite += 1
    print("black and white are " + str(countBlackWhite))
    
#calls
students()
art()