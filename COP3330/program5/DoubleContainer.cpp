#include "DoubleContainer.h"
#include <iostream>
using namespace std;

//constructors
DoubleContainer::DoubleContainer()
{
    maxsize = 5; //default constructor
    size = 0;
    content = new double[maxsize]; //DMA
}
DoubleContainer::~DoubleContainer()//destructor
{
    delete [] content; //deletes DMA
}
DoubleContainer::DoubleContainer(double array[],int size1)
{
    maxsize = 5;
    size = 0; //setting default values

    content = new double[maxsize]; //new DMA of the same size as the array being copied
    for (int i = 0;i<size1;i++) {
        Add(array[i]); //copying the array over
    }
}
DoubleContainer::DoubleContainer(DoubleContainer& t)//deep copy constructor
{

    maxsize = t.maxsize; //copying the values over
    size = t.size;
    content = new double[maxsize]; //allocates memory for the copy
    for(int i = 0;i < maxsize; i++)
    {
        content[i] = t.content[i]; //copying over the array
    }
}
DoubleContainer DoubleContainer::operator=(const DoubleContainer& t)
{
    delete [] t.content; //deletes old DMA
    DoubleContainer temp; //temporary object
    temp.maxsize = t.maxsize; //copies values
    temp.size = t.size;
    temp.content = new double[maxsize]; //new DMA
            for(int i = 0;i<maxsize;i++)
                temp.content[i] = t.content[i]; //copies over array
    return temp; //returns temporary object

}

std::ostream &operator<<(std::ostream& os, const DoubleContainer &t)
{
    os << "<"; //top of wrapper
    for (int i = 0; i < t.size; i++)
        os<<t.content[i]<<","; //prints values segmented by commas
    os<<">"<<endl; //bottom of wrapper
    return os << std::endl;
}

DoubleContainer operator+(DoubleContainer& t1, DoubleContainer& t2)
{
    double temp;
    if (t1.size != t2.size)
    {
        cout<<"Validation error! both containers must be the same size!"<<endl;
        return t1; //makes sure both containers are the same size
    }
    DoubleContainer sum; //new object to be returned
    for (int i = 0;i<t1.size;i++) {
        temp = (t1.content[i] + t2.content[i]); //adds the arrays together
        sum.Add(temp); //calls add function, which takes care of growing and inserting
    }
    return sum; //returns the new object
}

DoubleContainer operator-(DoubleContainer& t1, DoubleContainer& t2)
{
    double temp;
    if (t1.size != t2.size)
    {
        cout<<"Validation error! both containers must be the same size!"<<endl;
        return t1; //makes sure both containers are the same size
    }
    DoubleContainer sum; //new object to be returned
    for (int i = 0;i<t1.size;i++) {
        temp = (t1.content[i] - t2.content[i]); //subtracts the elements
        sum.Add(temp);
    }
    return sum; //returns the new object

}
DoubleContainer operator-(DoubleContainer& t)
{
    double temp;
    DoubleContainer neg;
    for (int i = 0; i<t.size; i++) {
        temp = (t.content[i] * -1); //multiplies all elements by -1
        neg.Add(temp);
    }
    return neg;
}

DoubleContainer operator*(double mult,DoubleContainer& t)
{
    double temp;
    DoubleContainer prod;
    for (int i = 0; i<t.size; i++) {
        temp = ((t.content[i]) * mult); //multiplies all elements by provided number
        prod.Add(temp);
    }
    return prod;
}

DoubleContainer operator*(DoubleContainer& t1,DoubleContainer& t2)
{
    if (t1.size != t2.size)
    {
        cout<<"Validation error! both containers must be the same size!"<<endl;
        return t1; //makes sure both arrays are same size
    }
    double temp;
    DoubleContainer product;
    for (int i = 0;i<t1.size;i++) {
        temp = (t1.content[i] * t2.content[i]); //dot product
        product.Add(temp);
    }
    return product;
}

void DoubleContainer::Add(double t)//adds double parameter to end of array
{
    if (size == maxsize)
    {
        Grow();
    }
    //increments size
    content[size++] = t; //adds the double t to the end


}

void DoubleContainer::Clear() //clears out the array
{
    delete [] content; //destructs old object
    maxsize = 5;
    size = 0;
    content = new double[maxsize]; //creates a new one with default values

}
double DoubleContainer::Remove() //removes the last value of the array and returns it
{
    double temp;
    temp = content[size]; //saves the last value to temp
    content[size] = 0; //sets it to 0
    size--; //decrements size
    return temp;
}

void DoubleContainer::Grow() {
    maxsize = (maxsize + 10); //adds 10 more spaces
    double *newlist = new double[maxsize]; //new DMA for extra 10 spaces
    for (int i = 0; i<size; i++)
        newlist[i] = content[i]; //pointer towards new dma takes old array values
    delete [] content; //deletes old dma
    content = newlist; //copies newlist properties into objects content member, the array
}





