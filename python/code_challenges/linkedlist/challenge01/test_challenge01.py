# Write your test here
import pytest 
from challenge01 import *


def test_case1():
    linkedList = LinkedList()
    node1 = Node(9)
    linkedList.append(node1)
    node2 = Node(1)
    linkedList.append(node2)
    node3 = Node(5)
    linkedList.append(node3)
    node4 = Node(8)
    linkedList.append(node4)
    delete(node3)
    assert linkedList.print_All() ==[9, 1, 8]

def test_case2():
    linkedList2 = LinkedList()
    node1 = Node(4)
    linkedList2.append(node1)
    node2 = Node(5)
    linkedList2.append(node2)
    node3 = Node(9)
    linkedList2.append(node3)
    node4 = Node(7)
    linkedList2.append(node4)
    delete(node1)
    assert linkedList2.print_All() ==[5, 9, 7]

def test_case3():
    linkedList3 = LinkedList()
    node1 = Node(1)
    linkedList3.append(node1)
    node2 = Node(3)
    linkedList3.append(node2)
    node3 = Node(7)
    linkedList3.append(node3)
    node4 = Node(9)
    linkedList3.append(node4)
    delete(node2)
    assert linkedList3.print_All() ==[1, 7, 9]


def test_case4():
    linkedList4 = LinkedList()
    node1 = Node(15)
    linkedList4.append(node1)
    node2 = Node(26)
    linkedList4.append(node2)
    node3 = Node(8)
    linkedList4.append(node3)
    node4 = Node(10)
    linkedList4.append(node4)
    delete(node3)
    assert linkedList4.print_All() ==[15, 26, 10]














