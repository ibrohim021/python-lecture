from copy import copy


a = {1,2,5,6,9,10}

b = {4,7,1,3,8,10}

c = a.copy()
print(c)

u = a.union(b)
print(u)

i = a.intersection(b)
print(i)

d = a.difference(b)
print(d)