import playerM
import os

def actions_menu():
    actions = ["Explore", "Travel", "Examine", "Talk"]

    for index, element in enumerate(actions, 1):
        print(index, "\b.", element)

    try:
        userInput = int(input("\nWhich action? "))
    except ValueError:
        while True:
            try:
                userInput = int(input("\nInvalid choice. Which action? "))
                break
            except ValueError:
                pass

    while userInput - 1 not in range(len(actions)):
        try:
            userInput = int(input("\nInvalid choice. Which action? "))
        except ValueError:
            while True:
                try:
                    userInput = int(input("\nInvalid choice. Which action? "))
                    break
                except ValueError:
                    pass
                
    if userInput == 1:
        explore_menu()
    elif userInput == 2:
        travel_menu()
    elif userInput == 3:
        examine_menu()
    elif userInput == 4:
        talk_menu()
        
def explore_menu():
    print("\nThis feature is not finished yet.\n")
    actions_menu()

def travel_menu():
    #makes a new line
    print()
    #Prints the travel destinations available from player's
    #current location into a numbered list
    
    for index, element in enumerate(playerM.Player.location.subloc, 1):
        print(index, "\b.", element.name)

    try:
        userInput = int(input("\nWhich location? "))
    #if user puts in a string, this catches the error and
    #returns input validation loop
    except ValueError:
        while True:
            try:
                userInput = int(input("\nInvalid choice. Which location? "))
                break
            except ValueError:
                pass
    #if user inputs a number not within range of the length
    #of the Options list it returns this input validation
    while userInput - 1 not in range(len(playerM.Player.location.subloc)):
        try:
            userInput = int(input("\nInvalid choice. Which location? "))
        except ValueError:
            while True:
                try:
                    userInput = int(input("\nInvalid choice. Which location? "))
                    break
                except ValueError:
                    pass

    userChoice = playerM.Player.location.subloc[userInput - 1]
    playerM.Player.location = userChoice
    os.system('cls')
    print(f"You traveled to {userChoice.name}.\n")
    actions_menu()

def examine_menu():
    #checks to see if there are any objects in current location
    if not playerM.Player.location.objekt:
        os.system('cls')
        print("There is nothing here.\n")
        actions_menu()
        
    else:
        #makes a new line
        print()
        #Prints the objekts available from player's
        #current location into a numbered list
        for index, element in enumerate(playerM.Player.location.objekt, 1):
            print(index, "\b.", element.name)

        try:
            userInput = int(input("\nExamine what? "))
        #if user puts in a string, this catches the error and
        #returns input validation loop
        except ValueError:
            while True:
                try:
                    userInput = int(input("\nInvalid choice. Examine what? "))
                    break
                except ValueError:
                    pass
        #if user inputs a object not within range of the length
        #of the Options list it returns this input validation
        while userInput - 1 not in range(len(playerM.Player.location.subloc)):
            try:
                userInput = int(input("\nInvalid choice. Examine what? "))
            except ValueError:
                while True:
                    try:
                        userInput = int(input("\nInvalid choice. Examine what? "))
                        break
                    except ValueError:
                        pass
                    
        userChoice = playerM.Player.location.objekt[userInput - 1]
        os.system('cls')
        print(f"{userChoice.descript}\n")
        actions_menu()
        
def talk_menu():
    print("\nThis feature is not finished yet.\n")
    actions_menu()
