/* Name: Merrick Moncure
Date: 4/10/2022
Section:7
Assignment: Avengers Data by Range Program
Due Date: 4/10/2022
About this project: Develop, compile, and run a C++ program that requires the proper use of arrays of structures in
 a program using a top-down approach in a well-structured design using procedural programming techniques.
Assumptions: N/A
All work below was performed by Merrick Moncure */
#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;



struct Avengers //structure that contains the avengers stats
{
    string range;
    int upperlim;
    int males;
    int females;
    int died;
    int alive;
};

void displayData(Avengers ranges[]); //prototyping functions
void readFile(Avengers ranges[]);
void avengersDead(Avengers ranges[]);
void femaleAvengers(Avengers ranges[]);

int main()
{
char casechoice; //holds the choice for the switch menu

Avengers ranges[6]; //sets the ranges and upper limits for the structures
    ranges[0].range = "<=750";
    ranges[1].range = "> 750 and <= 1500";
    ranges[2].range = "> 1500 and <= 2250";
    ranges[3].range = "> 2250 and <= 3000";
    ranges[4].range = "> 3000 and <= 3750";
    ranges[5].range = "> 3750 and <= 4500";

    ranges[0].upperlim = 750;
    ranges[1].upperlim = 1500;
    ranges[2].upperlim = 2250;
    ranges[3].upperlim = 3000;
    ranges[4].upperlim = 3750;
    ranges[5].upperlim = 4500;
    for (int i = 0; i < 6; i++) // sets all elements to 0
    {
        ranges[i].males = 0;
        ranges[i].females = 0;
        ranges[i].died = 0;
        ranges[i].alive = 0;
    }
    readFile(ranges); // reads all the data into the array
    while (true)
    {

        cout << "Menu Options:" << endl;
        cout << "A) Display Data" <<endl;
        cout << "B) Find Range with the largest number of Avengers who have died"<<endl;
        cout << "C) Find Range with the largest percentage of Avengers who are female"<<endl;
        cout << "D) Quit"<<endl;
        cin >> casechoice;
        switch (casechoice)
        {
            case 'A':
                displayData (ranges);
                break;
            case 'B' :
                avengersDead (ranges);
                break;
            case 'C' :
                femaleAvengers (ranges);
                break;
            case 'D' :
                break;

        }
    if (casechoice == 'D')
            break;
    }


}

void readFile(Avengers ranges[]) //reads all the files data into the structure array
{
    string name; //string variables to collect the raw data
    string appearances;
    string gender;
    string died;
    int appearancesnum;
    int gendernum;
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

            appearancesnum = (stoi(appearances));

            if (gendernum == 0 && appearancesnum < ranges[0].upperlim )
                (ranges[0].males++);
            if (gendernum == 0 && appearancesnum < ranges[1].upperlim && appearancesnum > ranges[0].upperlim)
                (ranges[1].males)++;
            if (gendernum == 0 && appearancesnum < ranges[2].upperlim && appearancesnum > ranges[1].upperlim)
                (ranges[2].males)++;
            if (gendernum == 0 && appearancesnum < ranges[3].upperlim && appearancesnum > ranges[2].upperlim)
                (ranges[3].males)++;
            if (gendernum == 0 && appearancesnum < ranges[4].upperlim && appearancesnum > ranges[3].upperlim)
                (ranges[4].males)++;
            if (gendernum == 0 && appearancesnum < ranges[5].upperlim && appearancesnum > ranges[4].upperlim)
                (ranges[5].males)++;

            if (gendernum == 1 && appearancesnum < ranges[0].upperlim)
                (ranges[0].females)++;
            if (gendernum == 1 && appearancesnum < ranges[1].upperlim && appearancesnum > ranges[0].upperlim)
                (ranges[1].females)++;
            if (gendernum == 1 && appearancesnum < ranges[2].upperlim && appearancesnum > ranges[1].upperlim)
                (ranges[2].females)++;
            if (gendernum == 1 && appearancesnum < ranges[3].upperlim && appearancesnum > ranges[2].upperlim)
                (ranges[3].females)++;
            if (gendernum == 1 && appearancesnum < ranges[4].upperlim && appearancesnum > ranges[3].upperlim)
                (ranges[4].females)++;
            if (gendernum == 1 && appearancesnum < ranges[5].upperlim && appearancesnum > ranges[4].upperlim)
                (ranges[5].females)++;

            if (diednum == 0 && appearancesnum < ranges[0].upperlim)
                (ranges[0].died)++;
            if (diednum == 0 && appearancesnum < ranges[1].upperlim && appearancesnum > ranges[0].upperlim)
                (ranges[1].died)++;
            if (diednum == 0 && appearancesnum < ranges[2].upperlim && appearancesnum > ranges[1].upperlim)
                (ranges[2].died)++;
            if (diednum == 0 && appearancesnum < ranges[3].upperlim && appearancesnum > ranges[2].upperlim)
                (ranges[3].died)++;
            if (diednum == 0 && appearancesnum < ranges[4].upperlim && appearancesnum > ranges[3].upperlim)
                (ranges[4].died)++;
            if (diednum == 0 && appearancesnum < ranges[5].upperlim && appearancesnum > ranges[4].upperlim)
                (ranges[5].died)++;

            if (diednum == 1 && appearancesnum < ranges[0].upperlim)
                (ranges[0].alive)++;
            if (diednum == 1 && appearancesnum < ranges[1].upperlim && appearancesnum > ranges[0].upperlim)
                (ranges[1].alive)++;
            if (diednum == 1 && appearancesnum < ranges[2].upperlim && appearancesnum > ranges[1].upperlim)
                (ranges[2].alive)++;
            if (diednum == 1 && appearancesnum < ranges[3].upperlim && appearancesnum > ranges[2].upperlim)
                (ranges[3].alive)++;
            if (diednum == 1 && appearancesnum < ranges[4].upperlim && appearancesnum > ranges[3].upperlim)
                (ranges[4].alive)++;
            if (diednum == 1 && appearancesnum < ranges[5].upperlim && appearancesnum > ranges[4].upperlim )
                (ranges[5].alive)++;

            i++; //increments
        }
        Data.close();
    }
}

