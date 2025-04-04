import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

excel = pd.read_csv("Spotify_dataset.csv")
def question1():
    column1 = excel.playlist_genre
    column2 = excel.track_popularity
    fig, ax = plt.subplots(figsize=(8, 6), layout="constrained", facecolor="pink")
    ax.barh(column1, column2)
    plt.title("based off the Genres most popular Song, which Genre is the most Popular?")
    plt.ylabel("Genre")
    plt.xlabel("Popularity")

def question2():
    column1 = excel.valence
    column2 = excel.danceability
    fig, ax = plt.subplots(figsize=(8, 6), layout="constrained", facecolor="pink")
    ax.scatter(column1, column2, alpha=0.5)
    plt.title("Does an increase in Valence equate to an increase in Danceability?")
    a, b = np.polyfit(excel.valence, excel.danceability, deg=1)
    plt.plot(excel.valence, a * excel.valence + b, color="red")
    plt.xlabel("Valence")
    plt.ylabel("Danceability")
    
while True:
    print("\nEnter the menu number for the visuallisation/records you want to view:\n")
    print("1) based off the Genres most popular Song, which Genre is the most Popular?")
    print("2) Does an icrease in valence equate to an increase in dancability?")
    print("3) View Both")
    print("Q) Exit Section\n\n")
    userInput = input("Input: ")
    match userInput:
        case '1':
            question1()
            plt.show()
        case '2':
            question2()
            plt.show()
        case '3':
            question1()
            question2()
            plt.show()
        case 'Q':
            print("Exit Section!")
            break
        case _:
            print("invalid input")

