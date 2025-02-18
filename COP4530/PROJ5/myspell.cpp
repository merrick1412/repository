#include <iostream>
#include <string>
#include "hashtable.h"
using namespace std;
void menu(HashTable<string>&);

int main(){
    HashTable<string> testtable;
    menu(testtable);
};


void menu(HashTable<string>& testtable)
{
    char choice;
    do {


        cout << "\n\n";
        cout << "l - Load Dictionary From File" << endl;
        cout << "a - Add Word" << endl;
        cout << "r - Remove Word" << endl;
        cout << "c - Clear HashTable" << endl;
        cout << "f - Find Word" << endl;
        cout << "d - Dump HashTable" << endl;
        cout << "s - HashTable Size" << endl;
        cout << "w - Write to File" << endl;
        cout << "x - Exit program" << endl;
        cout << "\nEnter choice : ";
        cin >> choice;
        switch (choice) {

            case 'l': {
                string entry;
                cin.clear();
                cout << "enter the filename " << endl;
                cin >> entry;
                testtable.load(entry.c_str());
                continue;
            }
            case 'a': {
                string entry;
                cin.clear();
                cout << "enter the word you wish to add" << endl;
                cin >> entry;
                testtable.insert(entry);
                continue;
            }
            case 'r':{
                string entry;
                cin.clear();
                cout<<"enter the word you wish to remove"<<endl;
                cin>> entry;
                testtable.remove(entry);
                continue;
            }

            case 'c':{
                testtable.clear();
                cout<< "table cleared"<<endl;
                continue;
            }

            case 'f':{
                string entry;
                cin.clear();
                cout<<"enter word"<<endl;
                cin >> entry;
                if(testtable.contains(entry)){
                    cout<<"word "<<entry<<" found"<<endl;
                }
                continue;
            }

            case 'd':{
                testtable.dump();
                continue;
            }

            case 's':{
                cout<<"Size of hashtable: "<<testtable.getSize();
                continue;
            }

            case 'w':{
                string entry;
                cin.clear();
                cout << "enter the filename " << endl;
                cin >> entry;
                testtable.write_to_file(entry.c_str());
                continue;
            }

            case 'x':{
                break;
            }
            default:{
                cout<<"invalid menu choice"<<endl;
                continue;
            }
        }
    } while(choice != 'x');
}
