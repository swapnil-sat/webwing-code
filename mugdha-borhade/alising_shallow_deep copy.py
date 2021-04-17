# ALISING

l = [1,2,3,4,"abc",True]
print("l: ", l)
print(id(l))
l1 = l
print("l1: ",l1)
print(id(l1))

l.append(99)
print("l: ",l)
print("l1: ",l1)
l1.append(100)
print("l1: ",l1)
print("l: ",l)
print(id(l))
print(id(l1))


# SHALLOW COPY

import copy
l2 = copy.copy(l)
print("l2: ",l2)
print(id(l2))
l.append(200)
print("l: ", l)
print("l1: ", l1)
print("l2: ", l2)

# DEEP COPY

l[2]=[300,301,302]
print("l: ",l)
print("l1: ",l1)
print("l2: ",l2)

l3= copy.copy(l)
print("l3: ",l3)
l.append(888)
print("l: ",l)
print("l3: ",l3)
print("l1 :",l1)
print("l2: ",l2)
l[2][1]=555
print("l: ",l)
print("l1: ",l1)
print("l2: ",l2)
print("l3: ",l3)
print(id(l))
print(id(l1))
print(id(l2))
print(id(l3))