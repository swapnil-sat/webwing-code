import sys
def add():
    print(sys.argv)
    print(type(sys.argv))
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    # a = 10
    # b = 20
    c = a+b
    print (c)
add()

