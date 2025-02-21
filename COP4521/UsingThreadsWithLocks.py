"""
Name:Merrick Moncure
Date: 2/2/25
Assignmnent: Module 4: Using Threads with Locks
Apply parallel and distributed computing to computational problems and analyze the scalability and efficiency of the solutions.
Assumptions: file name is votes.txt
All work below was performed by Merrick Moncure
"""
import threading
import random
lock = threading.Lock()

countKisses = 0
countMMs = 0
def clearFile(file):
    with open(file, 'w') as file: #empties file
        pass

def appendToFile(filename: str, num: int):
    with lock:        #thread safe file writing
        with open(filename, 'a') as file:
            file.write(f"{num}\n")


def Voter():
    global countKisses, countMMs
    for i in range(5):
        rand = random.choice([1,2])
        appendToFile("votes.txt", rand) #write to file

        with lock:  #makes sure threads update safely
            print(f"Vote: {rand}")

    VoteTally()

def VoteTally():
    global countKisses, countMMs
    with lock: #thread safe reading and writing
        try:
            with open('votes.txt', 'r') as file:
                for line in file:
                    vote = line.strip()
                    if vote == "1":
                        countKisses += 1
                    elif vote == "2":
                        countMMs += 1 #writes the number to the file
            print(f"Current votes for kisses: {countKisses}")
            print(f"Current votes for M&Ms: {countMMs}") #current tally

            clearFile("votes.txt")
        except FileNotFoundError:
            print("No votes file")

def main():
    clearFile("votes.txt") #start w empty file
    #25 voter threads
    voter_threads = []
    for i in range(25):
        thread = threading.Thread(target=Voter)
        voter_threads.append(thread)
        thread.start()
    #wait for voter threads to finish
    for thread in voter_threads:
        thread.join()
        # results
    print(f"Total votes for kisses: {countKisses}")
    print(f"Total votes for M&Ms: {countMMs}")

if __name__ == "__main__":
    main()