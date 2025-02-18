/* Name: Merrick Moncure
Date: 4/3/2022
Section:7
Assignment: Avengers - Avengers Data Program
Due Date: 4/3/2022
About this project: Develop, compile, and run a C++ program that requires the proper use of arrays of structures in a
 program using a top-down approach in a well-structured design using procedural programming techniques.
Assumptions: N/A
All work below was performed by Merrick Moncure */
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

const int AvengeNum = 173;
//function prototypes
void readFile(string AvengerName[],int NumAppearances[],int Gender[],int Died[]);
void displayDeaths(string AvengerName[], int Died[]);
void avgNvrDie(int NumAppearances[], int Gender[], int Died[]);

int main()
{
    char caseChoice; //char variable for switch
    string AvengerName[AvengeNum]; //array for names
    int NumAppearances[AvengeNum]; //array for appearances
    int Gender[AvengeNum]; //array for gender, 0 for male 1 for female
    int Died[AvengeNum]; //array for died, 0 for no 1 for yes
    readFile(AvengerName,NumAppearances,Gender,Died); //function to read the file into the arrays

cout<<"Avengers Data"<<endl; //intro menu
cout<<"Options"<<endl;
cout<<"A) Display count and names of the Avengers who who have died at least once ..."<<endl;
cout<<"B) Display average number of appearances of Avengers who have never Died by gender..."<<endl;
cout<<"Please select option (A-B)...";
cin>>caseChoice;
    switch (caseChoice)
    {
        case 'a':
        case 'A':
            displayDeaths(AvengerName,Died); //calls function to display the deaths
            break;
        case 'b':
        case 'B':
            avgNvrDie(NumAppearances,Gender,Died); //calls function to display the average appearances for those who didnt die
            break;
        default :
            cout<<"Invalid option entered"<<endl;
    }
}

void readFile(string AvengerName[],int NumAppearances[],int Gender[],int Died[]) //function for reading into array
{
    string name; //string variables to collect the raw data
    string appearances;
    string gender;
    string died;
    string ignore;
    int gendernum; //for converting the strings into ints
    int diednum;
    ifstream Data; //ifstream object created
    Data.open("AvengersData.txt"); //opens the text file
    if (Data.is_open()) //runs the loop as long as the files open
    {
        int i = 0;
        while(getline(Data, name, '\t')) //separates the types of data by \t and \n at the end
        {
            getline(Data, appearances, '\t');
            getline(Data, gender, '\t');
            getline(Data, died);

                if (gender == "MALE") //converts from string to int
                    gendernum = 0;
                if (gender == "FEMALE")
                    gendernum = 1;
                if (died == "NO")
                    diednum = 0;
                if (died == "YES")
                    diednum = 1;

                AvengerName[i] = name; //assigns into parallel arrays
                NumAppearances[i] = (stoi(appearances));
                Gender[i] = gendernum;
                Died[i] = diednum;
                i++; //increments
        }
    }
    Data.close(); //closes the file
}

void displayDeaths(string AvengerName[], int Died[]) //displays the avengers who have died
{
    double deathTally = 0;
    cout<<"Display name and count of Avengers who have died at least once"<<endl;
    cout<<"The following Avengers have died at least once ...."<<endl;
    for (int i = 0; i < AvengeNum; i++) //increments through the arrays
    {
        if (Died[i] == 1) //checks for death
        {
            cout<<AvengerName[i]<<endl;
            deathTally++; //counter for avengers who have died
        }

    }
    cout<<"The number of Avengers have died at least once = "<<deathTally<<endl;
    cout<<"The percentage of Avengers have died at least once = "<<(deathTally/AvengeNum*100)<<endl; //displays the average
}

void avgNvrDie(int NumAppearances[], int Gender[], int Died[]) //displays average appearances who have not died by gender
{
    double maleAliveTally = 0; //sets a tally for never dying avengers by gender
    double femaleAliveTally = 0;
    double maleAppearanceSum = 0; //a sum amount for the respective appearances
    double femaleAppearanceSum = 0;
    cout<<"Display count of Avengers who have never Died by gender..."<<endl;

    for (int i = 0; i < AvengeNum; i++)
    {

        if(Died[i] == 0) //filters out dead avengers
        {
            if(Gender[i] == 0) //filters out females
            {
                maleAliveTally++;
                maleAppearanceSum += NumAppearances[i];
            }
            if (Gender[i] == 1) //filters out males
            {
                femaleAliveTally++;
                femaleAppearanceSum += NumAppearances[i];
            }

        }

    }
    cout<<"The average number of appearances of Avengers who have never Died"<<endl;
    cout<<"male = "<<setprecision(7)<<(maleAppearanceSum/maleAliveTally)<<endl; //displays the average appearances
    cout<<"female = "<<setprecision(7)<<(femaleAppearanceSum/femaleAliveTally)<<endl;
}