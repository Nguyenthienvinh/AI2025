a=[input(),input()]
b=[]
for i in range (2):
    for j in range (len(a[i])):
        b.append(a[i][j])
b=set(b)
b=list(b)
print(b)

