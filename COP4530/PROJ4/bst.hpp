//
// Created by merrick on 11/6/2023.
//

#ifndef PROJECT4_4530_BST_HPP
#define PROJECT4_4530_BST_HPP
#include "bst.h"
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <queue>
using namespace cop4530;

bool isNumeric(const std::string& str) {
    for (char c : str) {
        if (!std::isdigit(c)) {
            return false;
        }
    }
    return true;
}

template <typename T>
typename BST<T>::BSTNode* BST<T>::copyTree(const  BSTNode* originalNode){
    if (originalNode == nullptr) {
        return nullptr;
    }

    auto* newNode = new typename BST<T>::BSTNode;
    newNode->element = originalNode->element;
    newNode->searchcount = originalNode->searchcount;

    newNode->left = copyTree(originalNode->left);
    newNode->right = copyTree(originalNode->right);

    return newNode; // new root
}
template <typename T>
void BST<T>::deleteNodes(typename BST<T>::BSTNode*& node){
    if (node){
        deleteNodes(node->left);
        deleteNodes(node->right);

        delete node;
        node = nullptr;  // After deletion, set the node pointer to null
    }
}

template <typename T>
BST<T>::BST(int th){
    threshold = th;
    root = nullptr;
}

template <typename T>
BST<T>::BST(const std::string input, int th){
    threshold = th;
    std::istringstream iss(input);
    root = nullptr;
    T value;
    while (iss >> value){
        insert(value);
    }
}

template <typename T>
void BST<T>::insertNode(BSTNode*& current, const T& value) {
    if (current == nullptr) {
        current = new BSTNode{value, 0, nullptr, nullptr, nullptr};
        tree.push_back(*current);
    } else if (value < current->element) {
        insertNode(current->left, value);
        if (current->left == nullptr)
            current->left = &tree.back();
    } else if (value > current->element) {
        insertNode(current->right, value);
        if (current->right == nullptr)
            current->right = &tree.back();
    }
}

template <typename T>
BST<T>::BST(const BST& b){
    threshold = b.threshold;
    root = copyTree(b.root);
}

template <typename T>
BST<T>::BST(BST&& b){
    threshold = b.threshold;
    root = b.root;
    b.root = nullptr;
}
template <typename T>
BST<T>::~BST(){
deleteNodes(root);
root = nullptr;
}

template <typename T>
void BST<T>::buildFromInputString(const std::string input) {
    if (root != nullptr){
        makeEmpty(root);
    }
    root = nullptr;
    std::istringstream iss(input);
    T value;
    while (iss >> value){
        insert(value);
    }
}

template <typename T>
bool BST<T>::operator!=(const BST<T>& other) const {
    return !(*this == other);
}

template <typename T>
bool BST<T>::operator==(const BST<T>& other) const {

    if (root == nullptr && other.root == nullptr)
        return true;

    if (root != nullptr && other.root != nullptr)
        return isEqual(root, other.root);


    return false;
}

template <typename T>
bool BST<T>::isEqual(BSTNode* t1, BSTNode* t2) const {
    if (t1 == nullptr && t2 == nullptr)
        return true;

    if (t1 == nullptr || t2 == nullptr)
        return false;

    // Compare elements and recursively check left and right subtrees
    return (t1->element == t2->element) &&
           isEqual(t1->left, t2->left) &&
           isEqual(t1->right, t2->right);
}

template <typename T>
const BST<T>& BST<T>::operator=(const BST<T>& b){
    if (this != &b){
        makeEmpty(root);
    }
    root = clone(b.root);
    return *this;
}

template <typename T>
const BST<T>& BST<T>::operator=(BST<T>&& b){
    if (this != &b) {
        makeEmpty(root);  // Clear the existing tree
        root = b.root;    // Move the pointer to the root of the source tree
        b.root = nullptr; // Reset the source tree's root pointer
    }
    return *this;
}

template <typename T>
void BST<T>::printInOrder() const{
    printInOrder(root);
}

template <typename T>
void BST<T>::printInOrder(const BSTNode *t) const{
    if (t != nullptr){
        printInOrder(t->left);
        std::cout << t->element << " ";
        printInOrder(t->right);
    } else
        return;
}

template <typename T>
void BST<T>::printLevelOrder() const{
    printLevelOrder(root);
}

template <typename T>
void BST<T>::printLevelOrder(BSTNode *t) const{
    if (root == nullptr) return;
    std::queue<BSTNode*> nodeQueue;
    nodeQueue.push(root);
    while (!nodeQueue.empty()){
        BSTNode* current = nodeQueue.front();
        std::cout << current->element <<" ";
        nodeQueue.pop();
        if(current->left != nullptr){
            nodeQueue.push(current->left);
        }
        if(current->right != nullptr){
            nodeQueue.push(current->right);
        }
    }
}

template <typename T>
bool BST<T>::empty() {
 if(root == nullptr) {
     return true;
 }
 else
     return false;
}
template <typename T>
int BST<T>::numOfNodes() const {
    return numOfNodes(root);
}

