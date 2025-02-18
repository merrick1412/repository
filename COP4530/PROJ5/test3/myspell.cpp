#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <utility>
#include <sstream>
#include <cctype>
#include "hashtable.h"
#include <unordered_map>
using namespace std;
void menu(HashTable<string>&);
bool comparePairs(const pair<string,int>&, const pair<string,int>&);

int main(int arg, char* argv[]){
    if (arg == 1) {
        HashTable<string> testtable;
        menu(testtable);
    }
else{
    const char* dictionaryFile = argv[1];
    const char* checkFile = argv[2];
    const char* outputFile = argv[3];
        HashTable<string> dictionary;

    ifstream dictionaryStream(dictionaryFile); //loading dictionary
    if (!dictionaryStream.is_open()){
            cerr << "couldnt open dict file";
            return 1;
    }
    string word;
    while (getline(dictionaryStream, word)){
            dictionary.insert(word);
    }
    dictionaryStream.close();

    unordered_map<string,int> wordRanks; //loading word ranks

    const char* wordRankFile = "wordrank.txt";
    ifstream wordRankFileStream(wordRankFile);
    if(!wordRankFileStream.is_open()){
        cerr << "couldnt open word rank file";
        return 1;
    }

    string word1;
    int rank;
    while (wordRankFileStream >> word >> rank){
        pair<string,int> toInsert;
        toInsert.first = word;
        toInsert.second = rank;
        wordRanks.insert(toInsert);
    }
    wordRankFileStream.close();

    ifstream checkFileStream(checkFile);
    if (!checkFileStream.is_open()){
        cerr <<"couldnt open check file";
        return 1;
    }

    vector<pair<string,bool>> checkWords;
    string word2;
    string stringWithoutPunctuation;
    while (checkFileStream >> word2){
        stringWithoutPunctuation = "";
        for (char &c : word2){
            c = tolower(c);
            if (!ispunct(c)) {
                stringWithoutPunctuation += c;
            }

        }
        word2 = stringWithoutPunctuation;
        checkWords.emplace_back(word2,false);
    }

    int amountOfMisspell = checkWords.size();
    for (auto & checkWord : checkWords){
        if (dictionary.contains(checkWord.first)) {
            checkWord.second = true;
            amountOfMisspell--;
        }
    }

    vector<vector<string>> misspelledWords;
    misspelledWords.resize(amountOfMisspell);
    int count = 0;
    for (auto & checkWord : checkWords){
        if (!checkWord.second){
            misspelledWords[count].push_back(checkWord.first);
            count++;
        }
    }
    string misspelledWord;
    for (auto & i : misspelledWords){
        misspelledWord = i[0];
        for (size_t x = 0; x< misspelledWord.length(); ++x){
            char originalC = misspelledWord[x];
            for (char replacement = 'a'; replacement <= 'z'; ++replacement){
                string modifiedWord = misspelledWord;
                modifiedWord[x] = replacement;
                if (dictionary.contains(modifiedWord)){
                    i.push_back(modifiedWord);
                }
            }
            misspelledWord[x] = originalC;
        }
    }

vector<vector<pair<string,int>>> rankedWords;
vector<vector<string>> unrankedWords;

 //keeps track of how many words got added to the lists
rankedWords.resize(misspelledWords.size());
unrankedWords.resize(misspelledWords.size());
    for (size_t i = 0; i < misspelledWords.size(); i++){

        for (size_t x = 1; x < misspelledWords[i].size(); x++){
            if (wordRanks.find(misspelledWords[i][x]) != wordRanks.end()){
                auto it = wordRanks.find(misspelledWords[i][x]);
                rankedWords[i].emplace_back(it->first, it->second);

            }
            else{ unrankedWords[i].push_back(misspelledWords[i][x]);

            }
        }

    }

    for (auto & rankedWord : rankedWords) {
        sort(rankedWord.begin(), rankedWord.end(), comparePairs);
    }
    vector<vector<string>> suggestionsList;
    suggestionsList.resize(rankedWords.size());
    vector<string> userChoices;
    userChoices.resize(misspelledWords.size());
    for (int i = 0; i < rankedWords.size(); i++){
        for (size_t x = 0; x < rankedWords[i].size(); x++){
            suggestionsList[i].push_back(rankedWords[i][x].first);
        }
        for (size_t x = 0; x < unrankedWords[i].size(); x++){
            suggestionsList[i].push_back(unrankedWords[i][x]);
        }
    }

    for (int i = 0; i < suggestionsList.size(); i++){
        int choice;
        cout<<endl<<"==========================="<<endl;
        string allCaps = misspelledWords[i][0];
        transform(allCaps.begin(),allCaps.end(), allCaps.begin(), ::toupper);

        cout<<"Misspelled word: "<<allCaps<<endl;
        if (suggestionsList[i].size() > 10){
            for (int x = 0; x< 10; x++){
                cout<<"("<<x<<"): "<<suggestionsList[i][x]<<endl;
            }
        }
        else{
            for (int x = 0; x< suggestionsList[i].size(); x++){
                cout<<"("<<x<<"): "<<suggestionsList[i][x]<<endl;
            }
        }
        cout<<endl<<"==========================="<<endl;
        cout<<"Which suggestion would you like to make?: ";
        cin >> choice;
        userChoices.push_back(suggestionsList[i][choice]);


    }
        unordered_map<string,string> corrections;
    vector<string> origMisspelledWords;


    ifstream inputFileStream2(checkFile);
    ofstream outputFileStream(outputFile);
    string line;
        while (getline(inputFileStream2, line)){
            istringstream iss(line);
            string word;
            while(iss >> word){
                auto it = find(origMisspelledWords.begin(), origMisspelledWords.end(), word);
                if (it != origMisspelledWords.end()){
                    size_t index = std::distance(origMisspelledWords.begin(), it);
                    outputFileStream << userChoices[index] << " ";
                } else{
                    outputFileStream << word << " ";
                }
            }
            outputFileStream << "\n";
        }
        checkFileStream.close();
        outputFileStream.close();



    //for (int i = 0; )
// for loop here with outer being how many suggestions per word, which would be misspelled[i].size, make sure to skip original
// inner printing out the suggestion words and allowing user to make a selection. 10 if 10+, misspelled[i].size suggestions if less
//store the user suggestions in a new vector, need to figure out how to output correctly to file


}

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

bool comparePairs(const pair<string,int>& lhs, const pair<string,int>& rhs){
    return lhs.second < rhs.second;
}