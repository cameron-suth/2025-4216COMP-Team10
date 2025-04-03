import matplotlib.pyplot as plt
import pandas as pd
excel = pd.read_csv("Spotify_dataset.csv")
def question1():
    column1 = excel.playlist_genre
    column2 = excel.track_popularity
    fig, ax = plt.subplots(figsize=(8, 6), layout="constrained", facecolor="pink")
    ax.barh(column1, column2)
    plt.title("based off the Genres most popular Song, which Genre is the most Popular?")
    plt.ylabel("Genre")
    plt.xlabel("Popularity")

#question1()
def question2():
    column1 = excel.valence
    column2 = excel.danceability
    fig, ax = plt.subplots(figsize=(8, 6), layout="constrained", facecolor="pink")
    ax.scatter(column1, column2)
    plt.title("Does an icrease in valence equate to an increase in dancability?")
    #ax.plot([0,1],[0,1], color="Red") 
    plt.xlabel("Valence")
    plt.ylabel("Danceability")
while True:
    userInput = input("\nEnter the menu number for the visuallisation/records you want to view\n\n1) based off the Genres most popular Song, which Genre is the most Popular?\n2) Does an icrease in valence equate to an increase in dancability?\n3) View Both\nQ) Exit Section\n\nInput: ")
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

