//
// Created by merrick on 9/16/2022.
//

#ifndef PROGRAM1_LINE_LINE_H
#define PROGRAM1_LINE_LINE_H
#endif //PROGRAM1_LINE_LINE_H
class Line
{
private:
    //private value members
    double xCoord;
    double yCoord;
    double slope;
public:
    Line();// a constructor that accepts 0 parameters, default constructor

    Line(double); // a constructor that accepts only 1 parameter, slope
    Line(double,double); //accepts 2 parameters, slope and y
    Line(double,double,double);//accepts 3 parameters, x, y and slope
    // Print function prototypes
    void PrintPointSlope();
    void PrintSlopeIntercept();
    void PrintStandard();
    //prototype for returning a perpendicular line
    Line GetPerpendicular();
    //protoype for taking a line and printing x and y of intersect
    void Intersection(Line);
    //getters and setters
    void SetXCoord(double);
    double GetXCoord() const;
    void SetYCoord(double);
    double GetYCoord() const;
    void SetSlope(double);
    double GetSlope() const;



};
