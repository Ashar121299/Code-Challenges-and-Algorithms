# Write your test here
import pytest
from challenge02 import findRepeatedword

def test_sentences():
    s1="ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    actual=findRepeatedword(s1)
    excepted="ASAC"
    assert actual==excepted
  
