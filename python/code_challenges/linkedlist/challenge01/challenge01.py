# Write here the code challenge solution
def delete(list, node):
    '''
    This function take a linked list and node as parameter ,and 
    search for the node in the list and deleted it and return the linked 
    list after deletion.
    '''
    node.value=node.next.value 
    node.next=node.next.next
    if list.head is None:
        print("The linked list is empty")
    else:
        nodes=[]
        current = list.head
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

if __name__=='__main__':
    class Node:
        def __init__(self,value):
           self.value = value
           self.next = None
    class LinkedList:
        def __init__(self):
          self.head = None

        def append(self, node):
            if self.head is None:
                self.head = node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = node
    
    linkedList = LinkedList()
    node1 = Node(9)
    linkedList.append(node1)
    node2 = Node(1)
    linkedList.append(node2)
    node3 = Node(5)
    linkedList.append(node3)
    node4 = Node(8)
    linkedList.append(node4)
    print(delete(linkedList,node2))

