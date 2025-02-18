//
// Created by merrick on 10/12/2023.
//
#ifndef PROJECT3_4530_STACK_HPP
#define PROJECT3_4530_STACK_HPP
#include "Stack.h"
#include <vector>
#include <iostream>

using namespace std;
using namespace cop4530;


template <typename T>
Stack<T>::Stack(){
Size = 0;
}

template <typename T>
Stack<T>::~Stack()= default;

template <typename T>
Stack<T>::Stack(Stack &&rhs){
    Size = rhs.Size;
    array = move(rhs.array);
    rhs.Size = 0;

}

template <typename T>
Stack<T>::Stack(const Stack &rhs){
    Size = rhs.Size;
    array = rhs.array;
}

template <typename T>
Stack<T>& Stack<T>::operator=(Stack<T> &&rhs)  noexcept {
    Size = rhs.Size;
    array = move(rhs.array);
    rhs.Size = 0;
}

template <typename T>
Stack<T>& Stack<T>::operator=(const Stack<T> &rhs) {
    array = rhs.array;

    Size = rhs.Size;

    return *this;




}

template <typename T>
bool Stack<T>::empty() const {
if (array.empty())
    return true;
return false;
}

template <typename T>
T& Stack<T>::top() {
    return array.back();
}

template <typename T>
const T& Stack<T>::top() const{
    return array.back();
}

template <typename T>
void Stack<T>::pop() {
    if(Size != 0) {
        array.pop_back();
        Size--;
    }
}

template <typename T>
void Stack<T>::push(const T &val) {
    array.push_back(val);
    Size++;
}

template <typename T>
void Stack<T>::push( T &&val) {
    Size++;
    array.push_back(move(val));
}

template <typename T>
int Stack<T>::size(){
    return Size;
}


#endif //PROJECT3_4530_STACK_HPP
