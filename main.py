`# Imports
import pandas as pd
import matplotlib.pyplot as plt

while True:
    # User Interaction
    print("Menu")
    print("1. Cam")
    print("2. Aaron")
    print("3. Harry")
    print("4. Reece")
    print("5. Josh")
    print("6. Josh A")
    print("Q. Quit Program")
    userInput = input("Enter the menu number for the visuallisation/records you want to view\nInput: ")
    
    match userInput:
        case '1':
            print("You have chosen Cam")
            from Cam import cam
        case '2':
            print("You have chosen Aaron")
            from Aaron import Aaron
        case '3':
            print("You have chosen Harry")
            from Harry import Harry
        case '4':
            print("You have chosen Reece")
            from Reece import reece
        case '5':
            print("You have chosen Josh")
            from JoshM import josh
        case '6':
            print("You have chosen Josh A")
            from JoshA import joshA
        case 'Q':
            print("Quit Program")
            break
        case _:
            print("Invalid Input. Try again")
            
