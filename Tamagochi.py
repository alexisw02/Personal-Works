#Excercise #¿?
#Make a Tamagochi

def Tamagochi_():
    
    print("Welcome to Tamagochi")
    
    hunger = 100
    energy = 100
    tamagochi_life = True
    
    while tamagochi_life == True:
        play = False
        eat = False
        sleep = False
        
        print("\nState............[1]")
        print("Play.............[2]")
        print("Eat..............[3]")
        print("Sleep............[4]")
        print("Exit.............[5]")
        
        option = input("\nChoose what you want: ")
        
        if option == '1':
            print("Hunger: ", hunger)
            print("Energy: ", energy)
        
        elif option == '2':
            play = True
            
            while play == True:
                
                print("\nPLAY:")
                print("What do you want to play?")
                print("Football soccer............[1]")
                print("     -20 hunger")
                print("     -15 energy")
                print("\nCard game..................[2]")
                print("     -10 hunger")
                print("      -5 energy")
                print("\nReturn.....................[3]")
                
                if energy == 0 or hunger == 0:
                    print("\nTamagochi is dead.")
                    tamagochi_life = False
                    break
                
                option = input("\nChoose what you want: ")
                
                if option == '1':
                    hunger -= 20
                    energy -= 15
                    
                elif option == '2':
                    hunger -= 10
                    energy -= 5                

                elif option == '3':
                    play = False

        elif option == '3':
            eat = True

            while eat == True:
                
                print("EAT:")
                print("What do you want to eat?")
                print("\nCake.......................[1]")
                print("     +10 hunger")
                print("     +20 energy")
                print("\nPotato chips...............[2]")
                print("      +5 hunger")
                print("      +5 energy")
                print("\nMeat.......................[3]")
                print("     +20 hunger")
                print("     +15 energy")
                print("\nChocolate..................[4]")
                print("      +5 hunger")
                print("     +15 energy")
                print("\nCandy......................[5]")
                print("      +3 hunger")
                print("      +5 energy")
                print("\nReturn.....................[6]")
                
                option = input("\nChoose what you want: ")
                
                if option == '1':
                    if hunger <= 90 and energy < 100:
                        hunger += 10
                        energy += 20
                    
                    else:
                        #print("\nTamagochi can't eat more Cake. Try with another option")
                        hunger = 100
                        energy = 100
                
                elif option == '2':
                    if hunger <= 95 and energy <= 95:
                        hunger += 5
                        energy += 5
                    
                    else:
                        #print("\nTamagochi can't eat more Potato Chips. Try with another option")
                        hunger = 100
                        energy = 100
                
                elif option == '3':
                    if hunger <= 80 and energy <= 85:
                        hunger += 20
                        energy += 15
                    
                    else:
                        #print("\nTamagochi can't eat more Meat. Try with another option")
                        hunger = 100
                        energy = 100
                
                elif option == '4':
                    if hunger <= 95 and energy <= 85:
                        hunger += 5
                        energy += 15
                    
                    else:
                        #print("\nTamagochi can't eat more Chocolate. Try with another option")
                        hunger = 100
                        energy = 100
                
                elif option == '5':
                    if hunger <= 97 and energy <= 95:
                        hunger += 3
                        energy += 5
                    
                    else:
                        #print("\nTamagochi can't eat more Candy. Try with another option")
                        hunger = 100
                        energy = 100
                
                elif option == '6':
                    eat = False

        elif option == '4':
            sleep = True
            
            while sleep == True:
                
                print("SLEEP:")
                print("\nSleep all day...........[1]")
                print("     +30 energy")
                print("\nTake a nap..............[2]")
                print("     +15 energy")
                print("\nReturn..................[3]")
                
                option = input("\nWhat do you want to sleep? ")
                
                if option == '1':
                    if energy <= 70:
                        energy += 30
                    
                    else:
                        energy = 100
                
                elif option == '2':
                    if energy <= 85:
                        energy += 15
                    
                    else:
                        energy = 100
                
                elif option == '3':
                    sleep = False
        
        elif option == '5':
            break
Tamagochi_()

