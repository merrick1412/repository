
#ifndef HASHTABLE_H
#define HASHTABLE_H
#include <vector>
#include <algorithm>
#include <iostream>
#include <list>
using namespace std;
namespace cop4530 {
static const unsigned int default_capacity = 11;
static const unsigned int max_prime = 1301081;
template<typename T>
class HashTable {
public:
    HashTable(size_t size = 101);
    ~HashTable();
    bool contains(const T &x) const;
    bool insert(const T & x);
    bool insert (T &&x);
    bool remove(const T &x);
    void clear();
    bool load(const char *filename);
    void dump() const;
    bool write_to_file(const char *filename) const;
    size_t getSize() const;
private:
    vector<vector<T>> lists;
    unsigned long prime_below (unsigned long);
    size_t currentSize;
    size_t myhash(const T &x) const;
    void makeEmpty();
    void rehash();
    void setPrimes(vector<long>&);
};
}
#include "hashtable.hpp"
#endif