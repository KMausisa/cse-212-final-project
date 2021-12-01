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
There are three ways to insert a new node into a linked list: Inserting a new head, inserting a new tail, and inserting in between the head and the tail (or at the middle). Here are the processes for each one:

### Inserting at the head
1. Create a new node.
2. Set the "next" of the new node to the current head.
3. Set the "prev" of the current head to the new node.
4. Set the head equal to the new node.

The four steps can be implemented into four lines of code like so:

```python
new_node = Node(value)      # Step 1
new_node.next = self.head   # Step 2
self.head.prev = new_node   # Step 3
self.head = new_node        # Step 4
```

### Inserting at the Tail
1. Create a new node.
2. Set the "prev" of the new node to the current tail.
3. Set the "next" of the current tail to the new node.
4. Set the tail equal to the new node. 

The four steps can be implemented into four lines of code like so:

```python
new_node = Node(value)      # Step 1
new_node.prev = self.tail   # Step 2
self.tail.next = new_node   # Step 3
self.tail = new_node        # Step 4    
```

There is a **special case** that can occur when inserting the head or tail. If the linked list is empty, the only step is to assign the new node to the head *and* tail. You can check to see if the linked list is empty if the head is equal to None.

### Inserting in the Middle
When inserting somewhere in the middle of the linked list, we should know the node that we will be inserting after. This node will be called the current node. Knowing this, we can adjust the pointers of the current node and the following node to point to the new node that is being inserted. Here are the steps:

1. Create a new node.
2. Set the "prev" of the new node to the current node.
3. Set the "next" of the new node to the next node after current.
4. Set the "prev" of the "next" node after current to the new node.
5. Set the next of the current node to the new node.

These five steps can be implemented into five lines of code like so:

```python
new_node = Node(value)          # Step 1
new_node.prev = current         # Step 2
new_node.next = current.next    # Step 3
current.next.prev = new_node    # Step 4
current.next = new_node         # Step 5
```
