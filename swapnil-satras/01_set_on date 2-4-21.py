s={1,2,3,4,5,6,7,8,9,10}
print(type(s),s)
s1=frozenset(s)
print(type(s1),s1)
print(id(s))
print(id(s1))