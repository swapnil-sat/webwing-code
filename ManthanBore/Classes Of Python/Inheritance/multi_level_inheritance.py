# class Parent(object):
#     def show_P(self):
#         print("parent class method")
# class Child(Parent):
#     def show_C(self):
#         print("child class method")
# class Grandchild(Child):
#     def show_G(self):
#         print("grandchild class method")
# g=Grandchild()
# g.show_G()
# g.show_P()
# g.show_C()

# Using Constructor:-
# class Parent(object):
#     def __init__(self):
#         print("parent class constructor")
#     def show_P(self):
#         print("parent class method")
# class Child(Parent):
#     def __init__(self):
#         print("child class constructor")
#     def show_C(self):
#         print("child class method")
# class Grandchild(Child):
#     def __init__(self):
#         print("grandchild class constructor")
#     def show_G(self):
#         print("grandchild class method")
# g=Grandchild()
# g.show_G()
# g.show_P()
# g.show_C()

# class Parent(object):
#     def __init__(self):
#         super().__init__()
#         print("parent class constructor")
#     def show_P(self):
#         print("parent class method")
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("child class constructor")
#     def show_C(self):
#         print("child class method")
# class Grandchild(Child):
#     def __init__(self):
#         super().__init__()
#         print("grandchild class constructor")
#     def show_G(self):
#         print("grandchild class method")
# g=Grandchild()
# g.show_G()
# g.show_P()
# g.show_C()


