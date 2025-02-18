/* Name: Merrick Moncure
Date: 1/30/2022
Section:7
Assignment: Ordered Exam Scores
Due Date: 1/30/2022
About this project: Write a program to numerically sort 3 exam scores and run it using g++
Assumptions: N/A
All work below was performed by Merrick Moncure */
#include <iostream>
#include <iomanip>
using namespace std;
int main() {
float examScore1, examScore2, examScore3; //creates the exam score variables
cout << "Welcome to the Ordered Exam Scores program!" << endl; //introduction
cout << "Please enter in a Exam Score ..."; //Assigns variables examScore 1-3 to user input
cin >> examScore1;
cout << "Please enter in a Exam Score ...";
cin >> examScore2;
cout << "Please enter in a Exam Score ...";
cin >> examScore3;
cout<<endl;
    if (examScore1>examScore2 && examScore2>examScore3) //sorts the exam scores in descending numerical value
{
cout << examScore1 << endl << examScore2 << endl << examScore3;
}
    else if (examScore1>examScore3 && examScore3>examScore2)
cout << fixed << setprecision(1) <<  examScore1 << endl << examScore3 << endl <<examScore2;
    else if (examScore2>examScore1 && examScore1>examScore3)
cout << fixed << setprecision(1) <<  examScore2 << endl << examScore1 <<endl << examScore3;
    else if (examScore2>examScore3 && examScore3>examScore1)
cout << fixed << setprecision(1) <<  examScore2 << endl << examScore3 << endl << examScore1;
    else if (examScore3>examScore1 && examScore1>examScore2)
cout << fixed << setprecision(1) <<  examScore3 << endl << examScore1 << endl << examScore2;
    else if (examScore3 < examScore2 && examScore2 < examScore1)
cout << fixed << setprecision(1) <<  examScore3 << endl << examScore2 << endl << examScore1;
    else if (examScore1 == examScore2 && examScore2 == examScore3) //an output for when the values are all equal
cout << "All the Exam Scores are equal";
    else
cout << "Invalid input. Rerun the program and input a valid input."; //an output for an invalid input
}

