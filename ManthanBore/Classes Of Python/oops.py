# class phone:
#     def make_call(self):
#         print("making call")
#     def play_game(self):
#         print("playing game")
# p1=phone()
# p1.make_call()
# p1.play_game()

# class employee:
#     def __init__(self,fname,lname,salary):
#         self.fname=fname
#         self.lname=lname
#         self.salary=salary
# rohit=employee("rohit","patil",45000)
# rohan=employee("rohan","patil",45000)
# print(rohit.fname,rohan.fname)

# class employee:
#     increment=1.5
#     def __init__(self,fname,lname,salary):
#         self.fname=fname
#         self.lname=lname
#         self.salary=salary
#     def increase(self):
#         self.salary=int(self.salary*employee.increment)
# rohit=employee("rohit","patil",45000)
# rohan=employee("rohan","patil",45000)
# print(rohit.fname,rohit.lname)
# print(rohan.salary)
# rohit.increase()
# print(rohit.salary)

# Creating a class with constructor:-
# class employee:
#     def __init__(self,name,age,gender,salary):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.salary=salary
#     def employee_details(self):
#         print("name of employee",self.name)
#         print("age of employee",self.age)
#         print("gender of employee",self.gender)
#         print("salary of employee",self.salary)
# e1=employee("rohit",24,"male",20000)
# e1.employee_details()