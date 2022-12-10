# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def TwoSum(self, root, k):
        '''
        this function check if summation of any 2 nodes inside tree equal the value of k
        '''
        self.memory_dict = {}
        def check(root):
            if not root:
                return False
            if root.val in self.memory_dict.keys():
                return True
            self.memory_dict[k-root.val] = 1
            return check(root.left) or check(root.right)
        return check(root)
if __name__=="__main__":
    tree1 = Tree()
    node1 = Node(5)
    tree1.root = node1

    node2 = Node(3)
    tree1.root.left = node2

    node3 = Node(6)
    tree1.root.right = node3

    node4 = Node(2)
    tree1.root.left.left = node4

    node5 = Node(4)
    tree1.root.left.right = node5

    node6 = Node(7)
    tree1.root.right.right = node6

    k=9
    print(tree1.TwoSum(tree1.root,k))


