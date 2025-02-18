/* Name: Merrick Moncure
Date: 2/20/2022
Section:7
Assignment: Playing With Numbers Program
Due Date: 2/20/2022
About this project: Write a program to find cousin primes under a number and check if its perfect
Assumptions: N/A
All work below was performed by Merrick Moncure */
#include <iostream>
void GetValidUserInputPosNumGT0(long int &num); //Prototyping functions
long int SumOfDivisors(long int num);
bool IsPrime(long int num);
void DisplayCousinPrimes(long int num);
bool IsPerfect(long int num);

using namespace std;


int main()
{
    char choice; //menu selection variable
    long int num; //the input number
    cout << "Welcome to playing with numbers!" << endl; //intro
    GetValidUserInputPosNumGT0(num); //input validation function
    bool perfectNumber = IsPerfect(num); //initializing perfect number variable with perfect number function
while (true) //infinite while loop to keep providing menu
{
    cout<<"1) Compute all the Cousin Prime Pairs less than a number"<<endl; //choices
    cout<<"2) Compute if a number is a Perfect number"<<endl;
    cout<<"3) Quit"<<endl;
    cin >> choice;

    switch (choice) //switch for choices
{
    case '1' : //displays cousin primes under input
        DisplayCousinPrimes(num);
        break; //breaks out of infinite loop to rerun

    case '2' :
        if (perfectNumber) //tests if input is perfect number using boolean
    {
        cout << num << " is perfect." << endl;
    }
    else
        cout << num << " is not perfect." << endl;

        break;

    case '3' : //quit option
        break;

    default :
        cout << "invalid choice" << endl;
}
if (choice == '3') //quits the program if 3 was chosen
    {
    break;
    }
}



}
void GetValidUserInputPosNumGT0(long int &num) //validation function
{

    cout <<"Please enter an integer greater than 0"<<endl;
    cin >> num;
    while (num <= 0) //checks for <0
    {
        cout<<"Please enter a valid integer greater than 0"<<endl;
        cin>>num;
    }
}
long int SumOfDivisors(long int num) //divisor sum function
{

    int sum = 0; //sets sum to 0 initially
    int increment; //the testing number
    for (increment = 1; increment <= num; increment++) //for loop that tests all numbers under input
    {
        if (num % increment == 0) //checks for divisor
        {
        sum += increment;
        }
    }
    return sum; //returns the sum to the function
}
bool IsPrime(long int num) //prime checking function
{

    int factorCheck; //serves same purpose as increment in previous function
    for (factorCheck = 2; factorCheck < num; factorCheck++) //same logic as checking for divisor
    {

        if (num % factorCheck == 0) //prime check
        {

        return false; //false if not prime
        }



    }

    return true; //true if prime
}
void DisplayCousinPrimes(long int num) //cousin prime function
{
int counter;
bool prime;
int lastPrime;
int cousinPrime;
for (counter = 2; counter < num; counter++) //checks all # under input
{

    prime = IsPrime(counter); //uses prime check function to check counter for prime

if (prime == true) //checks if prime
    {
    if (lastPrime + 4 == counter) //checks if cousin prime
        {
        cousinPrime = counter; //assigns the cousin prime to cousin prime variable
        cout<<"("<<lastPrime<<","<<cousinPrime<<")"<<endl; //prints the pair
        }
    lastPrime =  counter; //assigns prime numbers found to check for cousins
    }
}
}
bool IsPerfect(long int num) //perfect number function
{
    int sum; //sum variable
    sum = SumOfDivisors(num); //uses sum function to test for perfect
    if (sum - num == num) //perfect num test
    {
        return true; //true if perfect
    }
    return false; //false if not perfect
}
