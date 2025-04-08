import matplotlib.pyplot as plt
import pandas as pd 

excel = pd.read_csv("Spotify_dataset.csv")
table_popular = excel.track_popularity
table_time = excel.time_signature
table_year = excel.track_album_release_year
table_danceability = excel.danceability

def q1():
    fig, ax = plt.subplots(figsize = (8, 6), layout="constrained", facecolor = "pink")
    ax.bar(table_year, table_danceability)
    plt.title("Does Danceability increase over the years?")
    plt.xlabel("Release Year")
    plt.ylabel("Danceability")

def q2():
    fig, ax = plt.subplots(figsize = (8, 6), layout="constrained", facecolor = "pink")
    ax.bar(table_time, table_popular)
    plt.title("Are certain time signatures more prominent in popular songs?")
    plt.xlabel("Time Signature")
    plt.ylabel("Popularity")

while True:
    # User Interaction
    print("Menu")
    print("1. Does danceability increase over the year?")
    print("2. Are certain time signatures more prominent in popular songs?")
    print("3. View both")
    print("Q. Quit Program")
    userInput = input("Enter the menu number for the visuallisation/records you want to view\nInput: ")
    
    match userInput:
        case '1':
            print("You have selected:\nDoes Danceability increase over the years?")
            q1()
            plt.show()
        case '2':
            print("You have selected:\nAre certain time signatures more prominent in popular songs?")
            q2()
            plt.show()
        case '3':
            print("You have selected:\nView Both")
            q1()
            q2()
            plt.show()
        case 'Q':
            print("Quit Program")
            break
        case _:
            print("Invalid Input. Try again")