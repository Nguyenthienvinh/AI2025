n=int(input("nhap n:"))
settong=list()
for i in range (n):
    settong.append(int(input()))
settong.sort()
k=int(input())
sum=int(0)
setcon=[]
for i in range(n):
    sum+=settong[i]
    if sum>k:
        break
    setcon.append(settong[i])

setcon=set(setcon)
print(setcon)





