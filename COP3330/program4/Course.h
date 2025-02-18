#include <iostream>
#include <cstring>
#include "Student.h"
#ifndef PROG3_COURSE_H
#define PROG3_COURSE_H
class Course
{
    //operator overload for printing a course
friend std::ostream& operator<<(std::ostream& os, const Course& t);

public:
    //constructor destructor
    Course();
    ~Course();

    //setters, getters
    void SetBuilding(const char *name1);
    void SetClass(const char *name1);
    void SetName(const char *name1);

    const char* GetName() const;
    const char* GetClass() const;
    const char* GetBuilding() const;

    //course manipulation
    int Search(char* search); //searches for a student
    void addStudent(); //adds students to course
    void addCourse(); //adds a course
    void changeStudent(); //modifies a students enrollment
    void removeStudent(); //deletes a student
    void Display(); //displays course list

    void operator=(const Course& t);

    Student *enrolledStudents;
private:
    //course attributes and grow function
    void Grow();
    char *name;
    char *classID;
    char *building;
    int arrLim; //array attributes
    int size;

};



#endif //PROG3_COURSE_H
