//
// Created by merrick on 11/5/2023.
//

#ifndef PROJECT4_4530_BST_H
#define PROJECT4_4530_BST_H
#include <vector>
#include <string>

namespace cop4530{
    template <typename T>
    class BST {
    public:

        BST(int th = 1);
        BST(const std::string input, int h = 1);
        BST(const BST&);
        BST(BST&&);
        ~BST();

        void buildFromInputString(const std::string input);
        const BST & operator=(const BST &);
        const BST & operator=(BST &&);
        bool operator!=(const BST<T>& other) const;
        bool operator==(const BST<T>& other) const;
        bool empty();

        void printInOrder() const;
        void printLevelOrder() const;
        int numOfNodes() const;
        int height() const;
        void makeEmpty();
        void insert(const T& v);
        void insert(T &&v);
        void remove(const T& v);
        bool contains(const T& v);
    private:
        struct BSTNode{
            int searchcount;
            T element;
            BSTNode* right;
            BSTNode* left;
            BSTNode* parent;
        };
        std::vector<BSTNode> tree;
        BSTNode* root;
        int threshold;
        void printInOrder(const BSTNode *t) const;
        void printLevelOrder(BSTNode *t) const;
        void makeEmpty(BSTNode* &t);
        void insert(const T& v, BSTNode *&t);
        void insert(T&& v, BSTNode *&t);
        void remove(const T& v, BSTNode *&t);
        bool contains(const T& v, BSTNode *&t);
        int numOfNodes(BSTNode *t) const;
        int height(BSTNode *t) const;
        BSTNode * clone(BSTNode *t) const;
        BSTNode* findMin(BSTNode* node) const;
        bool isEqual(BSTNode* t1, BSTNode* t2) const;
        void insertNode(BSTNode*& current, const T& value);
        void deleteNodes(BSTNode*& node);
        BSTNode* copyTree(const BSTNode* originalNode);
        void rotate(BSTNode* t, BSTNode* p);
    };
}
#include "bst.hpp"
#endif //PROJECT4_4530_BST_H
