import matplotlib.pyplot as plt
import pandas as pd
excel = pd.read_csv("M:\\CSW\\2025-4216COMP-Team10\\Spotify_dataset.csv")
def question1():
    column1 = excel.track_popularity
    column2 = excel.playlist_genre
    fig, ax = plt.subplots(figsize=(8, 6), layout="constrained", facecolor="pink")
    ax.barh(column2, column1)
    plt.title("based off the Genres most popular Song, which Genre is the most Popular?")
    plt.ylabel("Genre")
    plt.xlabel("Popularity")
    plt.show()
question1()