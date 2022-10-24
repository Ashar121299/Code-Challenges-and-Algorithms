# Write here the code challenge solution
def middle_node (list):
    count=0
    nodes=[]
    current = list.head
    while current is not None:
        count+=1
        nodes.append(current.value)
    current=current.next
    if (count/2)%2!=0:
        mid=round(count/2)
    else :
        mid=(count/2)+1

    return nodes[mid:]
    

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

    print(middle_node(linkedList))


                
            