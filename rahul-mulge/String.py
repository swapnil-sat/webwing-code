#index number
s='rahul is developer'
print(s [1] )
print(s [2] )
print(s [0] )
s='rahul is developer'
print(s [-1] )
print(s [-2] )
print(s [-3] )
#=====================================================
#concatenation string
s1='rahul'
s2='mulge'
print(s1+s2)
#multiplication string
s1='python'
print(s1*3)
#positive indexing
s='Process finished with exit code'
print(s [:] )
s='Process finished with exit code'
print(s [: : 2])
#neagtive indexing
s='Process finished with exit code'
print(s [-3])
s='Process finished with exit code'
print(s [: : -2])
#==================================================================
#unpacking string
a,b,c,d,e,f='python'
print(a)
print(b)
print(c)
print(d)
print(e)
s='python'
a,b,c,d,e,f = s
print(a)
print(b)
print(c)
#======================================================
#capitalize
s='rahul is developer'
a=s.capitalize()
print(a)
s='rahul is developer'
a=s.capitalize()
print(a)
#====================================================
#itle
s='rahul is developer'
a=s.title()
print(a)
#islower
s='rahul is developer'
a=s.islower()
print(a)
s='Rahul is developer'
a=s.islower()
print(a)
#isupper
s='PYTHON'
a=s.isupper()
print(a)
s='pYTHON'
a=s.isupper()
print(a)
#lower
s='PYthon'
a=s.lower()
print(a)
s='python'
a=s.lower()
print(a)
#====================================================================
#len
s='python develper'
a=len(s)
print(a)
#counts
s='python developer'
a=s.count('o')
print(a)
#find
s='rahul is developer'
a=s.find('u')
print(a)
s='rahul is developer'
a=s.find('e',11)
print(a)
#===============================================================
#split
s='python developer'
a=s.split()
print(a)
#lstrip
str='!!!!python developer!!!!'
a=str.lstrip('!')
print(a)
#rstrip
str='!!!!python developer!!!!'
a=str.rstrip('!')
print(a)
#strip
str='!!!!python developer!!!!'
a=str.strip('!')
print(a)
#swapcase
s='PYthon'
a=s.swapcase()
print(a)
#reversed
s='python'
a="".join (reversed(s))
print(a)
#replace
str='python learner'
a=str.replace('learner','developer')
print(a)
#ascending oreder
str='python'
a="".join(sorted(str))
print(a)
#desending order
str='pytohn'
a="".join(reversed(sorted(str)))
print(a)

