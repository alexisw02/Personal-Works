#Excercise #¿?
#Do a Calculator

def calculator_():
    
    def addition():
        add = number_1 + number_2
        return add

    def subtraction():
        sub = number_1 - number_2
        return sub

    def multiply():
        mul = number_1 * number_2
        return mul

    def divition():
        if number_1 != 0 and number_2 != 0:
            div = number_1 / number_2
            return div
        else:
            print("Error! Isn't possible a divide by 0")

    def square():
        squ = pow(number_1, number_2)
        return squ

    while True:
        print("\nCalculator")
        print("Addition.......................[1]")
        print("Subtraction....................[2]")
        print("Multiply.......................[3]")
        print("Divition.......................[4]")
        print("Square.........................[5]")
        print("Exit...........................[6]\n")

        option = input("Type your choice: ")
        
        if option == '1':
            print("\nAddition:")

        elif option == '2':
            print("\nSubtraction:")

        elif option == '3':
            print("\nMultiply:")

        elif option == '4':
            print("\nDivition:")

        elif option == '5':
            print("\nSquare:")
        
        elif option == '6':
            print("\nLeaving....")
            break

        number_1 = float(input("Type the first number: "))
        number_2 = float(input("Type the second number: "))

        if option == '1':
            result = addition()

        elif option == '2':
            result = subtraction()

        elif option == '3':
            result = multiply()

        elif option == '4':
            result= divition()

        elif option == '5':
            result = square()

        print("The result is: ", result)

calculator_()