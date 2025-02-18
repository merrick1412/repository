//
// Created by merrick on 4/19/2022.
//

#include "Avenger.h"

Avenger::Avenger()
{
    Name = "";
    Appearances = 0;
}

Avenger::Avenger(string name, int appearances)
{
    Name = name;
    Appearances = 0;
}

string Avenger::computeNumberOfAppearancesRange(int)
{
    if (Appearances <= 750)
    {
        return "<=750";
    }
    if (Appearances > 750 && Appearances <= 1500)
    {
        return "> 750 and <= 1500";
    }
    if (Appearances > 1500 && Appearances <= 2250)
    {
        return "> 1500 and <=2250";
    }
    if (Appearances > 2250 && Appearances <= 3000)
    {
        return "> 2250 and <=3000";
    }
    if (Appearances > 3000 && Appearances <= 3750)
    {
        return "> 3000 and <=3750";
    }
    else
    {
        return "> 3750 and <=4500";
    }
}
