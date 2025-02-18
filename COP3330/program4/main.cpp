#include <iostream>
#include "Canvas.h"
#include "Course.h"
#include "Student.h"
#include <cctype>
using namespace std;
void mainMenu();
void courseMenu();
char menuValidation(char c);


int main()
{
Canvas c;
char cmd;
mainMenu();
do {


    cin >> cmd;
    cin.ignore(100, '\n');
    cmd = toupper(cmd);
    menuValidation(cmd);

    switch (cmd) {
        case 'I':
            c.newCourse();
            break;
        case 'S':
            c.findCourse();
            break;
        case 'R':
            c.removeCourse();
            break;
        case 'E': courseMenu();
                char cmd2;

            do {
                cin >> cmd2;
                cin.ignore(100,'\n');
                switch (cmd2) {
                    case 'C':c.changeStudentC(); break;
                    case 'A':c.addStudentC(); break;
                    case 'D':c.removeStudent(); break;
                    case 'F':c.studentSearch(); break;
                    case 'V':c.showStudents(); break;
                    case 'B':cout<<"Leaving course menu.."<<endl;break;
                }


            } while(cmd2 != 'B');

            break;
        case 'D':
            c.showCourses();
            break;
        case '?':
            mainMenu();
            break;
        case 'Q':
            break;
    }
} while (cmd != 'Q');
}

void mainMenu()
{
    cout<<"---Course Database---"<<endl;
    cout<<"\tI\tInsert a new course into the directory"<<endl;
    cout<<"\tS\tSearch for a course in the directory"<<endl;
    cout<<"\tR\tRemove a course from the directory"<<endl;
    cout<<"\tE\tEdit a course in the directory"<<endl;
    cout<<"\tD\tDisplay the course directory"<<endl;
    cout<<"\t?\tDisplay this menu"<<endl;
    cout<<"\tQ\tQuit"<<endl;
}

void courseMenu()
{
    cout<<"---Course Menu---"<<endl;
    cout<<"\tC\tChange a student in a course"<<endl;
    cout<<"\tA\tAdd a student"<<endl;
    cout<<"\tD\tDelete a student"<<endl;
    cout<<"\tF\tFind a Student"<<endl;
    cout<<"\tV\tDisplay the Students in a class"<<endl;
    cout<<"\tB\tGo back"<<endl;

}

char menuValidation(char c)
{
    if ((c == 'I') || (c == 'S') || (c == 'R') || (c == 'E') || (c == 'D')
    || (c == '?') || (c == 'Q'))
    {
        return c;
    }
    else
    {
        cout<<"Illegal command, please enter one of the displayed commands..."<<endl;
        mainMenu();
        cin>>c;
        c = toupper(c);
        menuValidation(c);
    }
}