void displayData(Avengers ranges[]) //displays the values in the array
{
cout<<"           Range     Num Females      Num Males  Num Died OnceNum Never Died Once"<<endl;
    cout<<setw(17)<<ranges[0].range<<setw(15)<<ranges[0].females<<setw(15)<<ranges[0].males<<setw(15)<<ranges[0].alive<<setw(15)<<ranges[0].died<<endl;
    cout<<setw(17)<<ranges[1].range<<setw(15)<<ranges[1].females<<setw(15)<<ranges[1].males<<setw(15)<<ranges[1].alive<<setw(15)<<ranges[1].died<<endl;
    cout<<setw(17)<<ranges[2].range<<setw(14)<<ranges[2].females<<setw(15)<<ranges[2].males<<setw(15)<<ranges[2].alive<<setw(15)<<ranges[2].died<<endl;
    cout<<setw(17)<<ranges[3].range<<setw(14)<<ranges[3].females<<setw(15)<<ranges[3].males<<setw(15)<<ranges[3].alive<<setw(15)<<ranges[3].died<<endl;
    cout<<setw(17)<<ranges[4].range<<setw(14)<<ranges[4].females<<setw(15)<<ranges[4].males<<setw(15)<<ranges[4].alive<<setw(15)<<ranges[4].died<<endl;
    cout<<setw(17)<<ranges[5].range<<setw(14)<<ranges[5].females<<setw(15)<<ranges[5].males<<setw(15)<<ranges[5].alive<<setw(15)<<ranges[5].died<<endl;
}

void avengersDead(Avengers ranges[]) //calculates the range with the largest amount of avengers who have died
{
    string maxdead;
    cout<< "The range with the largest number of avengers who have died once is ..."<<endl;
    cout<< "Range Number of Appearances: "<<endl;
    for (int i = 0;i < 6; i++)
    {
      int max = (ranges[0].died);
          if (ranges[i].died > max)
          {
              max = (ranges[i].died);
              cout<<max;
          }
          if ((ranges[i].died) == max)
            maxdead = ranges[i].range;
    }
    cout<<maxdead<<endl;
}

void femaleAvengers(Avengers ranges[])  //calculates the range with the largest percentage of female avengers
{
    cout<<"The range with the largest percentage of avengers who are female is ..."<<endl;
    cout<<"Range Number of Appearances: ";
    string maxfemale;
    double percent;
    int avengertotal = 0;
    for (int i = 0; i < 6; i++)
    {
       avengertotal += ranges[0].males;
       avengertotal += ranges[0].females;
       percent = (ranges[0].females/avengertotal);
       if ((ranges[i].females/avengertotal) > percent)
           percent = (ranges[i].females/avengertotal);
       if ((ranges[i].females/avengertotal) == percent)
           maxfemale = ranges[i].range;
    }
    cout<< maxfemale<<endl;
}