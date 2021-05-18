# Positional Argument:-
# def addition(a,b):
#     c=a+b
#     print("addition",c)
# addition(7,9)

# def addition(a=4,b=3):
#     c=a+b
#     print("addition",c)
# addition()

# Default Argument:-
# def addition(a,b=7):
#     c=a+b
#     print("addition",c)
# addition(9)
# addition(9,16)

# Keyword Argument:-
# def interest(price,rate,time):
#     i=price*rate*time/100
#     print("interest",i)
# interest(4000,10,2)
# interest(time=2,price=4000,rate=10)

# Arbitrary Argument:-
# def my_colour(*colours):
#     print("my favourite colour is "+colours[2])
# my_colour("red","yellow","blue","green")

# **Kwargs:-
# def my_colour(**colours):
#     print("my favourite colour is "+colours["lname"])
# my_colour(fname="red",lname="yellow")

# Passing list as an argument:-
# def my_colour(colour):
#     for x in colour:
#         print(x)
# colours=["red","yellow","blue","green"]
# my_colour(colours)

# Return statement or value:-
# def my_function(x):
#     return 5*x
# print(my_function(5))
# print(my_function(4))

# Pass statement:-
# def my_function():
#     pass