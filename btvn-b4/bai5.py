a=input("nhap sau ky tu")
a=a.split()
b=tuple(a)
print(b)
d=int(0)
for i in range(len(b)):
    if a[i].isdigit() :
        d+=1
print("so phan tu so trong tuple b la :",d)







# List=[]
# for i in range (len(a)):
#     List.append(a[i])
# List=tuple(List)
# print("")


