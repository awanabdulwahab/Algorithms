class Node(object):
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.data = data
        
class BinarySearchTree(object):
    def insert(self,root,node):
        if root is None:
            return node
        
        if root.data < node.data:
            root.right_child = self.insert(root.right_child, node)
        else:
            root.left_child = self.insert(root.left_child, node)
            
        return root
    
    def in_order_place(self,root):
        if not root:
            return None
        
        else:
            self.in_order_place(root.left_child)
            print(root.data)
            self.in_order_place(root.right_child)        
    
    def pre_order_place(self,root):
        if not root:
            return None
        else:
            print(root.data)
            self.pre_order_place(root.left_child)
            self.pre_order_place(root.right_child)
            
    def post_order_place(self,root):
        if not root:
            return None
        else:
            self.post_order_place(root.left_child)
            self.post_order_place(root.right_child)
            print(root.data)



# Testing the BST
r = Node(3)

node = BinarySearchTree()
nodeList  =  [1, 8, 5, 12, 14, 6, 15, 7, 16, 8]

for nd in nodeList:
    node.insert(r, Node(nd))

print("In Order Traversal")
print(node.in_order_place(r))                
print("Pre Order Traversal")
print(node.pre_order_place(r))
print("Post Order Traversal")
print(node.post_order_place(r))                      