#=============================================
#creating a tuple with tuple()
tup=tuple([10,20,30,True,'Python'])
print(tup)
print(type(tup))
#without tuple
tup=10,20,30,True,'Python'
print(tup)
tup2=tuple([10,20,30,40,50,60])
print(tup2)
tup3=(10,20,30,40,50)
print(tup3)
print(type(tup3))
tup=tuple([10,20,30,True,'Python'])
print(tup)
#tuple indexing
tup=(10,20,30,True,'Python')
a=tup.index(10)
print(a)
tup=(10,20,30,True,'Python')
a=tup[2]
print(a)
tup=(10,20,30,True,'Python')
a=tup[-1]
print(a)
tup=(10,20,30,True,'Python')
a=tup[-3]
print(a)
#tuple slicing
tup=(10,20,30,True,'Python')
a=tup[0:2]
print(a)
tup=(10,20,30,True,'Python')
a=tup[0:4:2]
print(a)
tup=(10,20,30,True,'Python')
a=tup[-5:-1]
print(a)

tup=(10,20,30,True,'Python')
a=tup[-3]
tup=(10,20,30,True,'Python')
a=tup[-3]
print(a)
tup=(10,20,30,True,'Python')
a=tup[:]
print(a)
#concatanating
tup1=10,20,30,True,'Python'
tup2=('rahul',60,30,20,10)
a=(tup1+tup2)
print(a)
#multiplication
tup1=(10,20,30,True,'Python')
a=(tup*3)
print(a)
#all
tup1=(1,2,3)
a=(all(tup1))
print(a)
tup1=(1,2,3,0)
a=(all(tup1))
print(a)
tup1=(1,2,3,0,'false')
a=(all(tup1))
print(a)
#any
tup=(1,2,3,0,'false')
s=(any(tup))
print(s)
tup1=(0,'false',0,'false')
s=(any(tup1))
print(s)
#len
tup=(1,2,3,4,5,6,6.6)
print(len(tup))
#count
tup=(1,10,20,True,0)
print(tup.count(0))
tup=(1,10,20,True,0)

#index
tup=(1,10,20,True,0)
a=tup.index(10)
print(a)
tup=(1,10,20,True,0)
a=tup.index(0)
print(a)
