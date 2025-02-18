//
// Created by merrick on 10/12/2023.
//
#ifndef PROJECT3_4530_STACK_H
#define PROJECT3_4530_STACK_H
#include <vector>

namespace cop4530 {
    template<typename T>
    class Stack {
    public:
        Stack();

        ~Stack();

        Stack(const Stack &rhs); //copy
        Stack(Stack &&rhs); //move
        Stack &operator=(const Stack &rhs); //copy overload
        Stack &operator=(Stack &&rhs) noexcept ; //move overload
        bool empty() const;

        T &top();

        const T &top() const;

        void pop();

        void push(const T &val);

        void push(T &&val); //move push
        int size();

    private:
        int Size;
        std::vector<T> array;
    };
}


#endif //PROJECT3_4530_STACK_H
