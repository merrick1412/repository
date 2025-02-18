#include "blob.h"
#include <iostream>
#include <stdio.h>
using namespace std;



blob::blob(int num1, char team)
{
    int health = 100;
    int power = 10;
    char color = team;
    int xCoord = rand()%10;
    int yCoord = rand()%10;
    int num = num1;
}

blob::blob()
{
    int health = 100;
    int power = 10;
    char color = 'a';
    int xCoord = -1;
    int yCoord = -1;
    int num = -1;
}
    int blob::GetX() const
    {
        return xCoord;
    }
    void blob::SetX(int x)
    {
        xCoord = x;
    }
    
    int blob::GetY() const
    {
        return yCoord;
    }
    void blob::SetY(int y)
    {
        yCoord = y;
    }
    
    char blob::GetTeam() const
    {
        return color;
    }
    void blob::SetTeam(char c)
    {
        color = c;
    }
    
    int blob::GetHP() const
    {
        return health;
    }
    void blob::SetHP(int hp)
    {
        health = hp;
    }
    
    int blob::GetPwr() const
    {
        return power;
    }
    void blob::SetPwr(int p)
    {
        power = p;
    }
    
    void blob::Move()
    {
        cout<<"To move up 1, press W."<<endl
        <<"To move down 1, press S."<<endl
        <<"To move right 1, press D."<<endl
        <<"To move left 1, press A."<<endl;
        char choice;
        cin>>choice;
        switch(choice)
        {
            case 'W': yCoord++;
                break;
            case 'w': yCoord++;
                break;
            case 'S': yCoord--;
                break;
            case 's': yCoord--;
                break;
            case 'A': xCoord--;
                break;
            case 'a': xCoord--;
                break;
            case 'D': xCoord++;
                break;
            case 'd': xCoord++;
                break;
            default: cout<<"Please enter a valid movement.";
        }
        
        cout<<"The new position of Blob"<<num<<
        " is ("<<xCoord<<","<<yCoord<<")"<<endl;
        
    }
    
    
