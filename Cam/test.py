import matplotlib.pyplot as plt
import pandas as pd 

excel = pd.read_csv("M:\\2025-4216COMP-Team10\\2025-4216COMP-Team10\\Spotify_dataset.csv")


def q1():
    table_release_year = excel.track_album_release_year
    table_popularity = excel.track_popularity
    fig, ax = plt.subplots(figsize=(8, 6), facecolor="pink", layout="constrained")
    ax.bar(table_release_year, table_popularity)
    plt.title("Has music popularity increased over time?")
    plt.ylabel('Popularity')
    plt.xlabel('Release Year')
def q2():
    table_release_year = excel.track_album_release_year
    table_tempo = excel.tempo
    fig, ax = plt.subplots(figsize=(8, 6), facecolor="pink", layout="constrained")
    ax.bar(table_release_year, table_tempo)
    plt.title("Has music tempo increased over time?")
    plt.ylabel('Tempo')
    plt.xlabel('Release Year')
while True:
    # User Interaction
    print("Choose Question")
    print("1. Has music popularity increased over time?")
    print("2. Has music tempo increased over time?")

    print("Q. Quit Program")
    userInput = input("Enter the menu number for the visuallisation/records you want to view\nInput: ")
    
    match userInput:
        case '1':
            print("You have chosen 1. Has music popularity increased over time?")
            q1()
            plt.show()
        case '2':
            print("You have chosen 2. Has music tempo increased over time?")
            q2()
            plt.show()
        case 'Q':
            print("Quit Program")
            break
        case _:
            print("Invalid Input. Try again")