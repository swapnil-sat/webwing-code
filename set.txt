Python 3.0 (r30:67507, Dec  3 2008, 20:14:27) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 3.0      
>>> set1={1,2,3,4,5,6}
>>> set1.add(55)
>>> print(set1)
{1, 2, 3, 4, 5, 6, 55}
>>> set1.remove(3)
>>> prent(set1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    prent(set1)
NameError: name 'prent' is not defined
>>> print(set1)
{1, 2, 4, 5, 6, 55}
>>> fs= frozenset(set1)
>>> print(set1)
{1, 2, 4, 5, 6, 55}
>>> type(fs)
<class 'frozenset'>
>>> d={'name':'ram',}
>>> d={'name':'ram',
   'age':'27',
   'city':'pune'}
>>> type(d)
<class 'dict'>
>>> id(d)
44738864
>>> d.keys()
<dict_keys object at 0x02AAC520>
>>> print(d)
{'city': 'pune', 'age': '27', 'name': 'ram'}
>>> d,valuse()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d,valuse()
NameError: name 'valuse' is not defined
>>> 
