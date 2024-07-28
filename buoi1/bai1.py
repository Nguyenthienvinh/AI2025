# a=list()
# n=int(input("nhap vao n phan tu "))
# for i in range (n):
#     a.append(int(input("a[""]=")))
# x=int(input("nhap x:"))
# if x in a:
#     print("yes")
# else :
#     print("no")
# a[2:7]=[8,5,4,0,1,3]
#
# print("max a=",max(a))
# print("min a=",min(a))
# y=int(input(" nhap vao y "))
# a.insert(0,y)
# d=int(1)
# for i in range (n-1):
#     if a[i]<=a[i+1]:
#         d=d+1
# if d==n :
#     print("Tang")
# elif d==1 :
#     print('giam')
# else:
#     print("No")
# b=list()
# N=int(input("nhap N:"))
# print(a)
# sum=a[0]
# for i in range (1,N+1):
#     sum+=a[i]
#     b.append(sum)
import math

c= [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]

b=sorted(c)
for i in range(len(c)):
    c[i]=abs(c[i])
c.sort()





