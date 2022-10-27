# Write here the code challenge solution   
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        '''
        This fuction add a new node to the end of the
        linked list or add the first node
        if the linked list was already empty
        '''
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node


    def remove_nth_node(self,head,n):
        '''
        This function return linked list after remove the 
        nth node from it 
        '''
        fast = head
        slow = head
                                                                                
        for i in range(n):
            fast = fast.next
    
        if not fast:
            return head.next

        

        while fast.next:
            fast = fast.next
            slow = slow.next
 
        slow.next = slow.next.next
        return head
    
    def print_Nth(self,head):
        
        result=''

        while head is not None:
            result+=f'{head.value}--> '
            head=head.next
        result+='None'
        
        return result

        
        
    def print_All(self):
        nodes=[]
        current = self.head
        while current is not None:
            nodes.append(current.value)
            current=current.next
        return nodes







                          
if __name__=='__main__':   
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
    print(linkedList.print_Nth(linkedList.remove_nth_node(linkedList.head,2)))
    
