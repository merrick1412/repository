#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include "Stack.h"
#include "Stack.hpp"
#include <sstream>
#include <unordered_map>

using namespace std;
using namespace cop4530;
const int NORTH = 1;
const int EAST = 2;
const int SOUTH = 4;
const int WEST = 8;
int numrows;
int numcols;
struct PairHash {
    template <class T1, class T2>
    size_t operator () (const pair<T1, T2>& p) const {
        auto h1 = hash<T1>{}(p.first);
        auto h2 = hash<T2>{}(p.second);
        return h1 ^ h2;
    }
};
bool wallCheckN(int x, int y, vector<vector<int>>& maze){
    if (x >= 0 && x < numrows && y >= 0 && y < numcols){
        return (maze[x][y] & 0x1) == 0;
    }
    return false;
}
bool wallCheckE(int x, int y, vector<vector<int>>& maze){
    if (x >= 0 && x < numrows && y >= 0 && y < numcols){
        return (maze[x][y] & 0x2) == 0;
    }
    return false;

}
bool wallCheckS(int x, int y, vector<vector<int>>& maze) {
    if (x >= 0 && x < numrows && y >= 0 && y < numcols) {
        return (maze[x][y] & 0x4) == 0;

    }
    return false;
}
bool wallCheckW(int x, int y, vector<vector<int>>& maze) {
    if (x >= 0 && x < numrows && y >= 0 && y < numcols) {
        return (maze[x][y] & 0x8) == 0;
    }
    return false;
}
bool visitedCheck(int x, int y, unordered_map<pair<int,int>,
                                bool, PairHash>& visited){
    pair<int,int> key(x,y);
    if (visited[key]){
        return true;
    }
    return false;
}

void dfs(int start_row, int start_col, int goal_row,
         int goal_col, vector<vector<int>>& maze, unordered_map<pair<int,int>,
         bool, PairHash>& visited){
    Stack<pair<int,int>> path;
    path.push(make_pair(start_row,start_col));
    visited[make_pair(start_row,start_col)] = true;
    int x,y;
    x = start_row; y = start_col;
    pair<int,int> previousMove;
    while (path.top() != make_pair(goal_row,goal_col)){
        x = path.top().first;
        y = path.top().second;
        if(!wallCheckN(x,y,maze) && !wallCheckE(x,y,maze) && !wallCheckS(x,y,maze) &&
        !wallCheckW(x,y,maze) && (path.size() == 0))
            break;

        if(wallCheckN(x,y,maze) && !visitedCheck(x-1,y,visited)) {
            x--;
            path.push(make_pair(x,y));
            visited[make_pair(x,y)] = true;
            continue;

            }
            if(wallCheckE(x,y,maze)&& !visitedCheck(x,y+1,visited)){
                y++;
                path.push(make_pair(x,y));
                visited[make_pair(x,y)] = true;
                continue;
            }
            if(wallCheckS(x,y,maze)&& !visitedCheck(x+1,y,visited)){
                x++;
                path.push(make_pair(x,y));
                visited[make_pair(x,y)] = true;

                continue;
            }

            if(wallCheckW(x,y,maze)&& !visitedCheck(x,y-1,visited)){
                y--;
                path.push(make_pair(x,y));
                visited[make_pair(x,y)] = true;

                continue;
            }
            else
                path.pop();
    }

    if (path.top() == make_pair(goal_row,goal_col)){
        cout<<"path found!"<<endl;
        auto size = path.size();
        string output;
        for (int i = 0; i < size; i++){
            cout << "("<<path.top().first << ","<<path.top().second<<")"<<endl;
            path.pop();
        }
    }
    else
        cout<<endl<<"couldnt find path";

}




int main() {
        string numrows_numcols;
        getline(cin, numrows_numcols);

        istringstream iss(numrows_numcols);

        if (iss >> numrows >> numcols) {
            cout << "numrows: " << numrows << endl;
            cout << "numcols: " << numcols << endl;
        } else {
            cerr << "failed to parse" << endl;
        }

    vector<vector<int>> maze;
    string line;
    int linesToRead = numrows+1;
    while (linesToRead > 0 && getline(cin,line)){
        if(line.empty()){
            continue;
        }
        vector<int> row;
        istringstream iss(line);
        int num;
        while(iss >> num){
            row.push_back(num);
        }
        maze.push_back(row);
        linesToRead--;
    }

    const int start_row = maze[numrows][0];
    const int start_col = maze[numrows][1];
    const int goal_row = maze[numrows][2];
    const int goal_col = maze[numrows][3];
    maze.pop_back();
    Stack<pair<int,int>> path;
    unordered_map<pair<int,int>, bool, PairHash> visited;
    visited[make_pair(5,5)] = true;
    //dfs(int start_row, int start_col, int goal_row,
    //         int goal_col, vector<vector<int>>& maze, unordered_map<pair<int,int>,
    //         bool, PairHash>& visited)
    dfs(start_row,start_col,goal_row,goal_col,maze,visited);
}


