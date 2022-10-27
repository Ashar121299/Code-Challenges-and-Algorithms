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

    linkl.remove_nth_node(linkl.head,2)
    actual=linkl.print_All()
    expected=[1, 2,  3, 5]
    assert actual == expected
