def calculadora_():
    
    def sumas():
        suma = numero_1 + numero_2
        return suma

    def restas():
        resta = numero_1 - numero_2
        return resta

    def multiplicaciones():
        multiplicacion = numero_1 * numero_2
        return multiplicacion

    def divisiones():
        if numero_1 != 0 and numero_2 != 0:
            division = numero_1 / numero_2
            return division
        else:
            print("Error! No es posible dividir entre 0")

    def potenciacion():
        potencia = pow(numero_1, numero_2)
        return potencia

    while True:
        print("\nBienvenido a la calculadora\n")
        print("Sumar.......................[1]")
        print("Restar......................[2]")
        print("Multiplicar.................[3]")
        print("Dividir.....................[4]")
        print("Potencia....................[5]")
        print("Salir.......................[6]\n")

        opcion = input("Ingrese su elección: ")
        
        if opcion == '6':
            print("\nSaliendo....")
            break

        if opcion == '1':
            print("\nSuma:")

        if opcion == '2':
            print("\nResta:")

        if opcion == '3':
            print("\nMultiplicación:")

        if opcion == '4':
            print("\nDivisión:")

        if opcion == '5':
            print("\nPotencia:")

        numero_1 = float(input("Digite el primer número: "))
        numero_2 = float(input("Digite el segundo número: "))

        if opcion == '1':
            resultado = sumas()

        if opcion == '2':
            resultado = restas()

        if opcion == '3':
            resultado = multiplicaciones()

        if opcion == '4':
            resultado = divisiones()

        if opcion == '5':
            resultado = potenciacion()

        print("El resultado es: ", resultado)

calculadora_()