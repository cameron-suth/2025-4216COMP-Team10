#Imports
#########################################################
#This is for plotting
import matplotlib.pyplot as plt
#This handles the data set
import pandas as pd
#handles large data arrays
import numpy as np
#########################################################
#This imports the dataset, so python knows what we are reading from
excel = pd.read_csv("Spotify_dataset.csv")

#Function for Question 1
def acousticPop():
    table_popularity = excel.track_popularity
    table_acousticness = excel.acousticness
    #Creating the Scatter graph, and setting the size and colour
    #Constrained ensures that the graph includes lables and a title
    fig, ax = plt.subplots(figsize=(8, 6), layout="constrained", facecolor="pink")
    #This plots acousticness along the X axis and Popularity on the Y. The s is the size of the points on the graph
    ax.scatter(table_acousticness, table_popularity, s=30)
    #Labels and Title
    plt.xlabel("Acousticness")
    plt.ylabel("Popularity")
    plt.title("Does Acousticness Impact Song Popularity?")
    #Show the graph
    plt.show()

#Function for Question 2
def speechyPop():
    table_speechiness = excel.speechiness
    table_popularity = excel.track_popularity
    #Creating the Scatter graph, and setting the size and colour
    #Constrained ensures that the graph includes lables and a title
    fig, ax = plt.subplots(figsize=(8, 6), layout="constrained", facecolor="pink")
    #This plots acousticness along the X axis and Popularity on the Y. The s is the size of the points on the graph
    ax.scatter(table_speechiness, table_popularity, s=30)
    #Lables and Title
    plt.xlabel("Speechiness")
    plt.ylabel("Popularity")
    plt.title("Does Speechiness Increase Song Popularity?")
    #Showing the Graph
    plt.show()

#########################################################
#Main

#This creates a variable to be inputted by the user
userAns = ""
#This creates a loop that will run through the menu until an option is chosen
while userAns !="3":
    print("1: Does the song being acoustic impact the popularity of the song?")
    print("2: Does speechiness increase song popularity?")
    print("3: Exit the program")
    #This prompts the user to input their choice and store it as the variable created earlier
    userAns = input("Please enter what you would like to do: ")

    #This calls on the acousticPop function for the first question
    if userAns == "1":
        acousticPop()
        input("please press enter to continue")
    
    #This calls upon the speechyPop function for the second question
    elif userAns == "2":
        speechyPop()
        input("please press enter to continue")

    #This exits the program
    elif userAns == "3":
        print("Exiting the program!")
        break

    #This is if the user does not input an approptiate answer
    else:
        print("Please enter a valid response.")
