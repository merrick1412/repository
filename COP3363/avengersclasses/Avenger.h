//
// Created by merrick on 4/19/2022.
//

#ifndef UNTITLED_AVENGER_H
#define UNTITLED_AVENGER_H
#include <string>
using namespace std;
class Avenger
{
public:
    string Name, Gender;
    bool Died;
    int Appearances;


    Avenger ();
    Avenger (string, int);

    void setName (string n)
    {
        Name = n;
    }
    string getName()
    {
        return Name;
    }

    void setAppearances(int a)
    {
        Appearances = a;
    }
    int getAppearances()
    {
        return Appearances;
    }

    void setDied(bool d)
    {
        Died = d;
    }
    bool getDied()
    {
        return Died;
    }

    void setGender(string g)
    {
        Gender = g;
    }
    string getGender()
    {
        return Gender;
    }

    string computeNumberOfAppearancesRange(int);

};


#endif //UNTITLED_AVENGER_H