template <typename T>
int BST<T>::numOfNodes(BSTNode *t) const {
    if (t == nullptr)
        return 0;
    return 1+ numOfNodes(t->left) + numOfNodes(t->right);
}

template <typename T>
int BST<T>::height() const {
    return height(root);
}

template <typename T>
int BST<T>::height(BSTNode *t) const {
    if (t == nullptr)
        return -1;
    int leftheight = height(t->left);
    int rightheight = height(t->right);
    int maxheight;
    if (leftheight > rightheight)
        maxheight = leftheight;
    else
        maxheight = rightheight;
    return 1 + maxheight;
}

template <typename T>
void BST<T>::makeEmpty() {
    makeEmpty(root);
}

template <typename T>
void BST<T>::makeEmpty(BSTNode *&t) {
    if (t != nullptr){
        makeEmpty(t->right);
        makeEmpty(t->left);
        delete t;
    }
}

template <typename T>
void BST<T>::insert(const T& v){
    insert(v, root);
}

template <typename T>
void BST<T>::insert(T&& v){
    insert(v, root);
}

template <typename T>
void BST<T>::insert(const T& v, BSTNode* &t){
    if (t == nullptr) {
        t = new BSTNode{ 0,v, nullptr, nullptr, nullptr,};
    }
    else {
        if (v < t->element) {
            if (t->left == nullptr) {
                t->left = new BSTNode{.searchcount = 0, .element = v, .right = nullptr, .left = nullptr, .parent = t};
            } else
                insert(v, t->left);
        } else if (v > t->element) {
            if (t->right == nullptr) {
                t->right = new BSTNode{.searchcount = 0, .element = v, .right = nullptr, .left = nullptr, .parent = t};
            } else {
                insert(v, t->right);
            }
        } else {
            t->searchcount++;
            if (t->searchcount % threshold == 0 && t->parent != nullptr){
                rotate(t,t->parent);
            }
        }
    }
}

template <typename T>
void BST<T>::insert( T&& v, BSTNode* &t){
    if (t == nullptr) {
        t = new BSTNode{v, nullptr, nullptr, nullptr, 0};
    }
    if(contains(v))
        return;
    else if(v < t->element){
        insert(std::move(v), t->left);
    }
    else if(v > t->element){
        insert(std::move(v), t->right);
    }
}

template <typename T>
void BST<T>::remove(const T& v){
    remove(v,root);
}

template <typename T>
typename BST<T>::BSTNode* BST<T>::findMin(BSTNode* node) const{
    if (node == nullptr){
        return nullptr;
    }
    BSTNode* current = node;
    while (current->left != nullptr){
        current = current->left;
    }
    return current;
}

template <typename T>
void BST<T>::remove(const T& v, BSTNode* &t){
    if (t == nullptr){
        return;
    }

    if (v < t->element){
        remove(v, t->left);
    } else if(v > t->element){
        remove(v, t->right);
    } else{
        if (t->left != nullptr && t->right != nullptr){
            BSTNode* minRight = findMin(t->right);
            t->element = minRight->element;
            remove(minRight->element, t->right);
        } else{
            BSTNode* temp = t;
            if (t->left != nullptr){
                t = t->left;
            } else if(t->right != nullptr){
                t = t->right;
            } else {
                t = nullptr;
            }
            delete temp;
        }
    }
}

template <typename T>
bool BST<T>::contains(const T &v) {
    return contains(v,root);
}

template <typename T>
bool BST<T>::contains(const T &v, BSTNode *&t) {
    if(t == nullptr){
        return false;
    }
    else if(v < t->element){
        return contains(v, t->left);
    }
    else if(v > t->element){
        return contains(v, t->right);
    } else {
        t->searchcount++;
        if (t->searchcount % threshold == 0 && t->parent != nullptr){
            rotate(t,t->parent);
        }
        return true;
    }
}

template <typename T>
typename BST<T>::BSTNode* BST<T>::clone(BSTNode *t) const {
    if (t == nullptr) {
        return nullptr;
    }

    BSTNode* newNode = new BSTNode;
    newNode->element = t->element;
    newNode->searchcount = t->searchcount;

    newNode->left = clone(t->left);
    newNode->right = clone(t->right);

    return newNode;
}

template <typename T>
void BST<T>::rotate(BSTNode* t, BSTNode* p) {
    if (p->left == t) {
        p->left = t->right;
        if (t->right)
            t->right->parent = p;
        t->right = p;
    } else {
        p->right = t->left;
        if (t->left)
            t->left->parent = p;
        t->left = p;
    }
    t->parent = p->parent;
    p->parent = t;

    if (t->parent) {
        if (t->parent->left == p)
            t->parent->left = t;
        else
            t->parent->right = t;
    } else {
        root = t;
    }
}
#endif //PROJECT4_4530_BST_HPP
