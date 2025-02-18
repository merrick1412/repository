#include <iostream>
#ifndef PROG3_STUDENT_H
#define PROG3_STUDENT_H
class Student
{
    friend std::ostream& operator<<(std::ostream& os, const Student& t); //operator overload to print out student

public:
    void operator=(const Student& t); //operator overload to copy a student to another
    //constructors, destructors
    Student();
    Student(const Student& t);
    Student(const char *sname, const char *m, const char *id1, char year);
    ~Student();

    //getters setters
    void SetName(const char *name1);
    const char* GetName() const;
    void SetMajor(const char* major1);
    const char* GetMajor() const;
    void SetID (const char* id1);
    const char* GetID() const;
    void SetYear(char year1);
    const char GetYear() const;

    //adding
    void addStudent();

private:
    char year;
    char* name;
    char* major;
    char* id;

};


#endif //PROG3_STUDENT_H
