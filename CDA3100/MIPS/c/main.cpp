#include <iostream>
using namespace std;
int matrix(int);
int main() {
    int size;
   cout<<"Matrix array program"<<endl;
   cout<<"Please enter in the size of the matrix 2-6:"<<endl;
   cin>>size;
    while (size<2||size>6) {
        cout<<"Size needs to be between 2-6, reenter size"<<endl;
        cin>>size;
    }
    matrix(size);
}



int matrix(int size)
{
    int matrix1[size*size];
    int matrix2[size*size];
    int matrix3[size*size];

    cout<<"Please enter the numbers for matrix 1"<<endl;
        for(int i = 0;i<size*size;i++)
        {
            cout<<"\nNumber: ";
                cin>>matrix1[i];
                cin.ignore(100,'\n');
        }
        cout<<"Printing matrix A"<<endl;
        for(int i=1;i<(size*size)+1;i++)
        {

            cout<<matrix1[i-1]<<"\t";
            if (i % size == 0)
                cout<<"\n";
        }
        cout<<endl;
    cout<<"Please enter the numbers for matrix 2"<<endl;
    for(int i = 0;i<size*size;i++)
    {
        cout<<"\nNumber: ";
        cin>>matrix2[i];
        cin.ignore(100,'\n');
    }
    cout<<"Printing matrix B"<<endl;
    for(int i=1;i<(size*size)+1;i++)
    {

        cout<<matrix2[i-1]<<"\t";
        if (i % size == 0)
            cout<<"\n";
    }


}