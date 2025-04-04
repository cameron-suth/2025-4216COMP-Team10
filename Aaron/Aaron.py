import matplotlib.pyplot as plt
import pandas as pd 

excel = pd.read_csv("Spotify_dataset.csv")
table_popular = excel.track_popularity
table_time = excel.time_signature
table_year = excel.track_album_release_year
table_danceability = excel.danceability

def year_dance():
    fig, ax = plt.subplots(figsize = (8, 6), layout="constrained", facecolor = "pink")
    ax.bar(table_year, table_danceability)
    plt.xlabel("Release Year")
    plt.ylabel("Danceability")

def time_pop():
    fig, ax = plt.subplots(figsize = (8, 6), layout="constrained", facecolor = "pink")
    ax.bar(table_time, table_popular)
    plt.xlabel("Time Signature")
    plt.ylabel("Popularity")

while True:
    # User Interaction
    print("Menu")
    print("1. Does danceability increase over the year?")
    print("2. Does the time signature affect how popular the song is?")
    print("3. View both")
    print("Q. Quit Program")
    userInput = input("Enter the menu number for the visuallisation/records you want to view\nInput: ")
    
    match userInput:
        case '1':
            print("You have selected:\nDoes Danceability increase over the years?")
            year_dance()
            plt.show()
        case '2':
            print("You have selected:\nDoes Time Signatures affect the Popularity of a song?")
            time_pop()
            plt.show()
        case '3':
            print("You have selected:\nView Both")
            year_dance()
            time_pop()
            plt.show()
        case 'Q':
            print("Quit Program")
            break
        case _:
            print("Invalid Input. Try again")