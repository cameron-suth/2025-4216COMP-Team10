import matplotlib.pyplot as plt
import pandas as pd 

excel = pd.read_csv("Spotify_dataset.csv") #telling python what we are reading from
table_energy = excel.energy #defining data set as a variable
table_concert = excel.liveness
table_length = excel.duration_ms
choice = ""

font1 = {'family':'serif','color':'black','size':20} #making a font style 
font2 = {'family':'serif','color':'black','size':12}

# - 

# Functions for the creation of the graphs

def energylive():
    fig, ax = plt.subplots(figsize=(8, 6)) #sets the size of the generated screen
    ax.scatter(table_energy, table_concert, s=20) #scatters the variables selected as a size defined by s
    plt.title("Is a higher energy song more likely to be played at a live event?", fontdict = font1) 
    plt.ylabel('Liveness', fontdict = font2)
    plt.xlabel('Energy', fontdict = font2)
    plt.show()

def longlive():
    fig, ax = plt.subplots(figsize=(8, 6)) #sets the size of the generated screen
    ax.scatter(table_energy, table_length, s=20) #scatters the variables selected as a size defined by s
    plt.title("Does a longer song affect the chance it being played live?", fontdict = font1)
    plt.ylabel('Liveness', fontdict = font2)
    plt.xlabel('Duration', fontdict = font2)
    plt.show()

# - 

# Terminal View

while True: 
    print("")
    print("What question would you like?")
    print("1. Is a higher energy song more likely to be played at a live event?")
    print("2. Does a longer song affect the chance it being played live?")
    print("Q. Quit program.")
    ans= input("Enter menu number here: ")

    match ans:
        case '1':
            print("You have selected: Is a higher energy song more likely to be played at a live event?")
            energylive() #calls function
        case '2':
            print("You have selected: Does a longer song affect the chance it being played live?")
            longlive() #calls function
        case 'Q':
            print("Quitting program now..")
            break #terminates program
        case _:
            print("Invalid input. Please try again.")

# - 


