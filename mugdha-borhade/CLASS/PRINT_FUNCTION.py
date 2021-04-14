print("hello")
print("world")

print("hello","world",sep=",")

a = 10
b = True
c = 10.25
d = "Hello"
e = 12
# numbered index:
print("a = {0},b= {1}, c ={2},d = {3}" .format(a,b,c,d))
# empty placeholders:
print("a={},b={},c={}".format('ok',1,True))
# named indexes:
print("a = {name}, b = {age},c = {city}" . format(name="Abc",age=10,city="pune"))
#
print("a=",a ,"b=",b , "c=",c)
#
print("a = %d,b =%f,c =%s"%(a,b,c))
# formated string

print(f"a = {a,e},b = {b},c={c}")

# print using symbols implicitly
print("a=",a)
print("b=",b)

print("a=",a,end=",")
print("b=",b)