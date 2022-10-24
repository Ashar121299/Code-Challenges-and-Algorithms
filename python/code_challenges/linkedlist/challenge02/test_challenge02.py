# Write your test here
from challenge02 import LinkedList,Node


def test_case1():
    linkedList = LinkedList()
    node1 = Node(1)
    linkedList.append(node1)
    node2 = Node(2)
    linkedList.append(node2)
    node3 = Node(3)
    linkedList.append(node3)
    node4 = Node(4)
    linkedList.append(node4)
    node5 = Node(5)
    linkedList.append(node5)
    node6 = Node(6)
    linkedList.append(node6)
    actual=linkedList.middle_node()
    expected=[4, 5, 6]
    assert actual==expected

def test_case2():
    linkedList = LinkedList()
    node1 = Node(1)
    linkedList.append(node1)
    node2 = Node(2)
    linkedList.append(node2)
    node3 = Node(3)
    linkedList.append(node3)
    node4 = Node(4)
    linkedList.append(node4)
    node5 = Node(5)
    linkedList.append(node5)
    actual=linkedList.middle_node()
    expected=[3, 4, 5]
    assert actual==expected