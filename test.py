# -*- coding = utf-8 -*-
# @Time : 2024/3/14 22:14
# @Author : Geist
# @File ： test.py
# @Software: PyCharm
import pandas as pd

left = pd.DataFrame(
    {'key1': ['key0', 'key1', 'key2', 'key3'],
     'key2': ['key0', 'key1', 'key2', 'key2'],
     'A': ['a0', 'a1', 'a2', 'a3'],
     'B': ['b0', 'b1', 'b2', 'b3']},
    index=['one', 'two', 'three', 'four']
)
print(left)
print('')
right = pd.DataFrame(
    {
        'key1': ['key0', 'key1', 'key1', 'key2'],
        'key2': ['key0', 'key1', 'key1', 'key3'],
        'C': ['c0', 'c1', 'c2', 'c3'],
        'D': ['d0', 'd1', 'd2', 'd3']
    },
    index=['one', 'two', 'three', 'four']
)
print(right)

data = pd.merge(left, right, on=['key1', 'key2'], how='inner')
print(data)

