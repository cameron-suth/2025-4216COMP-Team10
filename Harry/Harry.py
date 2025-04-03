import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("C:\Users\csmhkers\OneDrive - Liverpool John Moores University\4216 COMP\python\2025-4216COMP-Team10\Spotify_dataset.csv")
while True:

    print("which question would you like?")
    print("1. Are some oldersongs still popular today?")
    print("2. Are certain atists more prone to releasing more popular songs?")
    print("Q. Return to previous menu.")
    Ans = input("Answer: ")

    match Ans:
        case '1':
            oldSongs()
        case '2':
            artPop()
        case 'Q':
            break
        case _:
            print("enter something appropriate.")

    def oldSongs():
        songsDate = [[],[],[],[]]
        for x in data:
            T[x] = [data.get("artist_name")]


    #def artPop():
    #    data.