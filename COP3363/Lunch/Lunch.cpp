/* Name: Merrick Moncure
Date: 1/30/2022
Section:7
Assignment: What to have for lunch?
Due Date: 1/30/2022
About this project: Write a program to tell a user what to eat for lunch and run it using g++
Assumptions: N/A
All work below was performed by Merrick Moncure */
#include <iostream>
using namespace std;
int main()
{
char timeAnswer,breadAnswer,lettuceAnswer; //Established 3 character variables
cout << "Welcome to the what to have for lunch program!" <<endl; //welcome message
cout << "How much time do I have?" << endl; //Prints initial question
cout << "Enter A for a lot and B for not much" << endl;
cin >> timeAnswer; //Assigns user input to variable for how much time they have
if (timeAnswer == 'a' || timeAnswer == 'A') //If statement for a lot of time
{
  cout << "Do I have bread?" << endl; //Asks if the user has bread and for an input
  cout << "Type Y for yes or N for no." << endl;
  cin >> breadAnswer; //Assigns user input for having bread or not

  if (breadAnswer == 'y' || breadAnswer == 'Y') //If statement for having bread
  {
    cout << "Make a sandwich!"; //Prints one end node of the path
  }
  else if (breadAnswer == 'n' || breadAnswer == 'N') //If statement for not having bread
  {
    cout << "Do I have lettuce?" << endl; //Asks the question of having lettuce and asks for user input
    cout << "Type Y for yes and N for no." << endl;
    cin >> lettuceAnswer; //Puts user input into the variable for having lettuce
    if (lettuceAnswer == 'y' || lettuceAnswer == 'Y') //If statement for having lettuce
    {
    cout << "Make a salad!"; //Prints an end node
    }
    else if (lettuceAnswer == 'n' || lettuceAnswer == 'N') //If statement for not having lettuce
    cout << "Better run to the store!"; //Prints an end node
    else //else statement for an invalid input
    {
    cout << "Invalid answer. Please rerun the program and enter a valid answer.";
    }
    }
    else //else statement for invalid input
    {
    cout << "Invalid answer. Please rerun the program and enter a valid answer.";
    }

}
if (timeAnswer == 'b' || timeAnswer == 'B') // If statement for not having a lot of time
{
  cout << "Better throw something in the microwave."; //Prints an end node
}
if (timeAnswer != 'a' && timeAnswer != 'b' && timeAnswer != 'A' && timeAnswer != 'B') //if statement for an invalid response
  cout << "Invalid answer. Please rerun the program and enter a valid answer.";
}
