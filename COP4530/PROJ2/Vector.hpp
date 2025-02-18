#include <iostream>
#include "Vector.h"
using namespace std;
template <typename T>

Vector<T>::Vector(){
theSize = 0;
theCapacity = 0;
array = new T[theCapacity];
}

template <typename T>
Vector<T>::Vector(const Vector<T> &rhs){
theSize = rhs.theSize;
theCapacity = rhs.theCapacity;
array = new T[theCapacity];
    for (int i = 0; i<theCapacity; i++){
        array[i] = rhs.array[i];
    }
}

template <typename T>
Vector<T>::Vector(Vector<T> &&rhs){
    theSize = rhs.theSize;
    theCapacity = rhs.theCapacity;
    array = new T[theCapacity];
    for (int i = 0; i<theCapacity; i++){
        array[i] = rhs.array[i];
    }
    rhs.array = nullptr;
}

template <typename T>
Vector<T>::Vector(int num, const T& val){
    theSize = num;
    theCapacity = num;
    array = new T[theCapacity];
    for (int i = 0; i<theCapacity; i++){
        array[i] = val;
    }
}

template <typename T>
Vector<T>::Vector(const_iterator start, const_iterator end){
int size = distance(start, end)+1;
auto copy_from = start;
    theSize = size;
array = new T[size];
for (auto copy_to = 0; copy_to < size; copy_to++){
    array[copy_to] = *copy_from;
    copy_from++;
}

theCapacity = size;
}

template <typename T>
Vector<T>::~Vector(){
    delete [] array;
}

template <typename T>
void Vector<T>::doubleCapacity() {
    if (theCapacity == 0)
        theCapacity = 1;
    theCapacity = 2*theCapacity;
    T* newArray = new T[theCapacity];
    for (int i = 0; i<theSize; i++)
        newArray[i] = array[i];
    delete [] array;
    array = newArray;
}

template <typename T>
 T& Vector<T>::operator[](int index){
    if (index > theCapacity)
        throw out_of_range("out of bounds!");
    cout<<index;
    return array[index];
}

template <typename T>
const T& Vector<T>::operator[](int index) const{

    return array[index];
}

template <typename T>
const Vector<T>& Vector<T>::operator=(const Vector<T> &rhs) {
    theSize = rhs.theSize;
    theCapacity = rhs.theCapacity;
    delete [] array;
    array = new T[theCapacity];
    for (int i = 0; i<theSize; i++){
        array[i] = rhs.array[i];
    }

}

template <typename T>
Vector<T>& Vector<T>::operator=(Vector<T> &&rhs){
    theSize = rhs.theSize;
    theCapacity = rhs.theCapacity;
    array = new T[theCapacity];
    for (int i = 0; i<theCapacity; i++){
        array[i] = rhs.array[i];
    }
    rhs.array = nullptr;
}

template <typename T>
T& Vector<T>::at(int loc ){
    if (loc >= theSize || loc < 0)
        throw out_of_range("out of bounds!");;
    return array[loc];
}

template <typename T>
const T& Vector<T>::at(int loc ) const{
    if (loc >= theSize || loc < 0)
        throw out_of_range("out of bounds!");;
    return array[loc];
}

template <typename T>
T& Vector<T>::front(){
    return array[0];
}

template <typename T>
const T& Vector<T>::front() const{
    return array[0];
}

template <typename T>
T& Vector<T>::back(){
    return array[theSize-1];
}

template <typename T>
const T& Vector<T>::back() const{
    return array[theSize-1];
}

template <typename T>
int Vector<T>::size() const {
    return theSize;
}

template <typename T>
int Vector<T>::capacity() const {
    return theCapacity;
}

template <typename T>
bool Vector<T>::empty() const{
    if (theSize == 0)
        return true;
    return false;
}

template <typename T>
void Vector<T>::clear(){
    delete [] array;
    theCapacity = 0;
    theSize = 0;
    array = new T[theCapacity];
}

