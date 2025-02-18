

#include <iostream>
#include "blob.h"
#include <vector>
#include <stdio.h>

using namespace std;

int main()
{
//srand(time(NULL));
char blueteam = 'b';
char redteam = 'r';
    blob blueblob1(1,blueteam);
    blob blueblob2(2,blueteam);
    blob blueblob3(3,blueteam);
    blob blueblob4(4,blueteam);
        
    blob redblob1(5,redteam);
    blob redblob2(6,redteam);
    blob redblob3(7,redteam);
    blob redblob4(8,redteam);
    
    vector<blob> blobs{
    
        blueblob1,blueblob2,blueblob3,blueblob4,
        redblob1,redblob2,redblob3,redblob4,
    };
    cout<<blobs[4].GetY()<<endl;
    
    
for (int i = 0; i < 9; i++)
    
    

    return 0;
}
