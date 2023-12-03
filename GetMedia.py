#Exercise 1. 
#Calculate the Media of 5 numbers

def Media_():
    
    number_1 = float(input("\nType the first number: "))
    number_2 = float(input("Type the second number: "))
    number_3 = float(input("Type the third number: "))
    number_4 = float(input("Type the fourth number: "))
    number_5 = float(input("Type the fifth number: "))
    
    media = (number_1 + number_2 + number_3 + number_4 + number_5) / 5
    
    print("\nThe result of the media is: ", media)

#def Media_():
    
    #numbers = []
    
    #for i in range(5):
        #number = float(input("Type the number: "))
        #numbers.append(number)
    
    #print("Números ingresados: ", numbers)
        
Media_()    