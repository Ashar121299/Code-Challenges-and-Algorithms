class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def construct_tree(preorder, inorder):
    '''
    this function take preorder which is the preorder traversal of a
     binary tree and inorder which is the inorder traversal of the same tree,
     and construct it and return the binary tree.
    '''
    if not inorder and not preorder:
            return None
    root = Node(preorder[0])
    idx = inorder.index(preorder[0])
    root.left = construct_tree(preorder[1:idx+1], inorder[:idx])
    root.right = construct_tree(preorder[idx+1:], inorder[idx+1:])
    return root

