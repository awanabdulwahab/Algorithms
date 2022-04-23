# Binary Search Tree
Before starting with deletion I just want to put some lights on what is a Binary search tree(BST), Each node in a BST
can have maximum of two nodes(left and right child).The left sub-tree of a node has a key less than or equal to its
parent node's key. The right sub-tree of a node has a key greater than to its parent node's key

Deleting a node in a tree while maintaining its **Binary search tree property**.

## Explanation of cases:
1. When the node to be deleted is a leaf node then simply delete the node and pass nullptr to its parent node.
2. When a node to be deleted is having only one child then copy the child value to the node value and delete2.
the child (**Converted to case 1**)
3. When a node to be delete is having two childs then the minimum from its right sub tree can be copied to the3.
node and then the minimum value can be deleted from the node's right subtree (**Converted to Case 2**)


### Note:
The complexity of my code is **O(h)**, where h is the height of the tree.