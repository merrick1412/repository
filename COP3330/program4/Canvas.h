//
// Created by merrick on 10/26/2022.
//
#ifndef PROG3_CANVAS_H
#define PROG3_CANVAS_H
#include "Course.h"
class Canvas
{
public:
    //constructors and destructors
    Canvas();
    ~Canvas();

    //course related
    void newCourse();
    void removeCourse();
    void changeCourse();
    void showCourses() const;
    int courseSearch(char *search);
    void findCourse();

    //student related
    void addStudentC();
    void removeStudent();
    void changeStudentC();
    void showStudents();
    void studentSearch();

private:
    Course* classes;
    int arrLim;
    int size = 0;
    void grow();


};


#endif //PROG3_CANVAS_H
