/* Name: Merrick Moncure
Date: 2/6/2022
Section:7
Assignment: Ordered Exam Scores
Due Date: 2/6/2022
About this project: Write a program to find twin prime numbers under a user input and run it using g++
Assumptions: N/A
All work below was performed by Merrick Moncure */
#include <iostream>
using namespace std;
int main()
{
int upper_limit, primecheck, tested_number, factor; //defines variables
int last_prime = -1; //sets a value for the previous prime number as a placeholder
int primeamnt = 0; //number of prime numbers found
cout <<"Welcome to the twin prime numbers program"<<endl; //welcome message
cout<<"What is the upper value? (must be an integer)"<<endl; //asks for user input
cin >> upper_limit; //assigns user input to upper limit variable
while (upper_limit < 0) //tests for valid input
{
    cout << "please enter a valid input (must be an integer)"<<endl;
    cin >> upper_limit;
}
for (tested_number = 2; tested_number < upper_limit; tested_number++) //tests numbers under the upper limit
{
    primecheck = 1; //assumes a number is prime, will change if factor is found
    for (factor = 2; factor < tested_number; factor++) //tests all numbers below the tested number for a factor
    {
        if (tested_number % factor == 0) //factor check
        {
        primecheck = 0; //makes the number not prime if factor is found
        break;
        }
    }
        if (primecheck && last_prime > 0 && last_prime + 2 == tested_number) //finds twin prime numbers
        {
        cout << "(" << last_prime << "," << tested_number << ")"<<endl; //outputs the twin primes
        primeamnt++;
        }
        if (primecheck == 1)
        {
        last_prime = tested_number; //assigns found prime numbers to last prime variable

        }
}
cout << primeamnt <<" Twin prime numbers found!"<<endl;

}
