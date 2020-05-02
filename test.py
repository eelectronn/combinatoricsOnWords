"""
Created on May 01, 2020

@author: Harsh N. Patel

"""
import itertools

a = itertools.product(['0', '1'], repeat=3)
a = [''.join(word) for word in list(a)]
print(a)
