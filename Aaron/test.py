import matplotlib.pyplot as plt
import pandas as pd 

excel = pd.read_csv("Spotify_dataset.csv")
table_energy = excel.energy
table_tempo = excel.tempo
table_popular = excel.track_popularity
table_time = excel.time_signature
table_year = excel.

def energy_tempo():
    fig, ax = plt.subplots(figsize = (20, 20), facecolor = "pink")
    ax.barh(table_tempo, table_energy)
    plt.xlabel("Energy")
    plt.ylabel("Tempo")

def time_pop():
    fig, ax = plt.subplots(figsize = (20,20), facecolor = "pink")
    ax.barh(table_time, table_popular)
    plt.xlabel("Popularity")
    plt.ylabel("Time Signature")

while True:
    # User Interaction
    print("Menu")
    print("1. Does tempo affect the energy of a song?")
    print("2. Does the time signature affect how popular the song is?")
    print("3. View both")
    print("Q. Quit Program")
    userInput = input("Enter the menu number for the visuallisation/records you want to view\nInput: ")
    
    match userInput:
        case '1':
            print("You have selected:\nDoes Tempo affect the Energy of a song?")
            energy_tempo()
            plt.show()
        case '2':
            print("You have selected:\nDoes Time Signatures affect the Popularity of a song?")
            time_pop()
            plt.show()
        case '3':
            print("You have selected:\nView Both")
            energy_tempo()
            time_pop()
            plt.show()
        case 'Q':
            print("Quit Program")
            break
        case _:
            print("Invalid Input. Try again")