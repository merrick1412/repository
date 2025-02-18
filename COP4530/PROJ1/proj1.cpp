#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;
bool isIdentifier(const char& word);
bool swapCheck (int,int);
string makeLowercase(const string&);
void Sort(vector<pair<string, int>>& input);
void charSort(vector<pair<char,int>>& input);



int main() {

    int lineCount = 0;
    int wordCount = 0;
    int charCount = 0;
    string input;
    vector<char> inputVector;
    vector<string> Identifiers;
    vector<string> Numbers;
    char ch;
    while (cin.get(ch)){
        inputVector.push_back(ch);

    }
    string fullInput(inputVector.begin(), inputVector.end()); //makes a string from char vector

    for (int i = 0; i < inputVector.size(); i++){
        if (inputVector[i] == '\n')
            lineCount++;
    }


    istringstream lineparse(fullInput);
    string word;


    while (lineparse >> word){ //processes the raw input into lines, then into numbers and identifiers

        vector<char> wordVec;

        for (int i = 0; i<word.size(); i++)
            wordVec.push_back(word[i]);

        if (isdigit(wordVec[0])) {
            wordCount++;

            for (int x = 0; x < word.size(); x++){
                if (!isdigit(wordVec[x]) && isdigit(wordVec[x+1])) {
                    wordCount++;

                }
            }
            Numbers.push_back(word);
        }

        if (isIdentifier(wordVec[0])) {
            wordCount++;

            Identifiers.push_back(word);
        }

    }



    for (int i = 0; i < inputVector.size()-1; i++){

        charCount++;
    }

    cout<<"lines:"<<lineCount<<endl;
    cout<<"words:"<<wordCount<<endl;
    cout<<"chars:"<<charCount<<endl;

    vector<pair<char, int>> charStats; //matches characters and finds their frequency
    for (int i = 0; i < inputVector.size(); i++ ){
        bool foundmatch = false;
        bool firstrun = false;
        if (charStats.size() == 0) {
            charStats.push_back(pair<char , int> {inputVector[0], 1} );

            firstrun = true;
        }
        for (int x = 0; x < charStats.size(); x++){
            if (firstrun)
                break;
            if (inputVector[i] == charStats[x].first && !firstrun) {
                charStats[x].second++;
                foundmatch = true;

                }

            }
        if (!foundmatch && !firstrun){
            charStats.push_back(pair<char,int> {inputVector[i], 1});
        }
    }
    for (string& rawStr : Identifiers){
        transform(rawStr.begin(), rawStr.end(), rawStr.begin(), ::towlower); //turns all strings to lowercase
    }
    vector<pair<string, int>> identifierStats; //matches ident and finds their frequency
    for (int i = 0; i < Identifiers.size(); i++ ){
        bool foundmatch = false;
        bool firstrun = false;

        if (identifierStats.size() == 0) {
            identifierStats.push_back(pair<string , int> {Identifiers[0], 1} );

            firstrun = true;
        }
        for (int x = 0; x < identifierStats.size(); x++){

            if (makeLowercase(Identifiers[i]) == makeLowercase(identifierStats[x].first) && !firstrun) {
                identifierStats[x].second++;
                foundmatch = true;

            }

        }
        if (!foundmatch && !firstrun){
            identifierStats.push_back(pair<string,int> {Identifiers[i], 1});
        }
    }
    //number processing to avoid numbers with non digits
    for (int i = 0; i< Numbers.size();i++){
        for (int x = 0; x<Numbers[i].size();x++){
            if(!isdigit(Numbers[i][x])){


                if (x < (Numbers[i]).size()-1){
                    string beforeNonDig = Numbers[i].substr(0, x);
                    string afterNonDig = Numbers[i].substr(x+1);
                    Numbers[i]= beforeNonDig;
                    Numbers.push_back(afterNonDig);

                }
                else{
                    Numbers[i].pop_back();

                }
            }
        }
    }
    for (int i = 0; i<Numbers.size(); i++){
        for (int x = 0; x < Numbers[i].size(); x++){

            if (!isdigit(Numbers[i][x])){

            Numbers.erase(Numbers.begin() + i);
            }
        }
    }
    Numbers.erase(remove_if(Numbers.begin(), Numbers.end(), [](const string& element)
    {return element.empty();}), Numbers.end()); //algorithm that clears empty elements


    vector<pair<string, int>> numStats; //matches num and finds their frequency
    for (int i = 0; i < Numbers.size(); i++ ){
        bool foundmatch = false;
        bool firstrun = false;

        if (numStats.size() == 0) {
            numStats.push_back(pair<string , int> {Numbers[0], 1} );

            firstrun = true;
        }
        for (int x = 0; x < numStats.size(); x++){

            if (Numbers[i] == numStats[x].first && !firstrun) {

                numStats[x].second++;
                foundmatch = true;

            }

        }
        if (!foundmatch && !firstrun){

            numStats.push_back(pair<string,int> {Numbers[i], 1});
        }
    }


    charSort(charStats); //sorts the chars in descending order
    //sort(identifierStats.begin(), identifierStats.end(), identCompare); //sorts the idents in descending
    //sort(numStats.begin(), numStats.end(), numCompare); //sorts the nums in descending
    Sort(identifierStats);
    Sort(numStats);



    cout<<"\nThere were: "<<charStats.size()<<" unique characters\nThe top 5 most used characters are:"<<endl;
    if (charStats.size() <= 5){
        for ( int i = 0; i<charStats.size(); i++){
            if (charStats[i].first == '\t') {
                cout << "\\t\tFrequency: " << charStats[i].second << endl;
                continue;
            }
            if (charStats[i].first == '\n') {
                cout << "\\n\tFrequency: " << charStats[i].second << endl;
                continue;
            }

            else
                cout<<charStats[i].first<<"\tFrequency: "<<charStats[i].second<<endl;

            }
    }
    else{
        for ( int i = 0; i<5; i++){
            if (charStats[i].first == '\t') {
                cout << "\\t\tFrequency: " << charStats[i].second << endl;
                continue;
            }
            if (charStats[i].first == '\n') {
                cout << "\\n\tFrequency: " << charStats[i].second << endl;
                continue;
            }

            else
                cout<<charStats[i].first<<"\tFrequency: "<<charStats[i].second<<endl;

        }
    }
    cout<<"\nThere were: "<<identifierStats.size()<<" unique identifiers.\nThe top 5 most used identifiers are:"<<endl;
    if (identifierStats.size()  <= 5){
        for ( int i = 0; i<identifierStats.size(); i++){
            cout<<identifierStats[i].first<<"\tFrequency: "<<identifierStats[i].second<<endl;
        }
    }
    else{
        for ( int i = 0; i<5; i++){
            cout<<identifierStats[i].first<<"\tFrequency: "<<identifierStats[i].second<<endl;
        }
    }
    cout<<"\nThere were: "<<numStats.size()<<" unique numbers.\nThe top 5 most used numbers are:"<<endl;
    if (numStats.size()  <= 5){
        for ( int i = 0; i<numStats.size(); i++){
            cout<<numStats[i].first<<"\tFrequency: "<<numStats[i].second<<endl;
        }
    }
    else{
        for ( int i = 0; i<5; i++){
            cout<<numStats[i].first<<"\tFrequency: "<<numStats[i].second<<endl;
        }
    }

    return 0;
}

