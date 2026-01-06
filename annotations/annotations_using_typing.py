""" Annotaton usng typng"""

from typing import List

def addition(a: int, b: int) -> float:
    """ ths functon adds two numbers"""
    return a + b

def sum_of_lists(lists: List[int]) -> float:
    """ ths functon sums lstd"""
    return sum(lists)

s = sum_of_lists([12,34,56,77])
print(s)
