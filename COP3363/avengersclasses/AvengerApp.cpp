/* Name: Merrick Moncure
Date: 4/17/2022
Section:7
Assignment: Module 12: Avenger Data Using a Class Program & Unix Makefile
Due Date: 4/17/2022
About this project: Develop, compile, and run a C++ program that uses a minimal class to solve a problem
 using a top-down approach in a well-structured design using procedural programming techniques.
Assumptions: N/A
All work below was performed by Merrick Moncure */
#include <iostream>
#include <string>
#include "Avenger.h"
using namespace std;

void displayAvengers(Avenger, Avenger, Avenger, Avenger);

int main()
{
    Avenger ironman; //4 objects in the Avenger Class
    Avenger blackpanther;
    Avenger thor;
    Avenger spiderman;

    ironman.setAppearances(3068); //hard coding the stats for all 4 avengers
    ironman.setDied(true);
    ironman.setGender("MALE");
    ironman.setName("Anthony Stark");

    blackpanther.setAppearances(780);
    blackpanther.setDied(false);
    blackpanther.setGender("MALE");
    blackpanther.setName("Tchalla");

    thor.setAppearances(2402);
    thor.setDied(true);
    thor.setGender("MALE");
    thor.setName("Thor Odinson");

    spiderman.setAppearances(4333);
    spiderman.setDied(true);
    spiderman.setGender("MALE");
    spiderman.setName("Peter Parker");

    displayAvengers(ironman,blackpanther,thor,spiderman); //calls the function that displays the avengers
}

void displayAvengers(Avenger ironman, Avenger blackpanther, Avenger thor, Avenger spiderman)
{
    cout<<"Name: "<<ironman.getName()<<endl; //displays the avengers
    cout<<"Number Of Appearances: "<<ironman.getAppearances()<<endl;
    cout<<"Gender: "<<ironman.getGender()<<endl;
    cout<<"Died At Least Once: "<<ironman.getDied()<<endl;
    cout<<"Number Of Appearances Range: "<<ironman.computeNumberOfAppearancesRange(ironman.getAppearances())<<endl;
    cout<<" "<<endl;

    cout<<"Name: "<<blackpanther.getName()<<endl;
    cout<<"Number Of Appearances: "<<blackpanther.getAppearances()<<endl;
    cout<<"Gender: "<<blackpanther.getGender()<<endl;
    cout<<"Died At Least Once: "<<blackpanther.getDied()<<endl;
    cout<<"Number Of Appearances Range: "<<blackpanther.computeNumberOfAppearancesRange(blackpanther.getAppearances())<<endl;
    cout<<" "<<endl;

    cout<<"Name: "<<thor.getName()<<endl;
    cout<<"Number Of Appearances: "<<thor.getAppearances()<<endl;
    cout<<"Gender: "<<thor.getGender()<<endl;
    cout<<"Died At Least Once: "<<thor.getDied()<<endl;
    cout<<"Number Of Appearances Range: "<<thor.computeNumberOfAppearancesRange(thor.getAppearances())<<endl;
    cout<<" "<<endl;

    cout<<"Name: "<<spiderman.getName()<<endl;
    cout<<"Number Of Appearances: "<<spiderman.getAppearances()<<endl;
    cout<<"Gender: "<<spiderman.getGender()<<endl;
    cout<<"Died At Least Once: "<<spiderman.getDied()<<endl;
    cout<<"Number Of Appearances Range: "<<spiderman.computeNumberOfAppearancesRange(spiderman.getAppearances())<<endl;
}