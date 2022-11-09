# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


        
def convertToBST(nums):
    if not nums:
        return None
    nums.sort()
    mid=len(nums)//2
    root=Node(nums[mid])
    root.left=convertToBST(nums[:mid])
    root.right=convertToBST(nums[mid+1:])
    return root
def BredthFirst(root):
    retArr=[]
    queue1=[]
    queue1.append(root)
    while(len(queue1)>0):
        v=queue1[0].value
        retArr.append(v)
        current=queue1.pop(0)
        if(current.left != None):
            queue1.append(current.left)
        if(current.right !=None):
            queue1.append(current.right)
    return retArr
        
        
    
def valid(current):
    if current.left and current.left.value < current.value:
        valid(current.left)
        return True
    if current.right and current.right.value > current.value:
        valid(current.right)
        return True
    else: 
        return False
        
