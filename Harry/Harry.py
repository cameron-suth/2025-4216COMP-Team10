import matplotlib.pyplot as plt
import pandas as pd

#import the dataset
data = pd.read_csv("Spotify_dataset.csv")
#while loop to keep the code running for as long as the user wants
while True:

    print("which question would you like?")
    print("1. Which genre is the most popular?")
    print("2. Which artist has released the most popular songs?")
    print("Q. Return to previous menu.")
    Ans = input("Answer: ")

#oldSongs is a function that would record all the dates, artist names,song names and popularity of each song into an array
#so that it can reference it when needed to make the graph by sowing the oldest songs and their respective popularity.

    def oldSongs():
        playlistGenre = data.playlist_genre
        popularity = data.track_popularity
        releaseYear = data.track_album_release_year
        
        fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
        ax.stem(playlistGenre, popularity, releaseYear)
        ax.set(xlabel="Playlsit Genre", ylabel="popularity", zlabel="release year")


        plt.show()



    def artPop():
        artist = data.track_artist
        popularity = data.track_popularity

    match Ans:
        case '1':
            oldSongs()
        case '2':
            artPop()
        case 'Q':
            break
        case _:
            print("enter something appropriate.")
