# Trees

A tree is similar to a linked list in that each node points to the next node. The difference is that a node can point to more than one node. The following tree types will be discussed:
- Binary Trees
- Binary Search Trees
- Balanced Binary Search Trees

## Binary Trees
![Image of Binary Tree](images/binary-tree-illustration.png)

A Binary Tree is a tree data structure that consists of nodes with a parent-child relationship. The top node of a tree is called the **root**. Each node following the root has a parent and zero or more children. A node that does not have any children are called **external nodes** or **leafs**.

**Subtrees** are common terminology as well. A subtree is any node in the tree and its descendants. The node with the value of 13 is a subtree with descendants 12 and 14.

A node can have **ancestors** or **descendants**. For instance, an ancestor of a node can be its parent, grandparent, great-grandparent, and so on. Similarly, a descendant of a node can be its child, grandchild, great-grandchild, and so on. For example, looking at the binary tree above 13 is the child of 15 *and* the grandchild of 11. In other words, 11 and 15 are the ancestors of 11.

## Binary Search Trees
![Image of Binary Search Tree](images/binary-search-tree-illustration.jpg)

A **Binary Search Tree** (BST) follows a process to organize nodes. Data is placed into the tree by comparing the data with the value in the parent node. If the data being added is less than the parent node, then it is placed in the left subtree. If the data being added is greater than the parent node, then it is placed in the right subtree. 

In the example above, the process of inserting 3 is as follows:
1. Start at the root and compare the values. Since 3 is smaller than 5, 3 will be placed in the left subtree.
2. Compare 3 with the following node which is 2. Since 3 is greater than 2, 3 will be placed to the right.
3. Lastly, compare 3 to the following node, 4. 4 is greater than 3; therefore, 3 will be placed to the left. Since 4 does not have any children, the seach stops and 3 will be added to the list.

**Activity**: Find the correct spot to put a node with the value of **8**.

## Balanced Binary Search Trees
![Image of Balanced Binary Search Tree](images/balanced-tree-illustration.png)

A **Balanced Binary Search Tree** (Balanced BST) is a BST where the *height* between any two subtrees is not dramatically different. The **height** of a tree is the longest downward path from its root to any reachable leaf. For instance, the image above illustrates an **unbalanced** BST on the left, while the **balanced** BST is on the right. For the unbalanced BST, the *height*, or the longest path, from the root node to the furthest leaf is 5. On the other hand, the balanced BST has a height of 2. 

The height between the root node and any of the leafs in the balanced BST is the same, being 2. On the other hand, the height between the left and right subtree of the unbalanced binary tree is completely different with the height of the right subtree being 0. In order to balance the tree, there are many different algorithms you can implement. 



