#==================================================
#list
l1=[1,2,3,4,5,6,]
print(l1)
l1=[1,2,'python',33]
print(l1)
#indexing
l2=[10,20,'python',40,2,13]
print(l2 [1])
print(l2 [2])
print(l2[0])
print(l2 [-1])
print(l2 [-2])
print(l2 [3])
#slicing
l2=[10,20,'python',40,2,13]
print(l2[0:1])
print(l2[1:2])
#concantation
l1=['rahul',10,13]
l2=['sumeet',20,30]
a=(l1+l2)
print(a)
#multiplication
l1=['rahul',10,13]
a=(l1*3)
print(a)
#len
l1=[10,34,'python',7,55,99,1,]
print(len(l1))
#count
l1=['rahul',10,13,66,87,9,7]
a=l1.count(10)
print(a)
l1=['rahul',10,13,66,87,9,7,6,10]
a=l1.count(10)
print(a)
l1=[1,2,3,True,False,1,0,False,1+9j,1.1]
a=l1.count(0)
print(a)
l1=[1,2,3,True,False,1,0,False,1+9j,1.1]
a=l1.count(1)
print(a)
#index
l1=[10,20,'python',40,50,70]
a=l1.index(10)
print(a)
#=========================================================
l1=int(input('enter start value:'))
l2=int(input('enter end value:'))
a=range(1,10)
print(a)
s=range(10,21,2)
print(s)
l1=int(input(0))
l2=int(input(10))
s=range(0,10)
print(s)
