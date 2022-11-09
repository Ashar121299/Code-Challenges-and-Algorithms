# Write your test here
# Write your test here

from challenge03 import *

def test_one():
    numbers=[0,-3,-10,5,9]
    root1=convertToBST(numbers)
    actual=BredthFirst(root1)
    expected=[0,-3,9,-10,5]
    assert actual==expected
def test_two():
    numbers=[1,3]
    root1=convertToBST(numbers)
    actual=BredthFirst(root1)
    expected=[3,1]
    assert actual==expected
