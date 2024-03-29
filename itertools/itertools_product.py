from itertools import product

print list(product([1, 2, 3], repeat = 2))
'''
>> [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
'''


A, B = [1, 2, 3], [1, 2, 3]
print [(x, y) for x in A for y in B]
'''
>> [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
'''


A, B = [1, 2], [3, 5]
print [(x, y) for x in A for y in B]
'''
[(1, 3), (1, 5), (2, 3), (2, 5)]
'''

A = [[1,2,3],[3,4,5]]
print list(product(*A))
'''
[(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
'''
