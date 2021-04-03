Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 10.25\\2
SyntaxError: unexpected character after line continuation character
>>> 10.25//2
5.0
>>> 13//2
6
>>> 13//5.2
2.0
>>> 13/2
6.5
>>> 12/2
6.0
>>> 123%10
3
>>> 123//10
12
>>> 12%10
2
>>> 12//10
1
>>> 1%10
1
>>> str='abc'
>>> str1='xyz,
SyntaxError: EOL while scanning string literal
>>> a='abc'<'xyz
SyntaxError: EOL while scanning string literal
>>> a='abc'
>>> b='xyz'
>>> print(a>b)
False
>>> x='ABC'=='abc'
>>> print(x)
False
>>> 10==10
True
>>> 10!=10
False
>>> 20!=10
True
>>> a='apple'
>>> b='apple'
>>> a is b
True
>>> a='apple'
>>> b='banana'
>>> a is b
False
>>> a is not b
True
>>> a=10
>>> b=10
>>> a is not 10
False
>>> s='rahul is developer'
>>> 'rahul' in s
True
>>> 'rahul' not in s
False
>>> m not in s
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    m not in s
NameError: name 'm' is not defined
>>> 'm'not in s
True
>>> a=