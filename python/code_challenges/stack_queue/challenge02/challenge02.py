# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.next = None
        self.value =value 
class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This stack is empty")
    
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def parentheses(self,str):
        '''This function check if the string 
           of parentheses is valid
        '''
        dictionary={'(':')','[':']','{':'}'}
        for s in str:
            if s in dictionary.keys():
                self.push(s)
            elif s in dictionary.values():
                if dictionary[self.top.value] == s:
                    self.pop()
                else:
                    return False    
        return True
if __name__=='__main__':
    stack1= Stack()
    print(stack1.parentheses("[{[]]}]"))

