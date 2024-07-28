k= int(input("nhap k: "))
a=list()
for i in range(k):
    a.append(int(input()))

n=int(input("nhap n:"))
m=int(input("nhap m:"))
d=int(0)
x=list()
if n*m<=len(a):
    for i in range (n):
        y=list()
        for j in range(m):
            y.append(a[d])
            d=d+1
        x.append(y)
    print(x)
else:
    print("NO")
