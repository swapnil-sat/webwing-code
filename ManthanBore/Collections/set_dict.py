# s=set()
# print(type(s))
# s1={}
# print(type(s1))
# s1={1,}
# print(type(s1))
# s1=set()
# print(type(s1))
# s1.add(20)
# print(s1)
# print(type(s1))
# s1.add(30)
# print(s1)
# s2=set()
# s2.add(40)
# s2.add(50)
# print(s2)
# s1.update(s2)
# print(s1)
# l=[1,2,3,4]
# s1.update(l)
# print(s1)
# l=[1,2,3,4,5,2,4]
# s3=set(l)
# print(s3)
# s4=s3
# print(s4)
# s4.add(6)
# print(s4)
# print(s3)
# s5=s3.copy()
# print(s5)
# s3.add(7)
# print(s3)
# print(s5)
# print(s5.pop())
# print(s5)
# s5.remove(6)
# print(s5)
# s5.discard(3)
# print(s5)
# s3.discard(50)
# print(s3)
# s5.discard(50)
# print(s5)
# s5.clear()
# print(s5)
# print(40 in s1)
# print(100 not in s1)
# print(2 not in s1)
# d1=s1.discard(4)
# print(s1)
# d1=s1.remove(3)
# print(s1)
# d1=s1.pop()
# print(d1)
# i=iter(s1)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# for i in s1 :
#     print(i)

# d=dict()
# print(type(d))
# d1={}
# print(type(d1))
# d={1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}
# print(d)
# t=(1,2,3)
# print(type(t))
# d[t]="key is a tuple"
# print(d)
# d[6]="six"
# print(d)
# d[1]="Ten"
# print(d)
# d[1]="One"
# print(d)
# print(d.items())
# print(d.keys())
# print(d.values())
# for key,value in d.items():
#     print("key=",key,"value=",value)
# for a,b in d.items():
#     print(a,":",b)
# print(d[1])
# print(d[2])
# print(d.get(1))
# d.get(40)
# print(d)
# print(d.get(40,"Rock"))
# print(d.pop(3))
# print(d)
# print(d.popitem())
# print(d)
# del d[1]
# print(d)
# d["dict"]="Pune"
# d["state"]="MH"
# print(d)
# for k,v in d.items():
#     if v=="Pune":
#         d.pop(k)
#         print(d)
# d.clear()
# print(d)

# emp={
#     "ename":"rohit",
#     "esalary":"20,000",
#     "dept":"IT"
# }
# for x in emp:
#     print(x)
# for x in emp:
#     print(emp[x])
# for x in emp.keys():
#     print(x)
# for x in emp.values():
#     print(x)
# for x in emp.items():
#     print(x)
# emp2=emp.copy()
# print(emp2)
# emp2=dict(emp)
# print(emp2)

# Nested Dictionary:-
# company={
# "emp1":{
#     "ename":"sumit",
#     "esalary":"30,000",
#     "dept":"IT"
# }
#  "emp2":{
#     "ename":"ritesh",
#     "esalary":"40,000",
#     "dept":"shift 1"
# }
#  "emp3":{
#     "ename":"prakash",
#     "esalary":"29,900",
#     "dept":"shift 2"
# }
# }
# print(company)

# amazon={
#     "PC":"Dell",
#     "nikhil":"4",
#     "price":"3,70,000"
# }
# amazon.clear()
# print(amazon)