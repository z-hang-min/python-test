# 求pi的近似值
#已知pi/4=1-1/3+1/5-1+1/7+...根据前5000项来计算近似值
from itertools import count


s=0
count=0
for x in range(1,10000001):
    if x%2==0:
        continue
    # print("x的值",x)
    count=count+1
    if count%2==1:
        s=s+1/x
    else:
        s=s+(-1/x)
print("pi的近似值为；",4*s)

    

