# a=int (input("请输入三角形的第一条边："))
# b=int (input("请输入三角形的第2条边："))
# c=int (input("请输入三角形的第3条边："))
# s=(a+b+c)*(1/2)
# print("此三角形的面积为，",s,end=' ')
# print("此三角形的面积为w，",s,end=' ')
# a=15
# print("a=%d"%a)
# print("a=%o"%a)
# print("a=%X"%a)
# print("a=%5d"%a)
# print("a=%05d"%a)
# print("a=%-5d"%a)
# print("a=%-10d"%a)

#编写一个程序，判断输入的成绩是否及格

# grade=eval(input("请输入要查询的成绩："))
# if grade<0 or grade>100:
#     print("成绩%d有误"%grade)

# elif  grade<60:
#     print("成绩%d不及格"%grade)
# elif grade<80:
#     print("成绩%d良好"%grade)
# elif grade<100:
#     print("成绩%d优秀"%grade)
# elif  grade==100:
#     print("成绩%d完美"%grade)

#编写一个程序，统计步数兑换奖品
# bs=eval(input("请输入你的步数"))
# if 0>bs:
#     print('输入有误，步数要大于0')
# elif bs<100000:
#     print('无奖励')
# elif bs<150000:
#     print("优秀奖")
# elif bs<300000:
#      print("三等奖")
# elif bs<450000:
#      print("二等奖")
# elif bs >=450000:
#      print("一等奖")
#编写程序计算s=1+2+3+...+100的值
# i=1
# s=0
# while (i<=100):
#     s=s+i
#     i=i+1

# print(s)
# for i in range(1,10):
#     for y in range(1,i+1):
#         print("*",end="")
#     print("")


#99乘法表
# for i in range(1,10):
#     for y in range(1,i+1):
#         print("{0}*{1}={2}".format(y,i,i*y),end=" ")
#     print("")

#计算满足1+2+3+n<100的最大整数n

# s=0
# i=1
# while True:
#     s=s+i
#     if(s>10000):
#         print("sss=",s,"y=",i)
#         break
#     i+=1
#     print("s=",s,"+",i,"=",s+i)

# print(i)
# s=0
# for y in range(1,10000):
#     s=s+y
#     if s>10000:
#         print("py=",y)
#         break
#     print("y=",y,"s=",s)


  #输出1-50之间所有的奇数，一行5个格式进行输出     
# count=0
# for x in range(1,51):
#     if x%2==0: 
#         continue
#     count=count+1
#     print(x,end=" ")
#     if(count%5==0):
#         print("")
        
#百钱买百鸡
# for x in range(1,20):
#     for y in range (1,33):
#         z=100-x-y
#         if 5*x+3*y+1/3*z==100:
#             print(x,y,z)
      
from gettext import find
from random import random


# s="pythontt"
# print(s[2])
# y="python"
# print(len(y))
            
# print(y*2)
# print(min(y))
# print(max(y))        

# print(s.find('t',0,4))
# print(s.count("t"))
# print(s.lower())
# print(s.upper())
# lb=[1,3,4,55,45,"hello"]
# print(len(lb))
# lb.append("pyhton")
# lc=["wp",True]
# lb.extend("ddd")
# lb.insert(2,"99")
# lb.extend(lc)
# print(lb)
# print(lb.index(3))
# print(lb.count("d"))
# del(lb[1])
# print(lb)
# lb.pop()
# print(lb)
# lb.remove("99")
# print(lb)
# print(tuple(lb))

# print(divmod(3,5))
# print(round(3.5455,3))
# a=10
# import random

# print(random.random())
# print(random.randint(10,20))
# def test(s):
#     print("hello methond",s)

# test("hhhh")
# test(55)

# def maxii(x,y):
#     if x>y:
#        return x
#     elif x<y:
#         return y
# print(maxii(4,55))


#

# hour=eval(input("请输入上网小时数："))
# money=0
# if hour<=0:
#   money=0
# elif(0<hour<=10):
#   money=30
# elif hour<50:
#   money=3*hour
# elif hour>=50:
#   money=2.5*hour
# print("该月的上网费用为：",money)


#水仙花数 一个三位数



