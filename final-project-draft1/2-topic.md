# Linked Lists

A Linked List is a useful data structure that connects pieces of data that are *not necessarily* next to each other in memory. 

## Nodes
A linked list is made up of elements that are called **nodes**. A node consists of the **value** it will hold as well as the **pointer** which points to the next node in the linked list. For instance, a node that holds a value of *3* will point to a node that has a value of *6*.

## Singly Linked Lists
A Linked List where the pointers point in one direction is known as a **singly linked list**.

To better understand, here is a simple illustration:

![Image of Singly Linked List](images/linked-list-illustration.png)

### Knowing the Terms:
- **Head**: The head is the first node of the linked list.
- **Tail**: The tail is the last node of the linked list. The pointer for this node will point to *null*.

## Doubly Linked Lists
Most linked lists are *bi-directional*, meaning that it functions in two directions. Instead of one, a node will have to pointers named **next** and **previous**: 

- **Next**: The next pointer will point to the next node. These pointers will be pointing to the right.
- **Previous**: The previous (referred to as *prev*) pointer will point to the previous node. These pointers will be pointing to the left.

To better understand, here is a simple illustration:

![Image of Doubly Linked List](images/doubly-linked-list-illustration.png)

### Things to Note
Since the head will have two pointers, the prev will point to *null*. Both the head and tail will point to null.

## Inserting into a Linked List
Inserting a new node into a linked list involves moving the pointers 
