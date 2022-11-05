# Write your test here
from challenge01 import *
def test_one():
    tree1=[]
    tree=construct_tree([3,9,20,15,7],[9,3,15,20,7])
    tree1.append(tree.value)
    tree1.append(tree.left.value)
    tree1.append(tree.right.value)
    tree1.append(None)
    tree1.append(None)
    tree1.append(tree.right.left.value)
    tree1.append(tree.right.right.value)
    actual=tree1
    expected =[3,9,20,None,None,15,7]
    assert actual== expected
