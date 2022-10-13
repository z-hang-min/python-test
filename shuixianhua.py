#水仙花数，它的个位数的数字的3次幂之和等于它本身，请编程找出100-999所有水仙花数（153=1e3+5e3+3e3）

#提取个位，十位，bai位
from operator import ge, index

count=0
for x in range(100,1000):
    bai=x//100
    shi=x//10%10
    ge=x%10
    if(bai**3+shi**3+ge**3==x):
        print(x,end=" ")
        count+=1
        if count%2==0:
            print("")
    
#求3000-6000之间的奇数中，找出各位数字之和是30的倍数的数字，并计算这些数值之和
s=0
for a in range(3000,6001):
    if a%2==0:
        continue
    qian=a//1000
    bai=a//100%10
    shi=a//10%10
    ge=a%10
    if (qian+bai+shi+ge)%30==0:
        s=s+a
        print("正确的数是：",a)
        print("s是：",s)
print("s是：",s)
      


