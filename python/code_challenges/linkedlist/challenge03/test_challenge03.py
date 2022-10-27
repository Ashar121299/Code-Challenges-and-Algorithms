# Write your test here
import pytest
from challenge03 import Node,LinkedList

def test_case1():

    linkl=LinkedList()
    node1 = Node(1)
    linkl.append(node1)
    node2 = Node(2)
    linkl.append(node2)
    node3 = Node(3)
    linkl.append(node3)
    node4 = Node(4)
    linkl.append(node4)
    node5 = Node(5)
    linkl.append(node5)
    actual=linkl.print_Nth(linkl.remove_nth_node(linkl.head,2))
    expected='1--> 2--> 3--> 5--> None'
    assert actual == expected

def test_case2():

    linkl=LinkedList()
    node1 = Node(1)
    linkl.append(node1)
    node2 = Node(2)
    linkl.append(node2)
    node3 = Node(3)
    linkl.append(node3)
    node4 = Node(4)
    linkl.append(node4)
    node5 = Node(5)
    linkl.append(node5)
    actual=linkl.print_Nth(linkl.remove_nth_node(linkl.head,3))
    expected='1--> 2--> 4--> 5--> None'
    assert actual == expected
def test_case3():

    linkl=LinkedList()
    node1 = Node(1)
    linkl.append(node1)
    node2 = Node(2)
    linkl.append(node2)
    node3 = Node(3)
    linkl.append(node3)
    node4 = Node(4)
    linkl.append(node4)
    node5 = Node(5)
    linkl.append(node5)
    actual=linkl.print_Nth(linkl.remove_nth_node(linkl.head,4))
    expected='1--> 3--> 4--> 5--> None'
    assert actual == expected
def test_case4():

    linkl=LinkedList()
    node1 = Node(1)
    linkl.append(node1)
    node2 = Node(2)
    linkl.append(node2)
    node3 = Node(3)
    linkl.append(node3)
    node4 = Node(4)
    linkl.append(node4)
    node5 = Node(5)
    linkl.append(node5)
    actual=linkl.print_Nth(linkl.remove_nth_node(linkl.head,5))
    expected='2--> 3--> 4--> 5--> None'
    assert actual == expected
def test_case5():

    linkl=LinkedList()
    node1 = Node(1)
    linkl.append(node1)
    actual=linkl.print_Nth(linkl.remove_nth_node(linkl.head,1))
    expected='None'
    assert actual == expected
def test_case6():

    linkl=LinkedList()
    node1 = Node(1)
    linkl.append(node1)
    node2 = Node(2)
    linkl.append(node2)
    actual=linkl.print_Nth(linkl.remove_nth_node(linkl.head,1))
    expected='1--> None'
    assert actual == expected

