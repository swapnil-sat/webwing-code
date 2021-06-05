# class BalanceException(Exception):
#     pass
# def Check_Balance():
#     money=10000
#     withdraw=9000
#     try:
#         balance=money-withdraw
#         if(balance<=2000):
#             raise BalanceException("insufficient balance")
#         print(balance)
#     except BalanceException as obj:
#         print(obj)
# Check_Balance()

# class VoterEligibilityCriteria(Exception):
#     def __init__(self):
#         super().__init__()
# try:
#     age=14
#     print("age is "+str(age))
#     if (age<18):
#         raise VoterEligibilityCriteria
# except VoterEligibilityCriteria:
#     print("age is less than 18")
# else:
#     print("age is greater than or equal to 18")
# finally:
#     print("end of the program")


