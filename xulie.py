#编写程序1/2，2/3，3/4，...n(n+1),求所有项的和
# s=0
# for x in range(1,3):
#     s=s+x/(x+1)
# print(s)

#斐波那契数列，1，1，2，3，5，8，13，21，。。。。编程求出第多少项开始大于2021.
import re


# count =3
# n=1
# sum=1
# while(n<=3):
#     sum=sum+n
#     print("sum=",sum,"",end=" ")
#     n=sum+n
#     count=count+1
#     print("n=",n,";",end=" ")
# print("count=",count)

def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
i=1
while fib(i)<=3:
    i+=1
print("第%d 项的值为%d"%(i,fib(i)))
