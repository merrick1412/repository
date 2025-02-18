
/* Name: Merrick Moncure
Date: 2/27/2022
Section:7
Assignment: Playing With Numbers Program
Due Date: 2/27/2022
About this project: Write a program to find cousin primes under a number and check if its perfect
Assumptions: N/A
All work below was performed by Merrick Moncure */
#include <iostream>
#include <iomanip>
const int NUM_AVENGERS = 173; //constant for # of avengers
int getValidNumAppearances(); //Prototyping functions
int getValidAvenger();
void displayNumAppearances(int numAppearances[NUM_AVENGERS]);
void ChangeANumAppearances(int numAppearances[NUM_AVENGERS]);
void displayMaxNumAppearances(int numAppearances[NUM_AVENGERS]);

using namespace std;

int main()
{
    char switchChoice; //character data for choosing the switch
    int numAppearances[NUM_AVENGERS]= //array
    {
        1269, 1165, 3068, 2089, 2402,
        612, 3458, 1456, 769, 1214,
        115, 741, 780, 1036, 482,
        1112, 160, 1886, 332, 557,
        197, 106, 692, 109, 100,
        132, 108, 100, 156, 254,
        935, 576, 141, 355, 933,
        348, 206, 533, 374, 2,
        2305, 83, 402, 352, 565,
        112, 218, 149, 168, 1561,
        217, 158, 86, 41, 68,
        70, 61, 2125, 1761, 293,
        36, 22, 31, 34, 33,
        4, 47, 7, 3, 16,
        575, 58, 237, 4333, 126,
        158, 355, 517, 202, 31,
        28, 50, 27, 18, 302,
        330, 101, 43, 126, 24,
        886, 159, 3130, 241, 67,
        23, 103, 123, 110, 160,
        132, 121, 59, 629, 1324,
        236, 663, 525, 205, 108,
        359, 299, 333, 88, 369,
        380, 545, 6, 126, 417,
        31, 310, 40, 26, 63,
        2, 73, 22, 153, 73,
        59, 66, 43, 55, 108,
        64, 62, 94, 18, 81,
        1598, 1375, 746, 561, 592,
        679, 491, 65, 55, 44,
        65, 877, 176, 24, 25,
        35, 44, 78, 22, 77,
        115, 77, 69, 173, 75,
        12, 14, 13, 198, 29,
        45, 49, 35
    };

    while (true) //loop for menu selection
    {
        cout<<"Welcome to the Avengers Program!"<<endl;
        cout<<"1) Display the number of appearances"<<endl<<"2) Change the number of appearances for an Avenger"<<endl
        <<"3) Display the max number of appearances"<<endl<<"4) Quit"<<endl;
        cout<<"Select an option (1..4)..";
        cin>>switchChoice;

        switch (switchChoice) //switch loop for menu selection
        {
            case '1' :
                displayNumAppearances(numAppearances); //calls a function to display the array
                break;

            case '2' :
                ChangeANumAppearances(numAppearances); //calls a function to change an element in the array
                break;

            case '3' :
                displayMaxNumAppearances(numAppearances); //calls a function to display the largest element in the array
                break;

            case '4' : //quit option
                break;

            default : //invalid selection
                cout<<"invalid choice. Please choose again"<<endl;
        }
        if (switchChoice == '4') //quit option
            break;

    }
}

int getValidNumAppearances() //validates input for appearances
{
    int appearances;
    cin>>appearances;
    while (appearances < 1) //validation loop for the appearances being greater than 0
    {
        cout<<"Please enter a valid number of appearances greater than 0"<<endl;
        cin>>appearances;
    }
    return appearances; //returns validated value
}

int getValidAvenger() //validates avenger selection
{

    int avengerNum; //variable to check the avenger input

     while (avengerNum < 1 || avengerNum > NUM_AVENGERS)
    {
        cout<<"Please enter a valid avenger greater than 0 and less than 173."<<endl;
        cin>>avengerNum;
    }
    return avengerNum;

}

void displayNumAppearances(int numAppearances[NUM_AVENGERS]) //displays the array
{

    int endlcounter = 1; //counter for ending the line every 5 elements

    cout<<"Display Number Appearances"<<endl;
    for (int i = 0; i<NUM_AVENGERS; i++,endlcounter++)
    {
        cout<< right << setw(4) <<numAppearances[i]<<" "; //formatting
        if (endlcounter == 5)
        {
            cout << endl;
            endlcounter = 0; //linebreaks every 5 elements
        }
    }
    cout<<endl; //line break at the end
}

void ChangeANumAppearances(int numAppearances[NUM_AVENGERS]) //changes an array element
{
    int avengNum;
    int avengAppear;

    cout << "Change A Number of Appearances"<<endl;
    cout << "Please enter in the number of the Avenger..."<<endl;
    avengNum = getValidAvenger(); //input validation function

    cout << "Please enter in the Number of Appearances..."<<endl;
    avengAppear = getValidNumAppearances();
    numAppearances[(avengNum-1)] = avengAppear; //input validation function that accounts for n-1 element
}

void displayMaxNumAppearances(int numAppearances[NUM_AVENGERS]) //displays largest element
{
    int i;
    int largestNum;

    largestNum = numAppearances[0]; //sets largest to the first one then replaces it with any larger ones found

    for (i = 1; i < NUM_AVENGERS; i++ )
    {
        if (numAppearances[i] > largestNum)
        largestNum = numAppearances[i];
    }
    cout<<"The max number of appearances of the Avengers was "<<largestNum<<endl;
}
