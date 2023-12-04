#Exercise 1. 
#Calculate the Media of 5 numbers

def Media_():
    
    number = []
    media = 0
    
    for array in range(5):
        number = float(input("Type a number: "))
        media += number
    media /= 5
    
    print("\nThe media is: ", media)

Media_()    