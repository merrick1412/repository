#include <iostream>
#include "line.h"
using namespace std;
int main()
{
    Line firstline;
    Line secondline(7);
    Line thirdline(14,13);
    Line fourthline(32,44,12);

    cout<<"The first lines coordinates are: x="<<firstline.GetXCoord()<<" y="<<firstline.GetYCoord()
    <<" slope="<<firstline.GetSlope()<<endl;
    cout<<"The first line with default values in all its forms:"<<endl;
    firstline.PrintPointSlope();
    firstline.PrintSlopeIntercept();
    firstline.PrintStandard();
    cout<<"The line perpendicular to this line is: "; firstline.GetPerpendicular().PrintSlopeIntercept();
    cout<<endl;

    cout<<"The second lines coordinates are: x="<<secondline.GetXCoord()<<" y="<<secondline.GetYCoord()
        <<" slope="<<secondline.GetSlope()<<endl;
    cout<<"The second line in all its forms:"<<endl;
    secondline.PrintPointSlope();
    secondline.PrintSlopeIntercept();
    secondline.PrintStandard();
    cout<<"The line perpendicular to this line is: "; secondline.GetPerpendicular().PrintSlopeIntercept();
    cout<<endl;

    cout<<"The third lines coordinates are: x="<<thirdline.GetXCoord()<<" y="<<thirdline.GetYCoord()
        <<" slope="<<thirdline.GetSlope()<<endl;
    cout<<"The third line in all its forms:"<<endl;
    thirdline.PrintPointSlope();
    thirdline.PrintSlopeIntercept();
    thirdline.PrintStandard();
    cout<<"The line perpendicular to this line is: "; thirdline.GetPerpendicular().PrintSlopeIntercept();
    cout<<endl;

    cout<<"The fourth lines coordinates are: x="<<fourthline.GetXCoord()<<" y="<<fourthline.GetYCoord()
        <<" slope="<<fourthline.GetSlope()<<endl;
    cout<<"The fourth line in all its forms:"<<endl;
    fourthline.PrintPointSlope();
    fourthline.PrintSlopeIntercept();
    fourthline.PrintStandard();
    cout<<"The line perpendicular to this line is: "; fourthline.GetPerpendicular().PrintSlopeIntercept();
    cout<<endl;

    cout<<"The intersecting coordinates of line three and line four are :";
    thirdline.Intersection(fourthline);
    return 0;
}
