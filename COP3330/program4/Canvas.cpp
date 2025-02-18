#include <cstring>
#include <iostream>
#include "Canvas.h"
using namespace std;
//constructors and destructors
Canvas::Canvas()
{
    size = 0;
    arrLim = 2;
    classes = new Course[arrLim];
}
Canvas::~Canvas()
{
delete [] classes;
}


void Canvas::newCourse() //same grow logic as in Course.cpp
{
    if (size == arrLim)
    {
        grow(); //calls grow function if max is hit
    }
    classes[size].addCourse(); //calls the add course function in Course.cpp

size++; //incrementing size
}

void Canvas::removeCourse()
{
    char search[20]; //same search logic used for finding students in Course.cpp, similar to logic used in directory.cpp
    int found;
    if(size == 0)
    {
        cout <<"There is no courses added yet!"<<endl;
    }
    else
    {
        cout<<"Which course would you like to delete?: ";
        cin.getline(search, 20);
        found = courseSearch(search);
            if (found == -1)
                cout<<"\nCould not find the course!"<<endl;
            else if (size < 1)
            {
                cout<<"Deleting"<<classes[found];
                for(int i =found;i<size;i++)
                {
                    classes[i-1].SetBuilding(classes[i].GetBuilding());

                    classes[i-1].SetClass(classes[i].GetClass());

                    classes[i-1].SetName(classes[i].GetName());

                    classes[i-1].enrolledStudents = classes[i].enrolledStudents;

                }
                size--;
                cout<<"worked"<<endl;
            }
            else
            {
                classes[found].SetBuilding("\n");
                classes[found].SetName("\n");
                classes[found].SetClass("\n");
                delete [] classes[found].enrolledStudents;
                size--;
            }
    }

}
void Canvas::changeCourse()
{
    char search[20];
    int found;
    if (size == 0)
    {
        cout <<"There is no courses added yet!"<<endl;
    }
    else
    {
        cout<<"Which course would you like to change?: ";
        cin.getline(search,20);
        found = courseSearch(search);
        if (found == -1)
            cout<<"\nCould not find the course!"<<endl;
        else
        {
            cout<<"Changing course "<<classes[found]<<endl;
            cout<<"Enter in the new information "<<endl;
            classes[found].addCourse();
            cout<<"Updated to: "<< classes[found]<<endl;
        }
    }
}
void Canvas::showCourses() const
{
    if(size == 0)
        cout<<"There are no courses added yet."<<endl;
    else
    {
        for(int i=0;i<size;i++)
            cout<< classes[i];
    }
}

int Canvas::courseSearch(char *search)
{
    for (int i = 0; i<size; i++) //increment through array of names and id
    {
        // if the name or id searched matches one in the array, returns the index of said student
        if ((strcmp(classes[i].GetBuilding(), search)) == 0 || (strcmp(classes[i].GetName(), search)) == 0 || (strcmp(classes[i].GetClass(), search)) == 0)
            return i;
}
}

void Canvas::findCourse()
{
    char s[20];
    cout<<"Please enter the name, building, or code for the course you'd like to search for..."<<endl;
    cin.getline(s,20);
    int i = courseSearch(s);
    cout<<"Found "<<classes[i];
}

void Canvas::addStudentC() {
    char name[20];
    if(size == 0)
    {
        cout << "Add classes before trying to add a student to one!" << endl;
        return;
    }
    showCourses();
    cout<<"Which class would you like to add a student to?"<<endl;
    cin.getline(name,20);
    int found = courseSearch(name);
    if (found == -1)
        cout<<"\nCould not find the course!"<<endl;
    else
    {
        cout<<"Adding student to "<<classes[found]<<endl;
        classes[found].addStudent();
    }

}
void Canvas::removeStudent()
{
    char search[20];
    int found;
    if (size == 0)
    {
        cout <<"There is no courses yet!"<<endl;
    }

    else
    {
        showCourses();
        cout<<"Which course would you like to remove from?: ";
        cin.getline(search,20);
        found = courseSearch(search);
        if (found == -1)
            cout<<"\nCould not find the course!"<<endl;
        else
        {
            cout<<"Removing student from "<<classes[found]<<endl;
            classes[found].removeStudent();

        }
    }
}
void Canvas::changeStudentC()
{
char search[20];

if (size==0)
{
    cout<<"There is no courses added yet!"<<endl;
    return;
}
else
{
    cout<<"Enter the name of the course you would like to change students in..."<<endl;
    cin.getline(search,20);
    int found = courseSearch(search);
    if (found == -1)
        cout<<"Could not find the course!"<<endl;
    else
    {
        cout<<"Editing student in "<<classes[found]<<endl;
        classes[found].changeStudent();
    }
}
}
void Canvas::showStudents() {
    char search[20];
    int found;
    if (size == 0)
    {
        cout <<"There is no courses added yet!"<<endl;
    }
    else
    {
        cout<<"Which course would you like to see the students in?: ";
        showCourses();
        cin.getline(search,20);
        found = courseSearch(search);
        if (found == -1)
            cout<<"\nThere is no one in this course!"<<endl;
        else
        {
            classes[found].Display();
        }
    }
}
void Canvas::studentSearch() {
    char search[20];
    char searchclass[20];
    int found;
    if (size == 0)
    {
        cout <<"There is no courses added yet!"<<endl;
    }
    else
    {
        cout<<"Which course would you search in?: ";
        cin.getline(search,20);
        found = courseSearch(search);
        if (found == -1)
            cout<<"\nCould not find the course!"<<endl;
        else
        {
            cout<<"What name/id would you like to search for in "<<search<<"?"<<endl;
            cin.getline(searchclass,20);
            classes[found].Search(searchclass);
        }
    }
}

void Canvas::grow()
{

    Course* newlist = new Course[arrLim+1];
    cout<<"part one works"<<endl;
    for (int i=0; i<arrLim; i++)
    {
        cout<<"looping..."<<endl;
        newlist[i] = classes[i];
    }
    delete [] classes;
    cout<<"part 2 works"<<endl;
    classes = newlist;
    arrLim++;
}
