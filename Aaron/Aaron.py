import matplotlib.pyplot as plt
import pandas as pd 

excel = pd.read_csv("Spotify_dataset.csv")
table_popular = excel.track_popularity
table_time = excel.time_signature
table_year = excel.track_album_release_year
table_danceability = excel.danceability

def yearDance():
    fig, ax = plt.subplots(figsize = (8, 6), layout="constrained", facecolor = "pink")
    ax.bar(table_year, table_danceability)
    plt.title("Does Danceability increase over the years?")
    plt.xlabel("Release Year")
    plt.ylabel("Danceability")

def timePop():
    fig, ax = plt.subplots(figsize = (8, 6), layout="constrained", facecolor = "pink")
    ax.barh(table_time, table_popular)
    plt.title("Are certain time signatures more prominent in popular songs?")
    plt.xlabel("Time Signature")
    plt.ylabel("Popularity")

while True:
    print("Menu")
    print("1. Does danceability increase over the year?")
    print("2. Are certain time signatures more prominent in popular songs?")
    print("3. View both")
    print("Q. Return to Main Menu")
    userInput = input("Enter the menu number for the visuallisation/records you want to view\nInput: ")
    
    match userInput:
        case '1':
            print("You have selected:\nDoes Danceability increase over the years?")
            yearDance()
            plt.show()
        case '2':
            print("You have selected:\nAre certain time signatures more prominent in popular songs?")
            timePop()
            plt.show()
        case '3':
            print("You have selected:\nView Both")
            yearDance()
            timePop()
            plt.show()
        case 'Q':
            print("Return to Main Menu")
            break
        case _:
            print("Invalid Input. Try again")