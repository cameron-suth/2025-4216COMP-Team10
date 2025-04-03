import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#import the dataset
data = pd.read_csv("C:\\Users\\csmhkers\\OneDrive - Liverpool John Moores University\\4216 COMP\\python\\2025-4216COMP-Team10\\Spotify_dataset.csv")
#while loop to keep the code running for as long as the user wants
while True:

    print("which question would you like?")
    print("1. Are some oldersongs still popular today?")
    print("2. Which artist has released the most popular songs?")
    print("Q. Return to previous menu.")
    Ans = input("Answer: ")
#oldSongs is a function that would record all the dates, artist names,song names and popularity of each song into an array
#so that it can reference it when needed to make the graph by sowing the oldest songs and their respective popularity.
    def oldSongs():
        Year = input("What year would you like to search before: ")
        songsInfo = np.array([[]])
#        for column in data:
        songsInfo[0,0] = 12


    #def artPop():
    #    data.

    match Ans:
        case '1':
            oldSongs()
        case '2':
            artPop()
        case 'Q':
            break
        case _:
            print("enter something appropriate.")
