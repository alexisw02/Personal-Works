def Tamagochi_():
    
    print("Welcome to Tamagochi")
    
    menu = True
    hunger = 100
    energy = 100
    
    while menu == True:
        play = False
        
        print("\nState............[1]")
        print("Play.............[2]")
        print("Eat..............[3]")
        print("Sleep............[4]")
        print("Exit.............[5]")
        
        option = input("\nChoose what you want: ")
        
        if option == '1':
            print("Health: ", hunger)
            print("Energy: ", energy)
        
        elif option == '2':
            play = True
            
            while play == True:
                
                print("\nWhat do you want to play?")
                print("Football soccer............[1]")
                print("Card game..................[2]")
                print("Return.....................[3]")
                
                option = input("Choose what you want: ")
                
                if option == '3':
                    play = False
                
                elif option == '1':
                    hunger -= 5
                    energy -= 15
                    
                
                elif option == '2':
                    hunger -= 10
                    energy -= 5
            
Tamagochi_()