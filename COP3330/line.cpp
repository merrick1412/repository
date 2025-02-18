//
// Created by merrick on 9/16/2022.
//
#include "line.h"
#include <iostream>
using namespace std;
//constructors
Line::Line()
{
    xCoord = 0;
    yCoord = 0;
    slope = 1;
}
Line::Line(double m)
{
    xCoord = 0;
    yCoord = 0;
    slope = m;
}
Line::Line(double m, double y)
{
    xCoord = 0;
    yCoord = y;
    slope = m;
}
Line::Line(double x, double y, double m)
{
    xCoord = x;
    yCoord = y;
    slope = m;
}
//getters and setters
void Line::SetXCoord(double x)
{
    xCoord = x;
}
double Line::GetXCoord() const
{
    return xCoord;
}

void Line::SetYCoord(double y)
{
    yCoord = y;
}
double Line::GetYCoord() const
{
    return yCoord;
}

void Line::SetSlope(double m)
{
    slope = m;
}
double Line::GetSlope() const
{
    return slope;
}

void Line::PrintPointSlope()
{
    cout<<"The line in point slope form is: ";
    cout<<"y-"<<yCoord<<"="<<slope<<"(x-"<<xCoord<<")"<<endl;
}

void Line::PrintSlopeIntercept()
{
double yIntercept = (yCoord - (slope*xCoord));
    cout<<"The line in slope intercept form is: ";
    cout<<"y="<<slope<<"x+"<<yIntercept<<endl;
}

void Line::PrintStandard()
{
double a,c;
a = slope;
c = (((xCoord*slope) - yCoord)*-1);
    cout<<"The line in standard form is: ";
    cout<<a<<"x+y="<<c<<endl;
}

Line Line::GetPerpendicular()
{
    double prpSlope = (1 / slope *-1);
    Line prp;
    prp.SetSlope(prpSlope);
    prp.SetXCoord(xCoord);
    prp.SetYCoord(yCoord);
    return prp;
}

void Line::Intersection(Line inters)
{
    double xIntCoord,yIntCoord;
    double yInterc1,yInterc2;
    double yCoord2 = inters.GetXCoord();
    double xCoord2 = inters.GetXCoord();
    double slope2 = inters.GetSlope();
    yInterc1 = (yCoord - (slope * xCoord));
    yInterc2 = (yCoord2 - (slope2 * xCoord2));
    xIntCoord = (((yInterc1-yInterc2) / (slope-slope2)*(-1)));
    yIntCoord = ((xIntCoord * slope) + yInterc1);
    cout<<"The coordinates of the intersection are ";
    cout<<"("<<xIntCoord<<","<<yIntCoord<<")"<<endl;

}