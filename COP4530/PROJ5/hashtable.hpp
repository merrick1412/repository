
#ifndef HASHTABLE_HPP
#define HASHTABLE_HPP
#include <vector>
#include <algorithm>
#include <iostream>
#include <list>
#include "hashtable.h"
#include <functional>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_set>
using namespace cop4530;
using namespace std;
template <typename T>
HashTable<T>::HashTable(size_t size) {
    lists.resize(prime_below(size));
    currentSize = 0;
}

template <typename T>
HashTable<T>::~HashTable() {
    for (auto i = 0; i<lists.size(); i++){
        lists[i].clear();
    }
    lists.clear();
}

template <typename T>
bool HashTable<T>::contains(const T &x) const{
    auto & selectedList = lists[myhash(x)];
    return find(begin(selectedList), end(selectedList), x) != end(selectedList);
}

template <typename T>
bool HashTable<T>::insert(const T & x){
    auto & selectedList = lists[myhash(x)];
    if (contains(x)){
        return false;
    }

    selectedList.push_back(x);
    currentSize++;

    if (currentSize > lists.size()){
        rehash();
    }
return true;
}

template <typename T>
bool HashTable<T>::insert( T && x){
    auto & selectedList = lists[myhash(x)];
    if (contains(x)){
        return false;
    }

    selectedList.push_back(move(x));
    currentSize++;

    if (currentSize > lists.size()){
        rehash();
    }
    return true;
}

template <typename T>
bool HashTable<T>::remove(const T &x) {
    if (!contains(x))
        return false;
    auto & selectedList = lists[myhash(x)];
    auto itr = find(begin(selectedList), end(selectedList), x);
    if (itr == end(selectedList))
        return false;
    selectedList.erase(itr);
    --currentSize;
    return true;
}

template <typename T>
void HashTable<T>::clear() {
    makeEmpty();
    currentSize = 0;
}

template <typename T>
void HashTable<T>::makeEmpty() {
    for (auto & thisList : lists){
        thisList.clear();
    }
}

template <typename T>
bool HashTable<T>::load(const char *filename) {
    ifstream file(filename);
    if (!file.is_open()){
        cerr << "error opening " << filename <<endl;
        return false;
    }
    string line;
    while (getline(file, line)){
        istringstream iss(line);
        T value;
        if (!(iss >> value)){
            cerr << "couldnt parse "<<line<<endl;
            continue;
        }
        insert(value);
    }
    file.close();
    return true;
}

template <typename T>
void HashTable<T>::dump() const {
    if(lists.size() == 0){
        cout<<"empty"<<endl;
    }
    for (auto i = 0; i < lists.size(); i++){
        cout<<"v["<<i<<"]:\t";
            for(auto x = 0; x< lists[i].size(); x++){
                cout<<lists[i][x]<<"\t";
            }
        cout<<endl;
    }
}

template <typename T>
bool HashTable<T>::write_to_file(const char *filename) const {
    ofstream file(filename);
    if (!file.is_open()){
        cerr <<"couldnt open file " << filename<<endl;
        return false;
    }
    for (auto i = 0; i < lists.size(); i++){
        for(auto x = 0; x< lists[i].size(); x++){
            file << lists[i][x] << '\n';
        }
    }
    file.close();
    return true;
}

template <typename T>
size_t HashTable<T>::myhash(const T &x) const{
    static hash<T> hf;
    return hf(x) % lists.size(); //from lecture
}

template <typename T>
size_t HashTable<T>::getSize() const {
return currentSize;
}

template <typename T>
void HashTable<T>::rehash() {
    vector<vector<T>> oldlists = lists;

    lists.resize(prime_below(2 * lists.size()));
    for (auto & thisList : lists)
        thisList.clear();

    currentSize = 0;
    for (auto & thisList : oldlists)
        for (auto & x : thisList)
            insert(move(x));
}

template <typename T>
unsigned long HashTable<T>::prime_below (unsigned long n)
{
  if (n > max_prime)
    {
      std::cerr << "** input too large for prime_below()\n";
      return 0;
    }
  if (n == max_prime)
    {
      return max_prime;
    }
  if (n <= 1)
    {
		std::cerr << "** input too small \n";
      return 0;
    }

  // now: 2 <= n < max_prime
  std::vector <long> v (n+1);
  setPrimes(v);
  while (n > 2)
    {
      if (v[n] == 1)
	return n;
      --n;
    }

  return 2;
}

template <typename T>
void HashTable<T>::setPrimes(vector<long>& vprimes)
{
  int i = 0;
  int j = 0;

  vprimes[0] = 0;
  vprimes[1] = 0;
  int n = vprimes.capacity();

  for (i = 2; i < n; ++i)
    vprimes[i] = 1;

  for( i = 2; i*i < n; ++i)
    {
      if (vprimes[i] == 1)
        for(j = i + i ; j < n; j += i)
          vprimes[j] = 0;
    }
}

#endif