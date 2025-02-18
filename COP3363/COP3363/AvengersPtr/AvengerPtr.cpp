
/* Name: Merrick Moncure
Date: 3/27/2022
Section:7
Assignment: Avengers - Number of Appearances Program Part 2
Due Date: 3/27/2022
About this project: Write a program that can take an array of avenger appearances and calculate the maximum # of
appearances, change a number of appearances, display all the appearances, and add the cumulative total number of
appearances within ranges of numbers and sort them in ascending order
Assumptions: N/A
All work below was performed by Merrick Moncure */
#include <iostream>
#include <iomanip>

int getValidNumAppearances(); //Prototyping functions
int getValidAvenger(int *NUM_AVENGERS);
void displayNumAppearances(int *numAppearances, int *NUM_AVENGERS);
void ChangeANumAppearances(int *numAppearances, int *NUM_AVENGERS);
void displayMaxNumAppearances(int *numAppearances, int *NUM_AVENGERS);
void createCumulativeTotalEachRange(int *numAppearances,int *cumulativeTotalEachRange, int *NUM_AVENGERS);
void displaySortedTotals(int *numAppearances,int *NUM_AVENGERS);
int *AddAnotherAvenger(int *numAppearances, int &NUM_AVENGERS);

using namespace std;

int main()
{
    int NUM_AVENGERS = 173; // # of avengers
    char switchChoice; //character data for choosing the switch
      int * numAppearances = new int [NUM_AVENGERS] //array
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
        cout<< "1) Display the number of appearances"<<endl<<
        "2) Change the number of appearances for an Avenger"<<endl<<
        "3) Display the max number of appearances"<<endl<<
        "4) Create a cumulative total for each number of appearances by ranges,"" sort and display these sorted totals"
        <<endl << "5) Add another Avenger" <<endl<< "6) Quit"<<endl;
        cout<<"Select an option (1..6)..";
        cin>>switchChoice;

        switch (switchChoice) //switch loop for menu selection
        {
            case '1' :
                displayNumAppearances(numAppearances, &NUM_AVENGERS); //calls a function to display the array
                break;

            case '2' :
                ChangeANumAppearances(numAppearances, &NUM_AVENGERS); //calls a function to change an element in the array
                break;

            case '3' :
                displayMaxNumAppearances(numAppearances,&NUM_AVENGERS); //calls a function to display the largest element in the array
                break;

            case '4' :
                displaySortedTotals(numAppearances, &NUM_AVENGERS); //calls a function to display the sorted totals
                break;
            case '5' :
                numAppearances = AddAnotherAvenger(numAppearances,NUM_AVENGERS); //calls function to add another avenger
                break;

            case '6' : //quit option
                break;

            default : //invalid selection
                cout<<"invalid choice. Please choose again"<<endl;
        }
        if (switchChoice == '6') //quit option
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

int getValidAvenger(int *NUM_AVENGERS) //validates avenger selection
{

    int avengerNum; //variable to check the avenger input

     while (avengerNum < 1 || avengerNum > *NUM_AVENGERS)
    {
        cout<<"Please enter a valid avenger greater than 0 and less than 173."<<endl;
        cin>>avengerNum;
    }
    return avengerNum;

}

void displayNumAppearances(int *numAppearances, int *NUM_AVENGERS) //displays the array
{

    int endlcounter = 1; //counter for ending the line every 5 elements

    cout<<"Display Number Appearances"<<endl;
    for (int i = 0; i< *NUM_AVENGERS; i++,endlcounter++)
    {
        cout<< right << setw(4) <<*(numAppearances + i)<<" "; //formatting
        if (endlcounter == 5)
        {
            cout << endl;
            endlcounter = 0; //linebreaks every 5 elements
        }
    }
    cout<<endl; //line break at the end
}

void ChangeANumAppearances(int *numAppearances, int *NUM_AVENGERS) //changes an array element
{
    int avengNum;
    int avengAppear;

    cout << "Change A Number of Appearances"<<endl;
    cout << "Please enter in the number of the Avenger..."<<endl;
    avengNum = getValidAvenger(NUM_AVENGERS); //input validation function

    cout << "Please enter in the Number of Appearances..."<<endl;
    avengAppear = getValidNumAppearances();
    *(numAppearances + (avengNum-1)) = avengAppear; //input validation function that accounts for n-1 element
}

void displayMaxNumAppearances(int *numAppearances, int *NUM_AVENGERS) //displays largest element
{
    int i;
    int largestNum;

    largestNum = *(numAppearances); //sets largest to the first one then replaces it with any larger ones found

    for (i = 1; i < *NUM_AVENGERS; i++ )
    {
        if (*(numAppearances + i) > largestNum)
        largestNum = *(numAppearances + i);
    }
    cout<<"The max number of appearances of the Avengers was "<<largestNum<<endl;
}

void displaySortedTotals(int *numAppearances, int *NUM_AVENGERS) //function for displaying the sorted totals
{
    int minIndex, minValue;
    int RangeUpperLimitNum[6] = {750,1500,2250,3000,3750,4500}; //array for the ranges
    int cumulativeTotalEachRange[6] ={0,0,0,0,0,0}; //array for the cumulative totals
    createCumulativeTotalEachRange(numAppearances, cumulativeTotalEachRange, NUM_AVENGERS); //calls the function that puts the cumulative totals into the array

    for (int start = 0; start < 6; start++) //selection sort in ascending order
    {
        minIndex = start;
        minValue = *(cumulativeTotalEachRange + start);
        for (int index = start + 1; index < 6; index++)
        {
            if (*(cumulativeTotalEachRange + index) < minValue)
            {
                minValue = *(cumulativeTotalEachRange + index);
                minIndex = index;
            }
        }

        swap(*(cumulativeTotalEachRange + minIndex), *(cumulativeTotalEachRange + start));
        swap(*(RangeUpperLimitNum + minIndex), *(RangeUpperLimitNum + start)); //keeps the ranges assigned with the totals
    }
    cout<<right<<setw(20)<<"Upper Limit Range"
    <<right<<setw(20)<<"Number of Avengers"<<endl; //header
    for (int i = 0; i < 6; i++)
    {
        cout<<right<<setw(20)<<*(RangeUpperLimitNum + i)<<right<<setw(20)<<*(cumulativeTotalEachRange + i)<<endl; //prints the ranges and totals
    }


}

void createCumulativeTotalEachRange(int *numAppearances,int *cumulativeTotalEachRange,int *NUM_AVENGERS) //function for finding the cumulative totals
{
    int i;
    for (i = 0; i < *NUM_AVENGERS; i++) //goes through every element in the avengers array and adds 1 to the respective ranges
    {

        if (*(numAppearances + i) < 751)
        {
            *(cumulativeTotalEachRange)++;
        }

        if (*(numAppearances + i) < 1501 && *(numAppearances + i) > 750)
        {
            (*(cumulativeTotalEachRange + 1))++;
        }

        if (*(numAppearances + i) < 2251 && *(numAppearances + i) > 1500)
        {
            (*(cumulativeTotalEachRange + 2))++;
        }

        if (*(numAppearances + i) < 3001 && *(numAppearances + i) > 2250)
        {
            (*(cumulativeTotalEachRange + 3))++;
        }

        if (*(numAppearances + i) < 3751 && *(numAppearances + i) > 3000)
        {
            (*(cumulativeTotalEachRange + 4))++;
        }

        if (*(numAppearances + i) < 4501 && *(numAppearances + i) > 3750)
        {
            (*(cumulativeTotalEachRange + 5))++;
        }
    }
}
int *AddAnotherAvenger(int *numAppearances, int &NUM_AVENGERS)
{
    int useri; //a variable that collects the user input
    int *NewArray = new int [NUM_AVENGERS+1]; //dynamically allocates another element
    cout<<"Add new Avenger"<<endl<<"Please enter in the Number of Appearances..."<<endl;
    cin>>useri; //prompts for user input
    for (int i = 0; i < NUM_AVENGERS; i++)
        *(NewArray + i) = *(numAppearances + i);
    *(NewArray + (NUM_AVENGERS)) = useri; //assigns the new element to user input
    NUM_AVENGERS += 1;

    delete [] numAppearances; //deletes dynamic memory
    return NewArray; //returns the array with a new element
}