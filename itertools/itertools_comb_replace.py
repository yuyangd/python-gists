from itertools import combinations_with_replacement, combinations, product

print list(combinations('12345', 2))
'''
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'),
             ('2', '3'), ('2', '4'), ('2', '5'),
                         ('3', '4'), ('3', '5'),
                                     ('4', '5')]
'''

print list(combinations_with_replacement('12345',2))
'''
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'),
             ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'),
                         ('3', '3'), ('3', '4'), ('3', '5'),
                                     ('4', '4'), ('4', '5'),
                                                 ('5', '5')]
'''
print list(product('12345', repeat = 2))
'''
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'),
 ('2', '1'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'),
 ('3', '1'), ('3', '2'), ('3', '3'), ('3', '4'), ('3', '5'),
 ('4', '1'), ('4', '2'), ('4', '3'), ('4', '4'), ('4', '5'),
 ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4'), ('5', '5')]
'''


A = [1,1,3,3,3]
print list(combinations(A,2))
'''
[(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]
'''

n, m = raw_input().split()
for i in list(combinations_with_replacement(sorted(n), int(m))):
    print ''.join(i)
