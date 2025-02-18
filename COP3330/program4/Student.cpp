#include <iostream>
#include <cstring>
#include <iomanip>
#include "Student.h"
using namespace std;

std::ostream& operator<<(std::ostream& os, const Student& t) //overloads << to print out a student
{
    return os <<"\tStudent name: "<<t.name<<"\tStudent major: "<<
    t.major<<"\tStudent id: "<<t.id<<"\tStudent seniority: "<<t.year<<endl;
}

//constructors, destructors
Student::Student() //all values set to null
{
    name = new char[1];
    name[0] = '\0';

    major = new char[1];
    major[0] = '\0';

    year = '\0';

    id = new char[1];
    id[0] = '\0';
}
Student::Student(const Student& t)
{
    //copy of student class
    SetName(t.GetName());
    SetID(t.GetID());
    SetYear(t.GetYear());
    SetMajor(t.GetMajor());
}
Student::Student(const char *sname, const char *m, const char *id1, char year1)
{
    name = new char[(strlen(sname))+1]; //takes in a string and puts it in character array, the same way done in entry
        strcpy(name, sname);

    id = new char[(strlen(id1))+1];
        strcpy(id,id1);

    major = new char[(strlen(m))+1];
        strcpy(major, m);

    year = year1; //array not needed for year, due to only being 1 character
}

Student::~Student()
{
    delete [] id; //destructs
    delete [] major;
    delete [] name;
}

//getters setters
void Student::SetName(const char *name1)
{
delete [] name; //deletes old name array allocation, then makes new one
    name = new char[(strlen(name1))+1];
        strcpy(name, name1);
}
const char* Student::GetName() const
{
    return name; //returns name
}

void Student::SetMajor(const char* major1)
{
    delete [] major; //same logic as with name
    major = new char[(strlen(major1))+1];
        strcpy(major, major1);
}
const char* Student::GetMajor() const
{
    return major; //returns major
}

void Student::SetID (const char* id1)
{
delete [] id; //same as other setters
    id = new char[(strlen(id1))+1];
        strcpy(id, id1);
}
const char* Student::GetID() const
{
    return id;
}

void Student::SetYear(char year1)
{
    year = year1; //simple setter due to no dynamic allocation
}
const char Student::GetYear() const
{
    return year;
}

//adding and displaying
void Student::addStudent()
{
    cout<<"\nType the student's name: "; //this prompts user input
        cin.getline(name,20); //takes in user input and puts it into data members, same as done in entry.cpp

    cout<< "\nEnter the student's major: ";
        cin.getline(major, 20);

    cout<< "\nEnter the student's seniority, F for freshman, S for sophomore,\nJ for junior, E for senior, and + for higher."
    <<endl;
        char useri;
        cin >> useri;
        year = useri;
        cin.ignore(100,'\n'); //clears up buffer from cin, due to a leftover \n at the end
    cout<<"\n Enter the student's fsu id: ";
        cin.getline(id, 20);

}

void Student::operator=(const Student& t) //allows me to use object = object instead of manually setting
{
    SetName(t.GetName());
    SetMajor(t.GetMajor());
    SetID(t.GetID());
    SetYear(t.GetYear());
}