template <typename T>
void Vector<T>::push_back(const T & val){
    if(theSize == theCapacity)
        doubleCapacity();
    array[theSize] = val;
    theSize++;
}

template <typename T>
void Vector<T>::pop_back(){
    if (theSize > 0){
        --theSize;
    }
    else
        cout<<"already empty"<<endl;
}

template <typename T>
void Vector<T>::resize(int num, T val){
    bool newspaces = false;
    int temp = theSize;
    if (num > theSize)
        newspaces = true;
    if (num > theCapacity)
        doubleCapacity();
    theSize = num;
    if (newspaces){
        for(int i = temp-1; i < theSize; i++){
            array[i] = val;
        }
    }
}

template <typename T>
void Vector<T>::reserve(int newCapacity) {
    if (newCapacity > theCapacity){
        theCapacity = newCapacity;
        T* newArray = new T[theCapacity];
        for (int i = 0; i<theSize; i++)
            newArray[i] = array[i];
        delete [] array;
        array = newArray;
    }
}

template <typename T>
void Vector<T>::print(std::ostream& os, char ofc) const {
    for (int i = 0; i < theSize; i++) {
        os << array[i] << ofc;
    }
}

template <typename T>
T* Vector<T>::begin() {
    T* iterator;
    iterator = &(array[0]);
    return iterator;
}

template <typename T>
const T* Vector<T>::begin() const{
    T* iterator;
    iterator = &array[0];
    return iterator;
}

template <typename T>
T* Vector<T>::end() {
    T* iterator;
    iterator = &array[theSize-1];
    return iterator;
}

template <typename T>
const T* Vector<T>::end() const{
    T* iterator;
    iterator = &array[theSize-1];
    return iterator;
}

template <typename T>
T* Vector<T>::insert(iterator itr, const T& val){
    if (theSize == theCapacity)
        reserve(theCapacity+1);
    T copyArray[theSize];
    int iterator = 0;
    for (T* i = itr+1; i != end(); i++){
        copyArray[iterator] = *i;
        iterator++;
    }
    *(itr + 1) = val;
    theSize++;
    int iterator2 = 0;

    for (T* i = itr+2; iterator2 < iterator; i++){
        *i = copyArray[iterator2];
        iterator2++;
    }
    return itr+1;
}

template <typename T>
T* Vector<T>::erase(iterator itr) {
    if (itr == end()){
        theSize--;
        return itr -1;
    }
    iterator copy_from = itr;
    for ( auto copy_to = itr; copy_from != end(); copy_from++ ){
        *copy_to = *copy_from;
        copy_to++;
    }
    theSize--;
    return itr;
}

template <typename T>
T* Vector<T>::erase(iterator start, iterator end) {
// problem is here
    iterator copy_from = end;
    int count  = end - start;

    auto vecEnd = this -> end();
    for (auto copy_to = start; copy_to != end && copy_from != vecEnd; copy_to++){

        copy_to =copy_from++;
    }
    theSize -=(end - start);
    return &array[theSize-1];


}
template <typename T>
bool operator==(const Vector<T> & lhs, const Vector<T> &rhs){
    if (lhs.size() != rhs.size())
        return false;
    for (int i = 0; i< lhs.size(); i++){
        if (lhs[i] != rhs[i]) {
            cout<<endl<<lhs[i]<<' '<<rhs[i];
            return false;
        }
    }
    return true;
}

template <typename T>
bool operator!=(const Vector<T> & lhs, const Vector<T> &rhs){
    if (lhs.size() != rhs.size())
        return true;
    for (int i = 0; i< lhs.size(); i++){
        if (lhs[i] != rhs[i])
            return true;
    }
    return false;
}


template <typename T>
std::ostream & operator<<(std::ostream &os, const Vector<T> &v){
    int maxSize = v.size()-1;
    for (int i = 0; i < maxSize; i++) {
        os << v[i] << " ";
    }
    return os;
}