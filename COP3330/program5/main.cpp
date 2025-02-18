/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include "DoubleContainer.h"
using namespace std;


int main() {
double testarray[20]{
    1,2,3,4,4.5,12,23,4,3,23,43,22,3,33,2,11,
    100,33,99,499,
};
DoubleContainer A;
DoubleContainer B;
DoubleContainer C(testarray,20);

A.Add(7); A.Add(4); A.Add(3); A.Add(9); A.Add(10);
B.Add(7); B.Add(4); B.Add(3); B.Add(9); B.Add(10);
cout<<"Container A is: "<<A<<endl;
cout<<"Container B is: "<<B<<endl;

cout<<"the sum of A + B is: ";
cout<<(A+B)<<endl;

cout<<"The difference between A - B is: "
<<(A-B)<<endl;

cout<<"The product of A*B is: "
<<(A*B)<<endl;

cout<<"The opposite of A is: "<<(-A)<<endl;

cout<<"B times 4 is: "<<(4*B)<<endl;

cout<<"C is: "<<C<<endl;

DoubleContainer D(C);
cout<<"Copied C into D. D is now: "<<D<<endl;


return 0;

}
