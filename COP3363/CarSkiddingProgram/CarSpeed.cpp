/* Name: Merrick Moncure
Date: 1/23/2022
Section:7
Assignment: Compute the speed of a car by skid marks Program
Due Date: 1/23/2022
About this project: Write a program to calculate the distance a car skidded and run it using g++
Assumptions: Assumes correct user input
All work below was performed by Merrick Moncure */
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;
int main()
{
    double f, s, d; //Defines f, d, and s as double variables
    cout << "Welcome to the compute the speed of a car by skid marks program" << endl; //Welcome message
    cout << "Type the distance the car skidded, " << endl; //Asks for the distance, d
    cin >> d; //Assigns d to user input
    cout << "and the friction coefficient of the road. " << endl; // asks for the friction coefficient, f
    cin >> f; //Assigns f to user input
    s = sqrt(30*d*f); //The equation for finding the speed of the car

    cout << left << setw(30) << "Car Speed: " << fixed << setprecision(15) << right << setw(50) << s << endl ; //Displays the car's speed with the number justified right
    cout << left << setw(30) << "Distance the car skidded: " << fixed << setprecision(15) << right << setw(50) << d << endl; //Displays the car's distance with the number justified right
    cout << left << setw(30) << "Friction coefficient: " << fixed << setprecision(15) << right << setw(50) << f << endl; //Displays the friction coefficient with the number justified right

}
