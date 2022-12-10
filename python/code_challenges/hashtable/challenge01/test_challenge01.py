# Write your test here
import pytest
from challenge01 import Tree,Node

def test_tree1():
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

    k=3
    actual = tree1.TwoSum(tree1.root,k)
    expected = False
    assert actual == expected 

