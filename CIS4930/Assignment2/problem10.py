import random


def addMovie(watchlist):
    watchlist.append(input("Enter the movie title: "))

def removeMovie(watchlist):
    watchlist.remove(input("Enter the movie title: "))

def displayWatchlist(watchlist):
    print (watchlist)

def checkMovie(watchlist):
    check = input("Enter the movie title: ")
    if check in watchlist:
        print("The movie title is in the watchlist")
    else:
        print("The movie title is not in the watchlist")

def watchlistSize(watchlist):
    print("The total number of movies in the watchlist is " + str(len(watchlist)))

def clearWatchlist(watchlist):
    watchlist.clear()
    print("watchlist cleared")

def sortWatchlist(watchlist):
    watchlist.sort()
    print("sorted watchlist")

def reverseWatchlist(watchlist):
    watchlist.reverse()
    print("reversed watchlist")

def randomWatchlist(watchlist):
    print(random.choice(watchlist))
def menu():
    print("\nMenu:")
    print("1. Add a movie")
    print("2. Remove a movie")
    print("3. Display watchlist")
    print("4. Check if a movie is in the watchlist")
    print("5. Get the total number of movies in the watchlist")
    print("6. Clear the watchlist")
    print("7. Sort the watchlist")
    print("8. Reverse the watchlist")
    print("9. Pick a random movie from the watchlist")
    print("10. Exit")

def main():
    watchlist = []
    while True:
        menu()
        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            addMovie(watchlist)
        elif choice == '2':
            removeMovie(watchlist)
        elif choice == '3':
            displayWatchlist(watchlist)
        elif choice == '4':
            checkMovie(watchlist)
        elif choice == '5':
            watchlistSize(watchlist)
        elif choice == '6':
            clearWatchlist(watchlist)
        elif choice == '7':
            sortWatchlist(watchlist)
        elif choice == '8':
            reverseWatchlist(watchlist)
        elif choice == '9':
            randomWatchlist(watchlist)
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()