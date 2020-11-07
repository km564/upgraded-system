# #
# # class parent(object):
# #     def altered(self):
# #         print("Parent altered")
# # class child(parent):
# #     def altered(self):
# #         print("Before Parent altered")
# #         super(child,self).altered()
# #         print("After Parent altered")
# # dad=parent()
# # son=child()
# # #dad.altered()
# # son.altered()
# #
# #
# # class parent(object):
# #     def override(self):
# #         print("Parent Overrride")
# #     def implicit(self):
# #         print("Parent Impliciti")
# #     def altered(self):
# #         print("Parent altered")
# # class child(parent):
# #     def override(self):
# #         print("Child override")
# #     def implicit(self):
# #         print("Before Child Implicit")
# #         super(child,self).implicit()
# #         print("Afeter Child Implicit")
# #         super(child, self).implicit()
# #     def altered(self):
# #         print("Child Before parent altered")
# #         super(child,self).altered()
# #         print("After Child altered")
# # p=parent()
# # c=child()
# # p.override()
# # p.implicit()
# # p.altered()
# #
# # print("************************************************")
# # c.override()
# # c.implicit()
# # c.altered()
# #
# # class parent(object):
# #     def override(self):
# #         print("Parent Overrride()")
# #     def implicit(self):
# #         print("Parent Implicit()")
# #     def altered(self):
# #         print("Parent altered()")
# #
# # class child(object):
# #     def __init__(self):
# #         self.parent = parent()
# #     def implicit(self):
# #         self.parent.implicit()
# #     def override(self):
# #         print("Child Override")
# #     def altered(self):
# #         print("Child Before parent altered")
# #         self.parent.altered()
# #         print("After Child altered")
# #
# # son=child()
# # son.implicit()
# # son.override()
# # son.altered()
# #
# #
# #
# #
# #
# # list = [10,20,30,40,50,60,70]
# # num = int(input("Enter number\n"))
# #
# # if num in list:
# #     print("%d is Found" %(num))
# #     print(f'{num} is Found')
# # else:
# #     print("%d is not Found"%(num))
# #
# # a=4
# # b=5
# # print(bin(a))
# # print(bin(b))
# #
# #
# # a,b,a=10,10,20
# # print(a>b)
# # print(a>=b)
# # print(a==b)
# # print(a!=b)
# # print(b>a)
# # print(b!=a)
# # print("a is b=",a is b )
# # print("a is not  b=",a is not b)
# #
# # dict1 = {101:'xyz',102:'abc',103:'ast',104:'pqr'}
# # type(dict1)
# # print(dict1)
# #
# # x=int(input("enter key val:\n"))
# # print(x)
# # if x in dict1:
# #     print("%d is Found"%(x))
# # else:
# #     print("%d is not Found"%(x))
# #
# # a = [1,2,3,4,5]
# # b = [1,2,3,4,5]
# # print(a)
# # print(b)
# # print(type(a))
# # print(type(b))
# # print(id(a))
# # print(id(b))
# # if a==b:
# #     print("Same ")
# # else:
# #     print("Not same%d")
# #
# # if a is b:
# #     print("Memory address is same : %d"%(id(a),id(b)))
# # else:
# #     print("Memory address is not same: %d , %d"%(id(a),id(b)))
# #
# #
# # a=150
# # b=5
# # print(bin(a))
# # print(bin(b))
# # print(a<<2)
# # print(a>>5)
# #
# # """
# #
# #
# # a=10
# # b=20
# # print(a ^ b)
# # print(type(a^b))
#
#
# # import git
# # from git import Repo
# #
# # host_name ="github.com"
# # Git_Account = "murali-jpa"
# # username = "diamond.mjp@gmail.com"
# # password = "murali6116"
# # full_local_path = "MK-Atmecs_aws_101"
# # #remote = f"https://{username}:{password}@{host_name}/{Git_Account}"
# # #remote = f"{username}:{password}@https://github.com/murali-jpa"
# # # Repo.clone_from(remote, full_local_path)
# #
# # Repo.clone_from(f'https://diamond.mjp@gmail.com:murali6116/github.com/murali-jpa','ABCD')
#
import git
from git import Repo
host_name ="github.com/DevDungeon"
Git_Account = "Cookbook"
full_local_path = "Murali-Atmecs_1001"
remote = f"https://github.com/DevDungeon/Cookbook"
#remote = f"https://{host_name}//{Git_Account}"
Repo.clone_from(remote, full_local_path)