bool isIdentifier(const char& word){
    if (isalpha(word))
        return true;
    return false;
}


string makeLowercase( const string& in){
    string out;
    transform(in.begin(), in.end(), back_inserter(out), ::tolower);
    return out;
}
bool swapCheck(int a, int b){

    return a < b;

}

void Sort(vector<pair<string, int>>& input) {
    int size = input.size();
    bool swapped;
    do {
        swapped = false;
        for (int i = 1; i < size; i++) {

             if (swapCheck(input[i - 1].second, input[i].second)){

                 int temp;
                 string stemp;
                 //swap(input[i-1].second,input[i].second);
                 temp = input[i-1].second;
                 input[i-1].second = input[i].second;
                 input[i].second = temp;
                 stemp = input[i-1].first;
                 input [i-1].first = input[i].first;
                 input[i].first = stemp;
                 //swap(input[i-1].first,input[i].first);

                swapped = true;
            }
        }
        size--;
    }while (swapped);
}
void charSort(vector<pair<char, int>>& input) {
    int size = input.size();
    bool swapped;
    do {
        swapped = false;
        for (int i = 1; i < size; i++) {
            if(input[i-1].second == input[i].second && input[i-1].first > input[i].first){
                int temp;
                char ctemp;
                temp = input[i-1].second;
                input[i-1].second = input[i].second;
                input[i].second = temp;
                ctemp = input[i-1].first;
                input [i-1].first = input[i].first;
                input[i].first = ctemp;
                //swap(input[i-1].first,input[i].first);

                swapped = true;
                continue;
            }
            if (swapCheck(input[i - 1].second, input[i].second)){

                int temp;
                char ctemp;
                //swap(input[i-1].second,input[i].second);
                temp = input[i-1].second;
                input[i-1].second = input[i].second;
                input[i].second = temp;
                ctemp = input[i-1].first;
                input [i-1].first = input[i].first;
                input[i].first = ctemp;
                //swap(input[i-1].first,input[i].first);

                swapped = true;
            }
        }
        size--;
    }while (swapped);
}