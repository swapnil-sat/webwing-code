#dictionary
#1. Creating empty dictionary and adding key:value pairs.
dict1={}
print(dict1)
print(type(dict1))
dict1['a']=10
dict1['b']=20
dict1['c']=30
print(dict1)
dict1['a']=50
print(dict1)
#2. Creating a dictionary with dict() function
dic1=dict([('a',10),('b',20),('c',30),('d',40)])
print(dic1)
print(type(dic1))
#Accessing data from dictionary
#We can assign values to the keys and later we can fetch values by using Keys
dict1={'id':10,'name':'rahul','age':25,'marks':90}
print(dict1)
print(dict1['id'])
print(dict1['marks'])
dict2={'Id':100,'Name':'Sai', 'subjects':['SQL Server', 'Oracle', 'Python']}
print(type(dict2))
print(dict2['subjects'])
print(dict2['subjects'][0])
#Updating dictionary values
#If we need to change the age from 25 to 27 then
dict1={'id':102,'name':'sai','age':25,'subjects':['sql','oracle''python']}
dict1['age']=27
print(dict1)
#Deleting key:value pairs from dictionary
#Pop:
#Pop:
#If we need to delete the value 27 from the above dictionary then (by using pop)
dict1={'id':102,'name':'sai','age':25,'subjects':['sql','oracle''python']}
print(dict1.pop('id'))
#
d2 = {'id': 101, 'name': 'apple', 'add': 'pune'}
d2.pop('add')
print(d2)
#We can also delete by using popitem()
d2 = {'id': 101, 'name': 'apple', 'add': 'pune'}
print(d2.popitem())
d2 = {'id': 101, 'name': 'apple', 'add': 'pune'}
d2.clear()
print(d2)
#Dictionary functions
#keys(): it returns all keys from dictionary
d2 = {'id': 101, 'name': 'apple', 'add': 'pune'}
a = d2.keys()
print(a)
d2={'id':10,'name':'apple','add':'mumbai'}
a=d2.values()
print(a)
#copy(): it copies the dict into new dict.
d2={'id':10,'name':'apple','add':'mumbai'}
s=d2.copy()
print(s)
#pop(): it removes specific key value pair.
d2={'id':10,'name':'apple','add':'mumbai'}
a=d2.pop('id')
print(a)
#Note: we can also remove the key: value pair by using 'del' command.
d2={'id':10,'name':'apple','add':'mumbai'}
del (d2['id'])
print(d2)
#clear
dic1={3: (10, 20, 30), 4: [100, 'a', False], 's': 100}
dic1.clear()
print(dic1)
#fromkeys(): we can use tuple elements as keys in the dict and the elements must be unique
tup=(1,2,3,4,5,)
d1={}
a=d1.fromkeys(tup,'rahul')
print(a)
#we can also use list elements as keys in the dict and the elements must be unique
l1=[1,2,3,4,5]
d1={}
a=d1.fromkeys(tup,12)
print(a)
print(type(d1))
#get(): this function is used to get the value of specified key.
d2={'id':102,'name':'sai','add':'pune'}
a=d2.get('add')
print(a)
#Items(): this function is used to get all items. All key and value pairs will be displayed in tuple format
#
d2 = {'id': 101,'name':'apple','add':'pune'}
a = d2.items()
print(a)
#Update(): the current dictionary will be updated with the all key:value pairs from another dictionary.
d1={'id':12,'name':'rahul','add':'pune'}
d2={'sub1':'sql','sub':'java'}
a=d1.update(d2)
print(d1)
#How to perform arithmetic operations on the values of a dictionary?
#sum
d1={'sub1':80,'sub2':90,'sub3':70,'sub4':80}
a=sum(d1.values())
print(a)
#max
d1={'sub1':80,'sub2':90,'sub3':70,'sub4':80}
a=max(d1.values())
print(a)
#min
d1={'sub1':80,'sub2':90,'sub3':70,'sub4':80}
a=min(d1.values())
print(a)
#len
d1={'sub1':80,'sub2':90,'sub3':70,'sub4':80}
a=len(d1.values())
print(a)
#sorted
d1={'zsub1':100,'ysub2':90,'xsub3':70,'wsub4':80}
a=sorted(d1.values())
print(a)
