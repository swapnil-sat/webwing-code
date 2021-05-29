# class Parent(object):
#     money=1000000
#     def show(self):
#         print("parent class instance method")
#     @classmethod
#     def show_money(cls):
#         print("parent class method",cls.money)
#     @staticmethod
#     def static():
#         x=61
#         print("parent class static method",x)
# class Child(Parent):
#     def display(self):
#         print("child class instance method")
# c=Child()
# c.display()
# c.show()
# c.show_money()
# c.static()

# Single Inheritance using constructor:-
# class Parent(object):
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def print_name(self):
#         print(self.fname,self.lname)
# class Child(Parent):
#     pass
# x=Child("rohit","patil")
# x.print_name()


