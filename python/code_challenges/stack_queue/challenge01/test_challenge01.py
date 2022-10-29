# Write your test here
import pytest
from challenge01 import *


#@pytest.fixture 
def test_case1():
    queue1 = Queue()
    queue1.push(1)
    queue1.push(2)
    queue1.push(3)
    actual=queue1.peek()
    expected=1
    assert actual == expected
def test_case2():
    queue1 = Queue()
    queue1.push(1)
    queue1.push(2)
    queue1.push(3)
    actual=queue1.pop()
    expected=1
    assert actual == expected
def test_case3():
    queue1 = Queue()
    queue1.push(5)
    queue1.push(20)
    queue1.push(9)
    actual=queue1.peek()
    expected=5
    assert actual == expected
def test_case4():
    queue1 = Queue()
    queue1.push(5)
    queue1.push(20)
    queue1.push(9)
    queue1.peek()
    actual=queue1.empty()
    expected=False
    assert actual == expected
    
    