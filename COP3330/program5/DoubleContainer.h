#include <iostream>
using namespace std;
#ifndef UNTITLED_DOUBLECONTAINER_H
#define UNTITLED_DOUBLECONTAINER_H
class DoubleContainer
{
    //operator overloads
friend ostream& operator<<(ostream& os, const DoubleContainer &t);
friend DoubleContainer operator+(DoubleContainer&, DoubleContainer&);
friend DoubleContainer operator-(DoubleContainer&, DoubleContainer&);
friend DoubleContainer operator-(DoubleContainer&);
friend DoubleContainer operator*(double,DoubleContainer&);
friend DoubleContainer operator*(DoubleContainer&,DoubleContainer&);

public:
    DoubleContainer operator=(const DoubleContainer&);
    //constructors
    DoubleContainer();
    DoubleContainer(double [],int);
    DoubleContainer(DoubleContainer &);//deep copy constructor

    ~DoubleContainer();//destructor

    void Add(double); //adds double parameter to end of array
    void Clear(); //clears out the array
    double Remove(); //removes the last value of the array
private:
    void Grow();
    int size;
    int maxsize;
    double* content;
};



#endif //UNTITLED_DOUBLECONTAINER_H
