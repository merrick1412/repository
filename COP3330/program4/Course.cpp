#include "Course.h"
#include <iostream>
#include <cstring>
using namespace std;



Course::~Course() //destructor
{
    delete [] enrolledStudents;
    delete [] name;
    delete [] classID;
    delete [] building;
}
Course::Course()
{
    size = 0;
    arrLim = 2; //default limit of 2
    enrolledStudents = new Student[arrLim]; //array of student objects for each course object

    classID = new char[1]; //creating the 3 char arrays and assigning them null
        classID[0] = '\0';
    name = new char[1];
        name[0] = '\0';
    building = new char[1];
        building[0] = '\0';
}
//getters, setters
const char *Course::GetName() const
{
    return name;
}
void Course::SetName(const char *name1) //same as in student.cpp
{
    delete [] name;
    name = new char[(strlen(name1))+1];
        strcpy(name, name1);
}

const char* Course::GetClass() const
{
    return classID;
}
void Course::SetClass(const char *name1)
{
    delete [] classID;
    classID = new char[(strlen(name1))+1];
        strcpy(classID, name1);
}

const char *Course::GetBuilding() const
{
    return building;
}
void Course::SetBuilding(const char *name1)
{
    delete [] building;
    building = new char[(strlen(name1))+1];
        strcpy(building, name1);
}

void Course::addCourse() //exact same logic as in addStudent
{

    cout<<"Enter the Class code: ";
        cin.getline(classID, 20);

    cout<<"Enter the Class name: ";
        cin.getline(name, 20);

    cout<<"Enter the building it is in: ";
        cin.getline(building, 20);
    cout<<endl;
}

void Course::Grow() //grows the array of students in a course object, gets called when arrLim (the max size) is reached
{

    Student* tArray = new Student[arrLim+10]; //creates a temporary array to copy over
        for (int i=0;i<arrLim;i++)
        {
            tArray[i] = enrolledStudents[i]; //copies over the old array
        }
        delete [] enrolledStudents; //deletes old memory allocation
        enrolledStudents = tArray; //sets all the values of the old array
        arrLim += 10; //adds 10 to the max
}

void Course::Display()
{
    if (size == 0) //checks if the roster is empty
    {
        cout << "\nThere is no one in the class!" << endl;
    }
    else
    {
        for(int i=0;i<size;i++)
        {
            cout<<enrolledStudents[i]; //prints out every student up to the current size of the course
        }
    }
}

int Course::Search(char* search)
{
    for (int i = 0; i<size; i++) //increment thru array of names and id
    {
        // if the name or id searched matches one in the array, returns the index of said student
        if ((strcmp(enrolledStudents[i].GetID(), search)) || (strcmp(enrolledStudents[i].GetName(), search) == 0))
            return i;
    }
    return -1; //if cant find the student returns -1
}

void Course::removeStudent()
{
    char search[20]; //char array that will take user input, and feed it to search function
    int found;
    cout<<"Which student do you want to remove?";
    Display();
    cin.getline(search, 20);
    found = Search(search);
    if (found == -1) //found holds the return of the search function, if -1 nothing found
        cout<<"No student found"<<endl;
    else //if not -1, found will hold the index of the student that was searched
    {
        cout<<"Deleting... "<<enrolledStudents[found];
        for (int i = found+1; i<size; i++)
        {
            enrolledStudents[i - 1].SetName(enrolledStudents[i].GetName()); //pushes all the students back that were in front
            enrolledStudents[i - 1].SetMajor(enrolledStudents[i].GetMajor());//of the deleted student
            enrolledStudents[i - 1].SetID(enrolledStudents[i].GetID());
            enrolledStudents[i - 1].SetYear(enrolledStudents[i].GetYear());
        }
            size--; //decrements the size to represent a student getting removed
    }
}

void Course::changeStudent()
{
    int found;
    char search[20]; //same search logic used in removeStudent
    Display();
    cout<<"Type the student you wish to change: ";
    cin.getline(search, 20);
        found = Search(search);
    if (found == -1)
    {
        cout<<"Could not find student!"<<endl;
    }
    else
    {
        char name1[20]; //arrays to take in user input
        char id[20];
        char year;
        char major[20];
        cout<<"Found "<<enrolledStudents[found].GetName()<<"in class "<<name<<endl;
        cout<<"Student info: "<< enrolledStudents[found]<<endl;
        cout<<"\nType the new name"<<endl;
        cin.getline(name1,20);
        enrolledStudents[found].SetName(name1);
        cout<<"\nType the new ID"<<endl;
        cin.getline(id,20);
        enrolledStudents[found].SetID(id);
        cout<<"\nType the new major"<<endl;
        cin.getline(major,20);
        enrolledStudents[found].SetMajor(major);
        cout<<"Type the new year"<<endl;
        cin>>year;
        enrolledStudents[found].SetYear(year);
        cin.ignore(100,'\n'); //sets the students values to new ones
        return;
    }
}

void Course::addStudent()
{
    if (size == arrLim)
        Grow(); //calls grow function if max num of students is reached
    enrolledStudents[size++].addStudent(); //calls the add student function in Student.cpp
}

std::ostream& operator<<(std::ostream& os, const Course& t) //allows output of course classes using <<
{
    return os <<"\t| Name of Class: "<<t.name<<" |\t|Class Code: "<<
              t.classID<<"|\t|Building: "<<t.building<<"|\t|Size of Class: "<<t.size<<"|"<<endl;

}
void Course::operator=(const Course& t) //allows for copying using =
{
    for (int i=0;i<arrLim;i++) {
    enrolledStudents[i] = (t.enrolledStudents[i]);
    }
    SetName(t.GetName());
    SetBuilding(t.GetBuilding());
    SetClass(t.GetClass());

}