def lowestCommonAncestor(root,node1,node2):
    if(root == None):
        return None
    elif(node1.data == root.data or node2.data == root.data):
        return root    
    elif((node1.data <= root.data and node2.data > root.data) or (node2.data <= root.data and node1.data > root.data)):
        return root
    elif(root.data > max(node1.data, node2.data)):
        return lowestCommonAncestor(root.left_child, node1, node2)
    else:
        return lowestCommonAncestor(root.right_child, node1, node2)