import math

#完全平方数，如果一个数可以表现成某个正数的平方形式
#一个数加上100是一个完全平方数，再加上168也是一个完全平方数，找出第一个符号改要求的数
i=1
while True:
    x=math.sqrt(i+100)
    y=math.sqrt(i+100+168)
    if int(x)==x and int(y)==y:
        print(i)
        break
    else:
        i+=1



