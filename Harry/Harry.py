import matplotlib.pyplot as plt
import pandas as pd

#import the dataset
data = pd.read_csv("Spotify_dataset.csv")
#while loop to keep the code running for as long as the user wants
while True:
#Display another menu for the user so they can decide what they want to see
    print("which question would you like?")
    print("1. Does energy have any correlation with loudness?")
    print("2. Which genre has the most amount of lyrics?")
    print("Q. Return to previous menu.")
    Ans = input("Answer: ")


    def enLoud():
        Energy = data.energy
        Loudness = data.loudness
        
        fig, ax = plt.subplots(figsize = (8, 6), layout="constrained", facecolor = "pink")
        ax.scatter(Energy, Loudness)
        ax.set(xlabel="Energy", ylabel="Loudness")
        plt.title("Does energy have any correlation with loudness?")

        plt.show()

    def genSpeech():
        genre = data.playlist_genre
        speechiness = data.speechiness

        fig, ax = plt.subplots(figsize = (8, 6), layout="constrained", facecolor = "pink")
        ax.barh(genre, speechiness)
        ax.set(xlabel="Genre", ylabel="Speechiness")
        plt.title("Which genre has the most amount of lyrics?")

        plt.show()


    match Ans:
        case '1':
            enLoud()
            print("You have selected does energy have any correlation with loudness?")
        case '2':
            genSpeech()
            print("You have selected Which genre has the most amount of lyrics?")
        case 'Q':
            print("You have selected to return to the main menu.")
            break
        case _:
            print("enter something appropriate.")
